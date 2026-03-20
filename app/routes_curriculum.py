import json
import os
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import User, LessonProgress
from app.auth import get_current_user, require_user

router = APIRouter(prefix="/api/curriculum", tags=["curriculum"])

# Load curriculum data once at startup
_curriculum = None

def get_curriculum():
    global _curriculum
    if _curriculum is None:
        path = os.path.join(os.path.dirname(__file__), "..", "data", "curriculum.json")
        with open(path, "r", encoding="utf-8") as f:
            _curriculum = json.load(f)
    return _curriculum


@router.get("/levels")
async def list_levels(
    db: AsyncSession = Depends(get_db),
    user: User | None = Depends(get_current_user),
):
    """Return all levels with week titles (no full lesson content) + user progress."""
    data = get_curriculum()
    uid = user.id if user else None
    progress = {}
    if uid:
        result = await db.execute(
            select(LessonProgress).where(LessonProgress.user_id == uid)
        )
        for p in result.scalars().all():
            key = f"{p.level_id}-{p.week}-{p.day}"
            progress[key] = {"completed": p.completed, "quiz_score": p.quiz_score, "quiz_total": p.quiz_total}

    levels_out = []
    for level in data["levels"]:
        weeks_out = []
        for week in level["weeks"]:
            days_summary = []
            completed_count = 0
            for day in week["days"]:
                key = f"{level['id']}-{week['week']}-{day['day']}"
                prog = progress.get(key, {})
                is_done = prog.get("completed", False)
                if is_done:
                    completed_count += 1
                days_summary.append({
                    "day": day["day"],
                    "topic": day.get("topic_es") or day.get("topic", ""),
                    "topic_en": day.get("topic_en", ""),
                    "completed": is_done,
                    "quiz_score": prog.get("quiz_score"),
                    "quiz_total": prog.get("quiz_total"),
                })
            weeks_out.append({
                "week": week["week"],
                "title": week["title"],
                "days": days_summary,
                "completed_days": completed_count,
                "total_days": len(week["days"]),
            })
        levels_out.append({
            "id": level["id"],
            "name": level["name"],
            "description": level["description"],
            "weeks": weeks_out,
        })
    return {"levels": levels_out}


@router.get("/lesson/{level_id}/{week}/{day}")
async def get_lesson(level_id: str, week: int, day: int):
    """Return full lesson content for a specific day."""
    data = get_curriculum()
    for level in data["levels"]:
        if level["id"] == level_id:
            for w in level["weeks"]:
                if w["week"] == week:
                    for d in w["days"]:
                        if d["day"] == day:
                            return {"level": level_id, "week": week, **d}
    raise HTTPException(status_code=404, detail="Lesson not found")


@router.post("/progress/{level_id}/{week}/{day}")
async def mark_lesson_complete(
    level_id: str, week: int, day: int,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(require_user),
):
    """Mark a lesson as completed."""
    result = await db.execute(
        select(LessonProgress).where(and_(
            LessonProgress.user_id == user.id,
            LessonProgress.level_id == level_id,
            LessonProgress.week == week,
            LessonProgress.day == day,
        ))
    )
    prog = result.scalars().first()
    if prog:
        prog.completed = True
        from sqlalchemy import func
        prog.completed_at = func.now()
    else:
        from sqlalchemy import func
        prog = LessonProgress(
            user_id=user.id, level_id=level_id, week=week, day=day,
            completed=True, completed_at=func.now()
        )
        db.add(prog)
    await db.commit()
    return {"status": "ok", "completed": True}


@router.post("/quiz/{level_id}/{week}/{day}")
async def submit_quiz(
    level_id: str, week: int, day: int,
    payload: dict,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(require_user),
):
    """Submit quiz answers and record score. Body: {"answers": [0, 1, 2]}"""
    answers = payload.get("answers", [])
    # Get the lesson to check answers
    data = get_curriculum()
    lesson = None
    for level in data["levels"]:
        if level["id"] == level_id:
            for w in level["weeks"]:
                if w["week"] == week:
                    for d in w["days"]:
                        if d["day"] == day:
                            lesson = d
                            break
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")

    quiz = lesson.get("quiz", [])
    correct = 0
    total = len(quiz)
    results = []
    for i, q in enumerate(quiz):
        user_answer = answers[i] if i < len(answers) else -1
        is_correct = user_answer == q["answer"]
        if is_correct:
            correct += 1
        results.append({"correct": is_correct, "correct_answer": q["answer"], "user_answer": user_answer})

    # Save progress
    result = await db.execute(
        select(LessonProgress).where(and_(
            LessonProgress.user_id == user.id,
            LessonProgress.level_id == level_id,
            LessonProgress.week == week,
            LessonProgress.day == day,
        ))
    )
    prog = result.scalars().first()
    from sqlalchemy import func
    if prog:
        prog.quiz_score = correct
        prog.quiz_total = total
        prog.completed = True
        prog.completed_at = func.now()
    else:
        prog = LessonProgress(
            user_id=user.id, level_id=level_id, week=week, day=day,
            completed=True, quiz_score=correct, quiz_total=total, completed_at=func.now()
        )
        db.add(prog)
    await db.commit()
    return {"score": correct, "total": total, "results": results}
