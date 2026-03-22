import datetime
from pydantic import BaseModel, ConfigDict


# ── Auth ──

class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str
    display_name: str = ""


class LoginRequest(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class PasswordChange(BaseModel):
    current_password: str
    new_password: str


# ── Users ──

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    email: str
    display_name: str
    is_admin: bool
    is_active: bool
    currency: str
    created_at: datetime.datetime


# ── Accounts ──

class AccountCreate(BaseModel):
    name: str
    account_type: str = "checking"
    institution: str = ""
    balance: float = 0.0
    currency: str = "USD"


class AccountUpdate(BaseModel):
    name: str | None = None
    account_type: str | None = None
    institution: str | None = None
    balance: float | None = None


class AccountOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    account_type: str
    institution: str
    balance: float
    currency: str
    is_active: bool
    created_at: datetime.datetime


# ── Transactions ──

class TransactionCreate(BaseModel):
    account_id: int | None = None
    date: datetime.date
    description: str
    amount: float
    category: str = "Uncategorized"
    subcategory: str = ""
    notes: str = ""


class TransactionUpdate(BaseModel):
    account_id: int | None = None
    date: datetime.date | None = None
    description: str | None = None
    amount: float | None = None
    category: str | None = None
    subcategory: str | None = None
    notes: str | None = None
    is_recurring: bool | None = None


class TransactionOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    account_id: int | None
    date: datetime.date
    description: str
    amount: float
    category: str
    subcategory: str
    is_recurring: bool
    notes: str
    source: str
    created_at: datetime.datetime


# ── Uploads ──

class UploadOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    filename: str
    file_type: str
    row_count: int
    status: str
    error_message: str | None
    created_at: datetime.datetime
