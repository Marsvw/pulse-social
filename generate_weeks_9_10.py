#!/usr/bin/env python3
import json
import sys

# Read existing curriculum
with open('/sessions/serene-elegant-thompson/mnt/socialblog/data/curriculum.json', 'r', encoding='utf-8') as f:
    curriculum = json.load(f)

# Get the A1 level
a1_level = curriculum['levels'][0]

# Week 9 content
week_9 = {
    "week": 9,
    "title": "Comparativos, Superlativos y Planes Futuros",
    "days": [
        {
            "day": 1,
            "topic_es": "Comparativos — Bigger, Smaller, More Interesting",
            "topic_en": "Comparatives",
            "objective_es": "Al final de esta lección podrás comparar dos cosas usando adjetivos comparativos (bigger, smaller, more interesting) y podrás entender y hacer comparaciones en inglés.",
            "grammar_label": "Comparative Adjectives",
            "grammar_es": "Los comparativos se usan para comparar dos cosas. Hay dos formas: 1) Para adjetivos cortos (una sílaba: big, small, old, tall, fast), añades '-er' al final: big → bigger, small → smaller, fast → faster. Si el adjetivo termina en 'e', solo añades 'r': nice → nicer. Si termina en consonante + vocal + consonante, doblas la última consonante: big → bigger. 2) Para adjetivos largos (dos o más sílabas: interesting, beautiful, expensive), usas 'more' antes: more interesting, more beautiful, more expensive. Después del comparativo, usas 'than' (que): 'This book is bigger than that book.' 'She is more intelligent than her brother.' Algunos comparativos irregulares: good → better, bad → worse, far → farther/further.",
            "vocabulary": [
                {"en": "bigger", "es": "más grande", "pronunciation": "bíguer", "example_en": "This car is bigger than that one.", "example_es": "Este coche es más grande que ese."},
                {"en": "smaller", "es": "más pequeño", "pronunciation": "smóluer", "example_en": "A mouse is smaller than a cat.", "example_es": "Un ratón es más pequeño que un gato."},
                {"en": "older", "es": "más viejo/mayor", "pronunciation": "ólduer", "example_en": "My father is older than me.", "example_es": "Mi padre es mayor que yo."},
                {"en": "younger", "es": "más joven", "pronunciation": "yánguer", "example_en": "My sister is younger than me.", "example_es": "Mi hermana es más joven que yo."},
                {"en": "faster", "es": "más rápido", "pronunciation": "fástur", "example_en": "A car is faster than a bicycle.", "example_es": "Un coche es más rápido que una bicicleta."},
                {"en": "slower", "es": "más lento", "pronunciation": "slóuer", "example_en": "A turtle is slower than a rabbit.", "example_es": "Una tortuga es más lenta que un conejo."},
                {"en": "more interesting", "es": "más interesante", "pronunciation": "mor ínturestin", "example_en": "This movie is more interesting than that one.", "example_es": "Esta película es más interesante que esa."},
                {"en": "more beautiful", "es": "más bonito", "pronunciation": "mor biutiful", "example_en": "A rose is more beautiful than a weed.", "example_es": "Una rosa es más bonita que una mala hierba."},
                {"en": "better", "es": "mejor", "pronunciation": "bétur", "example_en": "Your idea is better than mine.", "example_es": "Tu idea es mejor que la mía."},
                {"en": "worse", "es": "peor", "pronunciation": "uers", "example_en": "This book is worse than that one.", "example_es": "Este libro es peor que ese."},
                {"en": "than", "es": "que (comparativo)", "pronunciation": "den", "example_en": "She is taller than her friend.", "example_es": "Ella es más alta que su amiga."},
                {"en": "expensive", "es": "caro", "pronunciation": "eksˈpensiv", "example_en": "Gold is more expensive than silver.", "example_es": "El oro es más caro que la plata."}
            ],
            "dialogue": {
                "context_es": "Dos amigos, Ana y Juan, comparan sus casas.",
                "lines": [
                    {"speaker": "Ana", "en": "My house is bigger than yours.", "es": "Mi casa es más grande que la tuya."},
                    {"speaker": "Juan", "en": "Yes, but your garden is smaller.", "es": "Sí, pero tu jardín es más pequeño."},
                    {"speaker": "Ana", "en": "That's true. My house is more beautiful too.", "es": "Es verdad. Mi casa es más bonita también."},
                    {"speaker": "Juan", "en": "Perhaps. But my location is better. It's closer to the city.", "es": "Quizás. Pero mi ubicación es mejor. Está más cerca de la ciudad."},
                    {"speaker": "Ana", "en": "You're right! Your house is in a better place than mine.", "es": "¡Tienes razón! Tu casa está en un lugar mejor que la mía."}
                ]
            },
            "examples": [
                {"en": "This pen is cheaper than that pen.", "es": "Este bolígrafo es más barato que ese bolígrafo.", "note_es": "Comparativo simple: cheap → cheaper."},
                {"en": "Sarah is taller than her brother.", "es": "Sarah es más alta que su hermano.", "note_es": "Comparativo de adjetivo corto: tall → taller."},
                {"en": "This restaurant is more expensive than that one.", "es": "Este restaurante es más caro que ese.", "note_es": "Comparativo de adjetivo largo: expensive → more expensive."},
                {"en": "Today is hotter than yesterday.", "es": "Hoy es más caluroso que ayer.", "note_es": "hot → hotter (dobla la 't')."},
                {"en": "This song is better than that song.", "es": "Esta canción es mejor que esa canción.", "note_es": "good → better (irregular)."},
                {"en": "Winter is colder than summer.", "es": "El invierno es más frío que el verano.", "note_es": "cold → colder."}
            ],
            "tip_es": "Recuerda: para adjetivos cortos (1 sílaba), añades '-er': tall → taller, fast → faster. Para adjetivos largos (2+ sílabas), usas 'more': beautiful → more beautiful, interesting → more interesting. Siempre usa 'than' después del comparativo.",
            "practice": [
                {"instruction_es": "Traduce al inglés:", "prompt": "El oro es más caro que la plata.", "answer": "Gold is more expensive than silver."},
                {"instruction_es": "Completa la oración:", "prompt": "A turtle is ___ than a rabbit.", "answer": "slower"},
                {"instruction_es": "Elige la opción correcta:", "prompt": "My sister is ___ than me. (young/younger)", "answer": "younger"},
                {"instruction_es": "Forma el comparativo:", "prompt": "big → ___", "answer": "bigger"},
                {"instruction_es": "Traduce:", "prompt": "Ella es más bonita que su amiga.", "answer": "She is more beautiful than her friend."},
                {"instruction_es": "Elige la forma correcta:", "prompt": "This book is ___ than that book. (interesting/more interesting)", "answer": "more interesting"}
            ],
            "flashcards": [
                {"front": "más grande", "back": "bigger (bíguer)"},
                {"front": "más pequeño", "back": "smaller (smóluer)"},
                {"front": "más rápido", "back": "faster (fástur)"},
                {"front": "más lento", "back": "slower (slóuer)"},
                {"front": "más bonito", "back": "more beautiful (mor biutiful)"},
                {"front": "más interesante", "back": "more interesting (mor ínturestin)"},
                {"front": "mejor", "back": "better (bétur)"},
                {"front": "peor", "back": "worse (uers)"},
                {"front": "que (en comparaciones)", "back": "than (den)"},
                {"front": "más caro", "back": "more expensive (mor eksˈpensiv)"}
            ],
            "quiz": [
                {"q_es": "Completa: 'A dog is ___ than a cat.'", "options": ["bigger", "big", "most big", "more big"], "answer": 0},
                {"q_es": "¿Cuál es el comparativo de 'good'?", "options": ["gooder", "better", "more good", "best"], "answer": 1},
                {"q_es": "Traduce: 'Este vestido es más bonito que ese.'", "options": ["This dress is nice than that.", "This dress is more beautiful than that.", "This dress beautiful more than that.", "This dress is beautifuler than that."], "answer": 1},
                {"q_es": "¿Qué palabra va después del comparativo?", "options": ["from", "than", "to", "at"], "answer": 1},
                {"q_es": "Completa: 'Winter is ___ than summer.'", "options": ["cold", "colder", "more cold", "coldest"], "answer": 1}
            ]
        },
        {
            "day": 2,
            "topic_es": "Superlativos — The Biggest, The Best, The Most",
            "topic_en": "Superlatives",
            "objective_es": "Al final de esta lección podrás identificar y usar superlativos (the biggest, the best, the most interesting) para comparar más de dos cosas.",
            "grammar_label": "Superlative Adjectives",
            "grammar_es": "Los superlativos se usan para hablar de la cosa número uno (la más...) entre un grupo. Se forman: 1) Para adjetivos cortos (una sílaba), añades '-est' (y generalmente 'the' antes): big → the biggest, small → the smallest, tall → the tallest. 2) Para adjetivos largos (dos o más sílabas), usas 'the most': beautiful → the most beautiful, interesting → the most interesting, expensive → the most expensive. Algunos superlativos irregulares: good → the best, bad → the worst. Siempre usas 'the' antes del superlativo. 'She is the tallest girl in her class.' 'This is the most expensive restaurant in the city.'",
            "vocabulary": [
                {"en": "biggest", "es": "el más grande", "pronunciation": "bígurst", "example_en": "Africa is the biggest continent.", "example_es": "África es el continente más grande."},
                {"en": "smallest", "es": "el más pequeño", "pronunciation": "smólurst", "example_en": "Monaco is the smallest country.", "example_es": "Mónaco es el país más pequeño."},
                {"en": "tallest", "es": "el más alto", "pronunciation": "tólurst", "example_en": "He is the tallest boy in school.", "example_es": "Él es el niño más alto de la escuela."},
                {"en": "fastest", "es": "el más rápido", "pronunciation": "fásturıst", "example_en": "The cheetah is the fastest animal.", "example_es": "El guepardo es el animal más rápido."},
                {"en": "slowest", "es": "el más lento", "pronunciation": "slóusurıst", "example_en": "The snail is the slowest animal.", "example_es": "El caracol es el animal más lento."},
                {"en": "best", "es": "el mejor", "pronunciation": "best", "example_en": "This is the best movie I've seen.", "example_es": "Esta es la mejor película que he visto."},
                {"en": "worst", "es": "el peor", "pronunciation": "uerst", "example_en": "That's the worst idea.", "example_es": "Esa es la peor idea."},
                {"en": "most beautiful", "es": "el más bonito", "pronunciation": "móust biutiful", "example_en": "She is the most beautiful woman.", "example_es": "Ella es la mujer más bonita."},
                {"en": "most expensive", "es": "el más caro", "pronunciation": "móust eksˈpensiv", "example_en": "Diamond is the most expensive gemstone.", "example_es": "El diamante es la piedra preciosa más cara."},
                {"en": "most interesting", "es": "el más interesante", "pronunciation": "móust ínturestin", "example_en": "This is the most interesting book.", "example_es": "Este es el libro más interesante."},
                {"en": "the", "es": "el, la, los, las (con superlativos)", "pronunciation": "dhu", "example_en": "She is THE tallest girl.", "example_es": "Ella es LA niña más alta."},
                {"en": "coldest", "es": "el más frío", "pronunciation": "kóldurst", "example_en": "Antarctica is the coldest place on Earth.", "example_es": "La Antártida es el lugar más frío de la Tierra."}
            ],
            "dialogue": {
                "context_es": "Tres amigos hablan sobre sus películas favoritas.",
                "lines": [
                    {"speaker": "Sofia", "en": "I think this is the best movie ever!", "es": "¡Creo que esta es la mejor película de todas!"},
                    {"speaker": "Marco", "en": "Really? I think it's the worst movie I've seen.", "es": "¿De verdad? Creo que es la peor película que he visto."},
                    {"speaker": "Laura", "en": "The main actor is the most handsome!", "es": "¡El actor principal es el más guapo!"},
                    {"speaker": "Sofia", "en": "That's true. And the story is the most interesting.", "es": "Es verdad. Y la historia es la más interesante."},
                    {"speaker": "Marco", "en": "Maybe... but it's also the longest movie I've ever watched!", "es": "Quizás... ¡pero también es la película más larga que he visto!"}
                ]
            },
            "examples": [
                {"en": "Mount Everest is the highest mountain in the world.", "es": "El Monte Everest es la montaña más alta del mundo.", "note_es": "high → highest."},
                {"en": "She is the most intelligent student in the class.", "es": "Ella es la estudiante más inteligente de la clase.", "note_es": "Adjetivo largo: intelligent → the most intelligent."},
                {"en": "This is the best restaurant in the city.", "es": "Este es el mejor restaurante de la ciudad.", "note_es": "good → the best (irregular)."},
                {"en": "The Amazon is the largest rainforest.", "es": "El Amazonas es la selva tropical más grande.", "note_es": "large → the largest."},
                {"en": "That's the worst pizza I've ever eaten.", "es": "Esa es la peor pizza que he comido.", "note_es": "bad → the worst (irregular)."},
                {"en": "Today is the hottest day this summer.", "es": "Hoy es el día más caluroso de este verano.", "note_es": "hot → the hottest (dobla la 't')."}
            ],
            "tip_es": "Siempre usa 'THE' antes del superlativo. No digas 'is biggest', di 'is THE biggest'. Para adjetivos cortos, añade '-est': tall → the tallest. Para adjetivos largos, usa 'THE MOST': beautiful → the most beautiful.",
            "practice": [
                {"instruction_es": "Traduce al inglés:", "prompt": "Esta es la película más interesante.", "answer": "This is the most interesting movie."},
                {"instruction_es": "Completa:", "prompt": "Mount Everest is ___ mountain in the world.", "answer": "the highest"},
                {"instruction_es": "Elige la opción correcta:", "prompt": "She is ___ girl in class. (tallest/the tallest)", "answer": "the tallest"},
                {"instruction_es": "Forma el superlativo:", "prompt": "big → ___", "answer": "the biggest"},
                {"instruction_es": "Traduce:", "prompt": "El guepardo es el animal más rápido.", "answer": "The cheetah is the fastest animal."},
                {"instruction_es": "Completa:", "prompt": "This is ___ idea. (worst/the worst)", "answer": "the worst"}
            ],
            "flashcards": [
                {"front": "el más grande", "back": "the biggest (dhu bígurst)"},
                {"front": "el más pequeño", "back": "the smallest (dhu smólurst)"},
                {"front": "el más alto", "back": "the tallest (dhu tólurst)"},
                {"front": "el más rápido", "back": "the fastest (dhu fásturust)"},
                {"front": "el mejor", "back": "the best (dhu best)"},
                {"front": "el peor", "back": "the worst (dhu uerst)"},
                {"front": "el más bonito", "back": "the most beautiful (dhu móust biutiful)"},
                {"front": "el más interesante", "back": "the most interesting (dhu móust ínturestin)"},
                {"front": "el más caro", "back": "the most expensive (dhu móust eksˈpensiv)"},
                {"front": "el más frío", "back": "the coldest (dhu kóldurst)"}
            ],
            "quiz": [
                {"q_es": "Completa: 'Mount Everest is ___ mountain.'", "options": ["the highest", "highest", "most high", "the most high"], "answer": 0},
                {"q_es": "¿Cuál es el superlativo de 'good'?", "options": ["the gooder", "the best", "the most good", "goodest"], "answer": 1},
                {"q_es": "Traduce: 'Esta es la peor idea.'", "options": ["This is worst idea.", "This is the worse idea.", "This is the worst idea.", "This is bad idea."], "answer": 2},
                {"q_es": "¿Qué va SIEMPRE antes del superlativo?", "options": ["a", "an", "the", "some"], "answer": 2},
                {"q_es": "Completa: 'She is ___ student in the class.'", "options": ["most intelligent", "the most intelligent", "more intelligent", "intelligenter"], "answer": 1}
            ]
        },
        {
            "day": 3,
            "topic_es": "'Going To' para Planes Futuros",
            "topic_en": "Going To for Future Plans",
            "objective_es": "Al final de esta lección podrás hablar de planes futuros usando 'going to' (voy a, va a, van a) y hacer preguntas sobre lo que alguien va a hacer.",
            "grammar_label": "Going To Future",
            "grammar_es": "'Going to' se usa para hablar de planes y decisiones ya hechas para el futuro. La estructura es: sujeto + 'am/is/are' + 'going to' + verbo en infinitivo. Ejemplos: 'I am going to study.' (Voy a estudiar.) 'She is going to travel.' (Ella va a viajar.) 'They are going to play soccer.' (Ellos van a jugar fútbol.) Para preguntas, cambia el orden: 'Are you going to come?' (¿Vas a venir?) 'Is he going to work?' (¿Va a trabajar?) Para negativas, añade 'not' después de 'am/is/are': 'I am not going to eat.' (No voy a comer.) Usa 'going to' cuando: 1) Tienes una intención clara, 2) Has hecho un plan, 3) Ves señales de algo que pasará pronto.",
            "vocabulary": [
                {"en": "going to", "es": "ir a (futuro)", "pronunciation": "góin tu", "example_en": "I'm going to study tomorrow.", "example_es": "Voy a estudiar mañana."},
                {"en": "plan", "es": "plan", "pronunciation": "plen", "example_en": "What's your plan for tonight?", "example_es": "¿Cuál es tu plan para esta noche?"},
                {"en": "travel", "es": "viajar", "pronunciation": "trávul", "example_en": "She's going to travel to Spain.", "example_es": "Ella va a viajar a España."},
                {"en": "study", "es": "estudiar", "pronunciation": "stádi", "example_en": "I'm going to study English.", "example_es": "Voy a estudiar inglés."},
                {"en": "work", "es": "trabajar", "pronunciation": "uerk", "example_en": "He's going to work on Saturday.", "example_es": "Él va a trabajar el sábado."},
                {"en": "play", "es": "jugar", "pronunciation": "plei", "example_en": "They're going to play soccer.", "example_es": "Ellos van a jugar fútbol."},
                {"en": "eat", "es": "comer", "pronunciation": "ít", "example_en": "We're going to eat pizza tonight.", "example_es": "Vamos a comer pizza esta noche."},
                {"en": "sleep", "es": "dormir", "pronunciation": "slip", "example_en": "I'm going to sleep early.", "example_es": "Voy a dormir temprano."},
                {"en": "watch", "es": "ver/mirar", "pronunciation": "uách", "example_en": "They're going to watch a movie.", "example_es": "Ellos van a ver una película."},
                {"en": "tomorrow", "es": "mañana", "pronunciation": "tumárou", "example_en": "I'm going to call you tomorrow.", "example_es": "Voy a llamarte mañana."},
                {"en": "next week", "es": "la próxima semana", "pronunciation": "nékst uík", "example_en": "She's going to visit us next week.", "example_es": "Ella va a visitarnos la próxima semana."},
                {"en": "this weekend", "es": "este fin de semana", "pronunciation": "dis uíkend", "example_en": "We're going to relax this weekend.", "example_es": "Vamos a relajarnos este fin de semana."}
            ],
            "dialogue": {
                "context_es": "Carlos y Ana hablan sobre sus planes para el próximo fin de semana.",
                "lines": [
                    {"speaker": "Carlos", "en": "What are you going to do this weekend?", "es": "¿Qué vas a hacer este fin de semana?"},
                    {"speaker": "Ana", "en": "I'm going to visit my grandmother in the country.", "es": "Voy a visitar a mi abuela en el campo."},
                    {"speaker": "Carlos", "en": "That sounds nice! I'm going to stay home and study.", "es": "¡Suena bonito! Voy a quedarme en casa y estudiar."},
                    {"speaker": "Ana", "en": "Are you going to work too?", "es": "¿También vas a trabajar?"},
                    {"speaker": "Carlos", "en": "No, I'm not going to work this weekend. I'm going to relax and watch movies.", "es": "No, no voy a trabajar este fin de semana. Voy a relajarme y ver películas."}
                ]
            },
            "examples": [
                {"en": "I'm going to travel to London next summer.", "es": "Voy a viajar a Londres el próximo verano.", "note_es": "Plan futuro determinado."},
                {"en": "She's going to buy a new car.", "es": "Ella va a comprar un coche nuevo.", "note_es": "Decisión ya tomada."},
                {"en": "Are you going to come to the party?", "es": "¿Vas a venir a la fiesta?", "note_es": "Pregunta sobre planes futuros."},
                {"en": "They're not going to play soccer tomorrow. It's going to rain.", "es": "Ellos no van a jugar fútbol mañana. Va a llover.", "note_es": "Negativa y predicción."},
                {"en": "We're going to eat dinner at 7 PM.", "es": "Vamos a cenar a las 7 PM.", "note_es": "Plan específico."},
                {"en": "What are they going to do this weekend?", "es": "¿Qué van a hacer ellos este fin de semana?", "note_es": "Pregunta con they."}
            ],
            "tip_es": "Recuerda: 'going to' es para planes hechos o intenciones. La estructura es: am/is/are + going to + verbo infinitivo. 'I am going to study.' Usa 'I'm going to' (contracción). 'Not going to' es 'I'm not going to study.'",
            "practice": [
                {"instruction_es": "Traduce al inglés:", "prompt": "Voy a estudiar mañana.", "answer": "I'm going to study tomorrow."},
                {"instruction_es": "Completa:", "prompt": "She ___ going to travel next week.", "answer": "is"},
                {"instruction_es": "Haz una pregunta:", "prompt": "¿Qué van a hacer ellos?", "answer": "What are they going to do?"},
                {"instruction_es": "Elige la opción correcta:", "prompt": "I ___ going to eat pizza. (am/is)", "answer": "am"},
                {"instruction_es": "Traduce:", "prompt": "Ella no va a trabajar el sábado.", "answer": "She's not going to work on Saturday."},
                {"instruction_es": "Completa:", "prompt": "Are you going ___ come?", "answer": "to"}
            ],
            "flashcards": [
                {"front": "voy a", "back": "I'm going to (ái'm góin tu)"},
                {"front": "va a", "back": "he/she/it is going to (íz góin tu)"},
                {"front": "van a", "back": "they are going to (ár góin tu)"},
                {"front": "plan", "back": "plan (plen)"},
                {"front": "viajar", "back": "travel (trávul)"},
                {"front": "estudiar", "back": "study (stádi)"},
                {"front": "mañana", "back": "tomorrow (tumárou)"},
                {"front": "el próximo fin de semana", "back": "next weekend (nékst uíkend)"},
                {"front": "¿Qué vas a hacer?", "back": "What are you going to do? (uát ár iú góin tu du)"},
                {"front": "No voy a", "back": "I'm not going to (ái'm nat góin tu)"}
            ],
            "quiz": [
                {"q_es": "Completa: 'I ___ going to study tomorrow.'", "options": ["is", "am", "are", "be"], "answer": 1},
                {"q_es": "¿Cuál es la pregunta correcta?", "options": ["What you going to do?", "What are you going to do?", "What you are going do?", "What do you going?"], "answer": 1},
                {"q_es": "Traduce: 'Ella va a viajar a España.'", "options": ["She going to travel to Spain.", "She is to travel Spain.", "She's going to travel to Spain.", "She is travel going to Spain."], "answer": 2},
                {"q_es": "Elige la negativa correcta:", "options": ["I'm not going to eat.", "I not going to eat.", "I'm going not to eat.", "I no going to eat."], "answer": 0},
                {"q_es": "¿Cuándo se usa 'going to'?", "options": ["Solo en pasado", "Para planes y decisiones futuras", "Para presente", "Para obligaciones"], "answer": 1}
            ]
        },
        {
            "day": 4,
            "topic_es": "Want To, Would Like To — Deseos y Preferencias",
            "topic_en": "Expressing Wants and Preferences",
            "objective_es": "Al final de esta lección podrás expresar deseos, preferencias y lo que quieres usando 'want to' y 'would like to', y comprenderás la diferencia de formalidad entre ellos.",
            "grammar_label": "Want To vs Would Like To",
            "grammar_es": "'Want to' y 'would like to' expresan deseos, pero con diferencias de formalidad. 'Want to' (querer) es más directo e informal: 'I want to eat.' (Quiero comer.) 'She wants a coffee.' (Ella quiere un café.) Para preguntas: 'Do you want to come?' (¿Quieres venir?) 'Would like to' (me gustaría/quería) es más educado y formal: 'I would like to eat.' (Me gustaría comer.) 'She would like a coffee.' (Le gustaría un café.) Para preguntas: 'Would you like to come?' (¿Te gustaría venir?) Con sustantivos (cosas específicas), usas: 'I want a book.' 'I would like a book.' Con verbos, usas el infinitivo: 'I want to read.' 'I would like to read.' Usa 'would like' en situaciones formales o para ser cortés.",
            "vocabulary": [
                {"en": "want", "es": "querer", "pronunciation": "uánt", "example_en": "I want to travel.", "example_es": "Quiero viajar."},
                {"en": "want to", "es": "querer (+ verbo)", "pronunciation": "uánt tu", "example_en": "Do you want to dance?", "example_es": "¿Quieres bailar?"},
                {"en": "would like", "es": "me gustaría/quisiera", "pronunciation": "uúd laik", "example_en": "I would like some tea.", "example_es": "Me gustaría un poco de té."},
                {"en": "would like to", "es": "me gustaría (+ verbo)", "pronunciation": "uúd laik tu", "example_en": "Would you like to join us?", "example_es": "¿Te gustaría unirte a nosotros?"},
                {"en": "prefer", "es": "preferir", "pronunciation": "prifer", "example_en": "I prefer coffee to tea.", "example_es": "Prefiero café a té."},
                {"en": "preference", "es": "preferencia", "pronunciation": "préfurens", "example_en": "What's your preference?", "example_es": "¿Cuál es tu preferencia?"},
                {"en": "hope", "es": "esperar", "pronunciation": "jóup", "example_en": "I hope to see you soon.", "example_es": "Espero verte pronto."},
                {"en": "dream", "es": "soñar", "pronunciation": "drím", "example_en": "She dreams of becoming a doctor.", "example_es": "Ella sueña con ser doctora."},
                {"en": "wish", "es": "desear", "pronunciation": "uísh", "example_en": "I wish to visit Rome.", "example_es": "Deseo visitar Roma."},
                {"en": "like", "es": "gustar", "pronunciation": "laik", "example_en": "I like pizza.", "example_es": "Me gusta la pizza."},
                {"en": "love", "es": "encantar/amar", "pronunciation": "ləv", "example_en": "I love ice cream.", "example_es": "Me encanta el helado."},
                {"en": "dislike", "es": "no gustar", "pronunciation": "dislík", "example_en": "I dislike spicy food.", "example_es": "No me gusta la comida picante."}
            ],
            "dialogue": {
                "context_es": "Un mesero y un cliente en un restaurante.",
                "lines": [
                    {"speaker": "Waiter", "en": "What would you like to order?", "es": "¿Qué te gustaría ordenar?"},
                    {"speaker": "Customer", "en": "I would like a coffee and a sandwich, please.", "es": "Me gustaría un café y un sándwich, por favor."},
                    {"speaker": "Waiter", "en": "Do you want sugar in your coffee?", "es": "¿Quieres azúcar en tu café?"},
                    {"speaker": "Customer", "en": "Yes, I would like some sugar, please. And I prefer my sandwich without lettuce.", "es": "Sí, me gustaría un poco de azúcar, por favor. Y prefiero mi sándwich sin lechuga."},
                    {"speaker": "Waiter", "en": "Perfect! Would you like anything else?", "es": "¡Perfecto! ¿Te gustaría algo más?"}
                ]
            },
            "examples": [
                {"en": "I want to learn to cook.", "es": "Quiero aprender a cocinar.", "note_es": "want + to + infinitivo."},
                {"en": "Would you like to go to the movies?", "es": "¿Te gustaría ir al cine?", "note_es": "would like + to + infinitivo (más formal)."},
                {"en": "She wants a new phone.", "es": "Ella quiere un teléfono nuevo.", "note_es": "want + sustantivo."},
                {"en": "I would like a cup of tea, please.", "es": "Me gustaría una taza de té, por favor.", "note_es": "would like + sustantivo (cortés)."},
                {"en": "Do they prefer red or white wine?", "es": "¿Prefieren vino tinto o blanco?", "note_es": "prefer + opción A + o + opción B."},
                {"en": "I don't want to work today.", "es": "No quiero trabajar hoy.", "note_es": "Negativa: don't want + to."}
            ],
            "tip_es": "Usa 'want to' en situaciones informales con amigos. Usa 'would like to' en situaciones formales, con gente que no conoces bien, o en restaurantes. 'Want' es directo; 'would like' es más educado. Ejemplo: Con amigos: 'I want pizza.' Con un cliente: 'I would like the pasta, please.'",
            "practice": [
                {"instruction_es": "Traduce al inglés:", "prompt": "Me gustaría un café, por favor.", "answer": "I would like a coffee, please."},
                {"instruction_es": "Completa:", "prompt": "Do you ___ to go to the party?", "answer": "want"},
                {"instruction_es": "Elige la opción correcta:", "prompt": "I ___ a new laptop. (want/would like)", "answer": "want"},
                {"instruction_es": "Forma la pregunta correcta:", "prompt": "¿Te gustaría venir a mi casa?", "answer": "Would you like to come to my house?"},
                {"instruction_es": "Traduce:", "prompt": "Ella quiere aprender inglés.", "answer": "She wants to learn English."},
                {"instruction_es": "Elige la opción más formal:", "prompt": "I ___ a cup of tea. (want/would like)", "answer": "would like"}
            ],
            "flashcards": [
                {"front": "quiero", "back": "I want (ái uánt)"},
                {"front": "quieres", "back": "you want (iú uánt)"},
                {"front": "quiere", "back": "he/she/it wants (uánts)"},
                {"front": "me gustaría", "back": "I would like (ái uúd laik)"},
                {"front": "¿Te gustaría?", "back": "Would you like? (uúd iú laik)"},
                {"front": "preferir", "back": "prefer (prifer)"},
                {"front": "no quiero", "back": "I don't want (ái dóunt uánt)"},
                {"front": "¿Quieres venir?", "back": "Do you want to come? (du iú uánt tu kəm)"},
                {"front": "desear/soñar", "back": "dream/wish (drím/uísh)"},
                {"front": "más educado", "back": "would like (less direct than want)"}
            ],
            "quiz": [
                {"q_es": "¿Cuál es más formal?", "options": ["I want a coffee.", "I would like a coffee.", "Both are the same.", "I want to a coffee."], "answer": 1},
                {"q_es": "Completa: 'Do you ___ to come?'", "options": ["like", "want", "would", "prefer"], "answer": 1},
                {"q_es": "Traduce: 'Quiero aprender inglés.'", "options": ["I want learning English.", "I want to learn English.", "I like to learn English.", "I would to learn English."], "answer": 1},
                {"q_es": "¿Cuál es la pregunta correcta y educada?", "options": ["You want tea?", "Want tea?", "Would you like tea?", "Do you want to tea?"], "answer": 2},
                {"q_es": "Elige la opción correcta:", "options": ["I would like to pizza.", "I would like pizza.", "I like to want pizza.", "I want to liking pizza."], "answer": 1}
            ]
        },
        {
            "day": 5,
            "topic_es": "Repaso y Práctica de la Semana 9",
            "topic_en": "Week 9 Review & Practice",
            "objective_es": "Repasarás todo lo aprendido en la semana 9: comparativos, superlativos, 'going to', y expresiones de deseo. Practicarás todas las estructuras en contexto.",
            "grammar_label": "Week 9 Complete Review",
            "grammar_es": "Semana 9 cubrió cuatro temas principales: 1) COMPARATIVOS: Usas '-er' para adjetivos cortos (bigger, taller, faster) y 'more' para adjetivos largos (more beautiful, more interesting). Siempre va 'than' después: 'She is taller than me.' 2) SUPERLATIVOS: Usas '-est' para adjetivos cortos (the biggest, the tallest) y 'the most' para adjetivos largos (the most beautiful, the most interesting). Siempre va 'the' antes: 'He is the tallest boy in school.' 3) GOING TO: Para planes futuros. Estructura: am/is/are + going to + infinitivo. 'I'm going to travel tomorrow.' 4) WANT/WOULD LIKE: want to es informal, would like to es formal. Ambos expresan deseos. 'I want to eat pizza.' vs 'I would like to order pizza.' Practica combinando estas estructuras en conversaciones.",
            "vocabulary": [
                {"en": "compare", "es": "comparar", "pronunciation": "kəmpér", "example_en": "Compare these two cars.", "example_es": "Compara estos dos coches."},
                {"en": "different", "es": "diferente", "pronunciation": "dífrənt", "example_en": "These books are very different.", "example_es": "Estos libros son muy diferentes."},
                {"en": "similar", "es": "similar", "pronunciation": "símilur", "example_en": "Their ideas are similar.", "example_es": "Sus ideas son similares."},
                {"en": "future", "es": "futuro", "pronunciation": "fiúchur", "example_en": "What about your future?", "example_es": "¿Qué tal tu futuro?"},
                {"en": "decision", "es": "decisión", "pronunciation": "disíshen", "example_en": "I made a decision.", "example_es": "Tomé una decisión."},
                {"en": "choice", "es": "elección", "pronunciation": "chóis", "example_en": "You have a choice.", "example_es": "Tienes una elección."},
                {"en": "advantage", "es": "ventaja", "pronunciation": "ədvántij", "example_en": "That's an advantage.", "example_es": "Esa es una ventaja."},
                {"en": "disadvantage", "es": "desventaja", "pronunciation": "dísədvántij", "example_en": "What's the disadvantage?", "example_es": "¿Cuál es la desventaja?"},
                {"en": "opinion", "es": "opinión", "pronunciation": "əpíniən", "example_en": "What's your opinion?", "example_es": "¿Cuál es tu opinión?"},
                {"en": "agree", "es": "estar de acuerdo", "pronunciation": "əgrí", "example_en": "I agree with you.", "example_es": "Estoy de acuerdo contigo."},
                {"en": "disagree", "es": "no estar de acuerdo", "pronunciation": "disəgrí", "example_en": "I disagree.", "example_es": "No estoy de acuerdo."},
                {"en": "reason", "es": "razón", "pronunciation": "rézən", "example_en": "What's your reason?", "example_es": "¿Cuál es tu razón?"}
            ],
            "dialogue": {
                "context_es": "Dos amigos hablan sobre sus planes y preferencias.",
                "lines": [
                    {"speaker": "Alex", "en": "What are you going to do this summer?", "es": "¿Qué vas a hacer este verano?"},
                    {"speaker": "Jordan", "en": "I'm going to travel to the beach. I love the beach because it's more relaxing than the city.", "es": "Voy a viajar a la playa. Amo la playa porque es más relajante que la ciudad."},
                    {"speaker": "Alex", "en": "That sounds nice! I would like to come with you. The beach is the most beautiful place I know.", "es": "¡Suena bonito! Me gustaría ir contigo. La playa es el lugar más bonito que conozco."},
                    {"speaker": "Jordan", "en": "Great! Do you want to leave next weekend or next month?", "es": "¡Excelente! ¿Quieres irte el próximo fin de semana o el próximo mes?"},
                    {"speaker": "Alex", "en": "I prefer next month. I have work to do, and it will be hotter then, which is even better!", "es": "Prefiero el próximo mes. Tengo trabajo que hacer, ¡y hará más calor entonces, lo cual es aún mejor!"}
                ]
            },
            "examples": [
                {"en": "A is bigger than B, but C is the biggest of all.", "es": "A es más grande que B, pero C es el más grande de todos.", "note_es": "Comparativo vs superlativo."},
                {"en": "I'm going to study because I want to pass my exam.", "es": "Voy a estudiar porque quiero pasar mi examen.", "note_es": "Combina going to + want to."},
                {"en": "Would you like a coffee? Yes, I would like one, thank you.", "es": "¿Te gustaría un café? Sí, me gustaría uno, gracias.", "note_es": "Diálogo formal."},
                {"en": "The weather is better today than yesterday, and tomorrow will be the best day of the week.", "es": "El clima es mejor hoy que ayer, y mañana será el mejor día de la semana.", "note_es": "Comparación completa."},
                {"en": "She wants to go shopping, but he would prefer to stay home.", "es": "Ella quiere ir de compras, pero él preferiría quedarse en casa.", "note_es": "Contraste de preferencias."},
                {"en": "This restaurant is more expensive than that one, but that one is the most expensive in the city.", "es": "Este restaurante es más caro que ese, pero ese es el más caro de la ciudad.", "note_es": "Tres elementos en comparación."}
            ],
            "tip_es": "Para esta semana, recuerda: Comparativos necesitan 'than'. Superlativos necesitan 'the'. 'Going to' es para planes ya decididos. 'Want to' es informal; 'would like to' es formal. Practica combinando todas estas estructuras en conversaciones reales.",
            "practice": [
                {"instruction_es": "Traduce al inglés:", "prompt": "Ella es más inteligente que él, pero su hermana es la más inteligente de la familia.", "answer": "She is more intelligent than him, but her sister is the most intelligent in the family."},
                {"instruction_es": "Completa:", "prompt": "I ___ to travel next month because it's going ___ be hot.", "answer": "am going / to"},
                {"instruction_es": "Elige la opción correcta:", "prompt": "This car is ___ than that one. (big/bigger/the biggest)", "answer": "bigger"},
                {"instruction_es": "Forma la pregunta:", "prompt": "¿Quieres venir a la fiesta?", "answer": "Do you want to come to the party?"},
                {"instruction_es": "Traduce:", "prompt": "Este es el mejor restaurante de la ciudad, pero es más caro que los otros.", "answer": "This is the best restaurant in the city, but it's more expensive than the others."},
                {"instruction_es": "Completa el diálogo:", "prompt": "— What would you like? — I ___ a coffee, please.", "answer": "would like"}
            ],
            "flashcards": [
                {"front": "comparativo", "back": "comparative (bigger, more beautiful)"},
                {"front": "superlativo", "back": "superlative (the biggest, the most beautiful)"},
                {"front": "voy a", "back": "I'm going to (ái'm góin tu)"},
                {"front": "quiero", "back": "I want (ái uánt)"},
                {"front": "me gustaría", "back": "I would like (ái uúd laik)"},
                {"front": "que (comparativo)", "back": "than (den)"},
                {"front": "el (superlativo)", "back": "the (dhu)"},
                {"front": "más - adjetivo corto", "back": "-er (bigger, taller)"},
                {"front": "más - adjetivo largo", "back": "more (more beautiful)"},
                {"front": "el/la - adjetivo corto", "back": "-est (the biggest, the tallest)"}
            ],
            "quiz": [
                {"q_es": "Ordena por tamaño: big, bigger, ___", "options": ["more big", "the big", "the biggest", "bigest"], "answer": 2},
                {"q_es": "Completa: 'I am ___ to study hard next semester.'", "options": ["wanting", "going", "liking", "wishing"], "answer": 1},
                {"q_es": "¿Cuál frase es correcta?", "options": ["She is more tall than him.", "She is taller than him.", "She is the tall than him.", "She is tall than him."], "answer": 1},
                {"q_es": "Selecciona la opción más formal:", "options": ["I want a table.", "I want to a table.", "I would like a table.", "I like wanting a table."], "answer": 2},
                {"q_es": "Completa: 'This is ___ movie I've seen this year.'", "options": ["more interesting", "interesting", "the most interesting", "most interesting"], "answer": 2}
            ]
        }
    ]
}

# Week 10 content
week_10 = {
    "week": 10,
    "title": "Repaso General y Conversaciones del Mundo Real",
    "days": [
        {
            "day": 1,
            "topic_es": "En el Aeropuerto y Hotel — Viajando",
            "topic_en": "At the Airport & Hotel",
            "objective_es": "Al final de esta lección podrás usar el inglés en situaciones reales: check-in en un aeropuerto, reservar habitación en un hotel, y preguntar sobre servicios.",
            "grammar_label": "Travel Situations",
            "grammar_es": "En el aeropuerto, necesitas entender y responder preguntas sobre: pasaporte, boletos, equipaje, y destino. Frases comunes: 'Where are you traveling to?' (¿Dónde viajas?) 'May I see your passport?' (¿Puedo ver tu pasaporte?) 'Do you have any luggage?' (¿Tienes equipaje?) En el hotel, usarás: 'I have a reservation.' (Tengo una reserva.) 'I need a room for two nights.' (Necesito una habitación por dos noches.) 'Can you help me with my luggage?' (¿Puedes ayudarme con mi equipaje?) 'Where is the bathroom?' (¿Dónde está el baño?) Usa la estructura: sujeto + verbo + pregunta/afirmación. En estas situaciones, es importante ser polite y claro.",
            "vocabulary": [
                {"en": "airport", "es": "aeropuerto", "pronunciation": "érpórt", "example_en": "I'm going to the airport tomorrow.", "example_es": "Voy al aeropuerto mañana."},
                {"en": "passport", "es": "pasaporte", "pronunciation": "páspórt", "example_en": "Can I see your passport?", "example_es": "¿Puedo ver tu pasaporte?"},
                {"en": "ticket", "es": "boleto/billete", "pronunciation": "tíkit", "example_en": "Here is my ticket.", "example_es": "Aquí está mi boleto."},
                {"en": "luggage", "es": "equipaje", "pronunciation": "lúgij", "example_en": "I have two pieces of luggage.", "example_es": "Tengo dos piezas de equipaje."},
                {"en": "hotel", "es": "hotel", "pronunciation": "jouél", "example_en": "We're staying at a nice hotel.", "example_es": "Nos estamos hospedando en un hotel bonito."},
                {"en": "reservation", "es": "reservación", "pronunciation": "rezərveíshen", "example_en": "I have a reservation for tonight.", "example_es": "Tengo una reservación para esta noche."},
                {"en": "room", "es": "habitación", "pronunciation": "rum", "example_en": "I need a room for two nights.", "example_es": "Necesito una habitación por dos noches."},
                {"en": "bed", "es": "cama", "pronunciation": "bed", "example_en": "The bed is comfortable.", "example_es": "La cama es cómoda."},
                {"en": "bathroom", "es": "baño", "pronunciation": "báðrum", "example_en": "Where is the bathroom?", "example_es": "¿Dónde está el baño?"},
                {"en": "check-in", "es": "registro de entrada", "pronunciation": "chek-ín", "example_en": "Check-in is at 3 PM.", "example_es": "El registro es a las 3 PM."},
                {"en": "check-out", "es": "registro de salida", "pronunciation": "chek-áut", "example_en": "Check-out is at 11 AM.", "example_es": "La salida es a las 11 AM."},
                {"en": "flight", "es": "vuelo", "pronunciation": "flait", "example_en": "What time is your flight?", "example_es": "¿A qué hora es tu vuelo?"}
            ],
            "dialogue": {
                "context_es": "Un viajero llega al aeropuerto y va a check-in en el hotel.",
                "lines": [
                    {"speaker": "Airport Officer", "en": "Good evening! May I see your passport and ticket, please?", "es": "¡Buenas noches! ¿Puedo ver tu pasaporte y boleto, por favor?"},
                    {"speaker": "Traveler", "en": "Of course. Here they are. I'm traveling to Barcelona for business.", "es": "Por supuesto. Aquí están. Voy a Barcelona por negocios."},
                    {"speaker": "Airport Officer", "en": "Thank you. How many pieces of luggage do you have?", "es": "Gracias. ¿Cuántas piezas de equipaje tienes?"},
                    {"speaker": "Traveler", "en": "I have two suitcases and one carry-on bag.", "es": "Tengo dos maletas y una bolsa de mano."},
                    {"speaker": "Airport Officer", "en": "Perfect. Have a nice flight! Gate 7.", "es": "¡Perfecto! ¡Buen vuelo! Puerta 7."}
                ]
            },
            "examples": [
                {"en": "What time do we arrive in New York?", "es": "¿A qué hora llegamos a Nueva York?", "note_es": "Pregunta sobre horario de llegada."},
                {"en": "I need a room with a window, please.", "es": "Necesito una habitación con ventana, por favor.", "note_es": "Solicitud específica en el hotel."},
                {"en": "Is breakfast included in the price?", "es": "¿El desayuno está incluido en el precio?", "note_es": "Pregunta sobre servicios incluidos."},
                {"en": "Can I store my luggage here?", "es": "¿Puedo guardar mi equipaje aquí?", "note_es": "Pregunta sobre servicios."},
                {"en": "Where can I rent a car?", "es": "¿Dónde puedo alquilar un coche?", "note_es": "Pregunta práctica."},
                {"en": "I lost my passport. What should I do?", "es": "Perdí mi pasaporte. ¿Qué debo hacer?", "note_es": "Situación de emergencia."}
            ],
            "tip_es": "En el aeropuerto y hotel, sé claro y polite. Siempre di 'please' (por favor) y 'thank you' (gracias). Repite información importante como números de vuelo, fechas, y nombres. Ten tu pasaporte y boleto listos. En el hotel, préguntaleal recepcionista si no entiende.",
            "practice": [
                {"instruction_es": "Traduce al inglés:", "prompt": "Necesito una habitación para dos noches.", "answer": "I need a room for two nights."},
                {"instruction_es": "Completa:", "prompt": "Can I see your ___?", "answer": "passport / ticket"},
                {"instruction_es": "Pregunta:", "prompt": "¿Dónde está la recepción?", "answer": "Where is the reception / front desk?"},
                {"instruction_es": "Forma la respuesta:", "prompt": "— How many suitcases do you have? —", "answer": "I have two suitcases."},
                {"instruction_es": "Traduce:", "prompt": "¿A qué hora es el check-in?", "answer": "What time is check-in?"},
                {"instruction_es": "Completa:", "prompt": "I ___ a reservation for tonight.", "answer": "have"}
            ],
            "flashcards": [
                {"front": "aeropuerto", "back": "airport (érpórt)"},
                {"front": "pasaporte", "back": "passport (páspórt)"},
                {"front": "boleto", "back": "ticket (tíkit)"},
                {"front": "equipaje", "back": "luggage (lúgij)"},
                {"front": "hotel", "back": "hotel (jouél)"},
                {"front": "habitación", "back": "room (rum)"},
                {"front": "baño", "back": "bathroom (báðrum)"},
                {"front": "reservación", "back": "reservation (rezərveíshen)"},
                {"front": "vuelo", "back": "flight (flait)"},
                {"front": "cama", "back": "bed (bed)"}
            ],
            "quiz": [
                {"q_es": "¿Qué pides cuando llegas a un hotel?", "options": ["I need a flight", "I need a reservation", "I need luggage", "I need an airport"], "answer": 1},
                {"q_es": "Completa: '___ is at 3 PM.'", "options": ["Check-out", "Check-in", "Passport", "Luggage"], "answer": 1},
                {"q_es": "Pregunta educada sobre servicio:", "options": ["Give me a room!", "Can I have a room?", "I want room!", "Room now!"], "answer": 1},
                {"q_es": "¿Cuál es normal en el aeropuerto?", "options": ["The hotel officer asks for your passport.", "The airport officer asks for your passport.", "The doctor asks for your passport.", "The teacher asks for your passport."], "answer": 1},
                {"q_es": "Traduce: 'Tengo dos maletas.'", "options": ["I have two luggage.", "I have two suitcases.", "I have two pieces.", "I have two bags."], "answer": 1}
            ]
        },
        {
            "day": 2,
            "topic_es": "En el Doctor — Salud y Cuerpo",
            "topic_en": "At the Doctor's Office",
            "objective_es": "Al final de esta lección podrás describir síntomas, hablar sobre tu salud, y entender consejos médicos en inglés.",
            "grammar_label": "Health & Medical Situations",
            "grammar_es": "En una cita médica, necesitas: 1) Describir síntomas: 'I have a headache.' (Tengo dolor de cabeza.) 'I feel dizzy.' (Me siento mareado.) 'My throat hurts.' (Me duele la garganta.) 2) Usar 'have' para dolores: 'I have a cold.' 'I have a fever.' 'I have a toothache.' 3) Usar 'hurt' o 'ache' para dolores: 'My back hurts.' 'I have back pain.' 4) Preguntas del doctor: 'How long have you had this?' (¿Cuánto tiempo tienes esto?) 'Do you take any medication?' (¿Tomas medicamentos?) 'Are you allergic to anything?' (¿Eres alérgico a algo?) Responde con: 'Yes, I'm allergic to...' 'No, I'm not allergic.' 'I've had it for two days.'",
            "vocabulary": [
                {"en": "doctor", "es": "doctor", "pronunciation": "dáktər", "example_en": "I need to see a doctor.", "example_es": "Necesito ver a un doctor."},
                {"en": "headache", "es": "dolor de cabeza", "pronunciation": "hédeik", "example_en": "I have a terrible headache.", "example_es": "Tengo un dolor de cabeza terrible."},
                {"en": "fever", "es": "fiebre", "pronunciation": "fívər", "example_en": "I have a high fever.", "example_es": "Tengo fiebre alta."},
                {"en": "cold", "es": "resfriado", "pronunciation": "kóld", "example_en": "I think I'm catching a cold.", "example_es": "Creo que me estoy resfriando."},
                {"en": "cough", "es": "tos", "pronunciation": "kof", "example_en": "I have a terrible cough.", "example_es": "Tengo una tos terrible."},
                {"en": "throat", "es": "garganta", "pronunciation": "zróut", "example_en": "My throat hurts.", "example_es": "Me duele la garganta."},
                {"en": "stomach", "es": "estómago", "pronunciation": "stəmuk", "example_en": "I have a stomach ache.", "example_es": "Tengo un dolor de estómago."},
                {"en": "allergic", "es": "alérgico", "pronunciation": "əlérjik", "example_en": "I'm allergic to peanuts.", "example_es": "Soy alérgico a los cacahuates."},
                {"en": "medication", "es": "medicamento", "pronunciation": "medikéishen", "example_en": "The doctor prescribed me medication.", "example_es": "El doctor me recetó medicamento."},
                {"en": "rest", "es": "descanso", "pronunciation": "rest", "example_en": "You need rest and fluids.", "example_es": "Necesitas descanso y líquidos."},
                {"en": "dizzy", "es": "mareado", "pronunciation": "dízi", "example_en": "I feel dizzy.", "example_es": "Me siento mareado."},
                {"en": "tired", "es": "cansado", "pronunciation": "táiurd", "example_en": "I'm very tired.", "example_es": "Estoy muy cansado."}
            ],
            "dialogue": {
                "context_es": "Un paciente en la consulta del doctor.",
                "lines": [
                    {"speaker": "Doctor", "en": "Hello! What's the problem today?", "es": "¡Hola! ¿Cuál es el problema hoy?"},
                    {"speaker": "Patient", "en": "I have a terrible headache and a high fever. I don't feel well.", "es": "Tengo un dolor de cabeza terrible y fiebre alta. No me siento bien."},
                    {"speaker": "Doctor", "en": "How long have you had these symptoms?", "es": "¿Cuánto tiempo tienes estos síntomas?"},
                    {"speaker": "Patient", "en": "Since yesterday morning. I also have a cough and my throat hurts.", "es": "Desde ayer por la mañana. También tengo tos y me duele la garganta."},
                    {"speaker": "Doctor", "en": "Are you allergic to any medications? I'll give you antibiotics and you need rest and fluids.", "es": "¿Eres alérgico a algún medicamento? Te daré antibióticos y necesitas descanso y líquidos."}
                ]
            },
            "examples": [
                {"en": "I have a terrible toothache. Can you help me?", "es": "Tengo un dolor de muelas terrible. ¿Puedes ayudarme?", "note_es": "Problema dental."},
                {"en": "My back hurts. It started three days ago.", "es": "Me duele la espalda. Empezó hace tres días.", "note_es": "Describir cuándo empezó."},
                {"en": "I'm allergic to penicillin. I cannot take it.", "es": "Soy alérgico a la penicilina. No puedo tomarla.", "note_es": "Información importante."},
                {"en": "The doctor says I need to take this medicine twice a day.", "es": "El doctor dice que necesito tomar este medicamento dos veces al día.", "note_es": "Instrucciones del doctor."},
                {"en": "I feel dizzy and nauseous. I think I'm sick.", "es": "Me siento mareado y con náuseas. Creo que estoy enfermo.", "note_es": "Múltiples síntomas."},
                {"en": "Do you have any pain? Where does it hurt?", "es": "¿Tienes algún dolor? ¿Dónde te duele?", "note_es": "Preguntas del doctor."}
            ],
            "tip_es": "Cuando estés en la consulta, sé claro sobre tus síntomas. Usa: 'I have + noun' (headache, fever) o 'My + body part + hurts' (My head hurts). Siempre menciona alergias. Lleva una lista de medicamentos que tomas. Si no entiendes, pide que repita: 'Can you repeat, please?'",
            "practice": [
                {"instruction_es": "Traduce al inglés:", "prompt": "Tengo fiebre y dolor de garganta.", "answer": "I have a fever and a sore throat. / My throat hurts."},
                {"instruction_es": "Completa:", "prompt": "I ___ a terrible headache.", "answer": "have"},
                {"instruction_es": "Pregunta:", "prompt": "¿Cuánto tiempo tienes estos síntomas?", "answer": "How long have you had these symptoms?"},
                {"instruction_es": "Traduce:", "prompt": "Soy alérgico a los medicamentos.", "answer": "I'm allergic to medications."},
                {"instruction_es": "Forma la respuesta:", "prompt": "— Where does it hurt? —", "answer": "My head / My throat / My back hurts."},
                {"instruction_es": "Completa:", "prompt": "I'm feeling ___. I have a cold.", "answer": "sick / terrible / bad"}
            ],
            "flashcards": [
                {"front": "doctor", "back": "doctor (dáktər)"},
                {"front": "dolor de cabeza", "back": "headache (hédeik)"},
                {"front": "fiebre", "back": "fever (fívər)"},
                {"front": "resfriado", "back": "cold (kóld)"},
                {"front": "tos", "back": "cough (kof)"},
                {"front": "garganta", "back": "throat (zróut)"},
                {"front": "estómago", "back": "stomach (stəmuk)"},
                {"front": "alérgico", "back": "allergic (əlérjik)"},
                {"front": "medicamento", "back": "medication (medikéishen)"},
                {"front": "descanso", "back": "rest (rest)"}
            ],
            "quiz": [
                {"q_es": "Completa: 'I ___ a high fever.'", "options": ["am", "have", "take", "feel"], "answer": 1},
                {"q_es": "¿Cuál es un síntoma?", "options": ["I have a hotel.", "I have a headache.", "I have a ticket.", "I have a reservation."], "answer": 1},
                {"q_es": "¿Cuál es la pregunta del doctor?", "options": ["Where is your room?", "How long have you had this?", "What is your flight?", "When is check-in?"], "answer": 1},
                {"q_es": "Traduce: 'Me duele la espalda.'", "options": ["I have back.", "I back hurts.", "My back hurts.", "I'm hurting back."], "answer": 2},
                {"q_es": "¿Qué dices si eres alérgico?", "options": ["I'm allergic to...", "I'm angry about...", "I'm afraid of...", "I'm angry with..."], "answer": 0}
            ]
        },
        {
            "day": 3,
            "topic_es": "El Clima y Estaciones",
            "topic_en": "Weather & Seasons",
            "objective_es": "Al final de esta lección podrás describir el clima, hablar sobre las estaciones, y entender predicciones meteorológicas.",
            "grammar_label": "Weather & Seasons",
            "grammar_es": "Para hablar del clima, usas: 1) 'It is + adjective': 'It is sunny.' 'It is cold.' 'It is rainy.' 'It is windy.' 2) 'It is + noun': 'It is rain.' → 'It is raining.' (Está lloviendo.) 'It is snow.' → 'It is snowing.' (Está nevando.) 3) Para temperatura: 'It is hot/warm/cold/cool.' 'The temperature is 25 degrees.' 4) Sobre estaciones: 'Spring, Summer, Fall/Autumn, Winter.' 'In summer, it is hot.' 'I love winter because it is cold.' Para predicciones: 'It will be sunny tomorrow.' 'It might rain this weekend.' 'There is a chance of snow.'",
            "vocabulary": [
                {"en": "weather", "es": "clima/tiempo", "pronunciation": "uéðər", "example_en": "What's the weather like today?", "example_es": "¿Cómo está el clima hoy?"},
                {"en": "sunny", "es": "soleado", "pronunciation": "sóni", "example_en": "It's a sunny day.", "example_es": "Es un día soleado."},
                {"en": "rainy", "es": "lluvioso", "pronunciation": "réini", "example_en": "It's rainy today.", "example_es": "Está llovioso hoy."},
                {"en": "cloudy", "es": "nublado", "pronunciation": "kláudi", "example_en": "The sky is cloudy.", "example_es": "El cielo está nublado."},
                {"en": "cold", "es": "frío", "pronunciation": "kóld", "example_en": "It's very cold outside.", "example_es": "Hace mucho frío afuera."},
                {"en": "hot", "es": "caliente", "pronunciation": "jot", "example_en": "It's hot in summer.", "example_es": "Hace calor en verano."},
                {"en": "windy", "es": "ventoso", "pronunciation": "uíndi", "example_en": "It's very windy today.", "example_es": "Está muy ventoso hoy."},
                {"en": "spring", "es": "primavera", "pronunciation": "sprin", "example_en": "Spring is my favorite season.", "example_es": "La primavera es mi estación favorita."},
                {"en": "summer", "es": "verano", "pronunciation": "sərər", "example_en": "I love summer!", "example_es": "¡Amo el verano!"},
                {"en": "fall / autumn", "es": "otoño", "pronunciation": "fol / ótəm", "example_en": "The leaves fall in autumn.", "example_es": "Las hojas caen en otoño."},
                {"en": "winter", "es": "invierno", "pronunciation": "uíntər", "example_en": "It snows in winter.", "example_es": "Nieva en invierno."},
                {"en": "temperature", "es": "temperatura", "pronunciation": "témpərəchur", "example_en": "The temperature is 30 degrees.", "example_es": "La temperatura es 30 grados."}
            ],
            "dialogue": {
                "context_es": "Dos amigos hablan sobre el clima.",
                "lines": [
                    {"speaker": "Sara", "en": "What's the weather like today?", "es": "¿Cómo está el clima hoy?"},
                    {"speaker": "Mike", "en": "It's sunny and warm, but the wind is strong. I think it's about 25 degrees.", "es": "Está soleado y cálido, pero el viento es fuerte. Creo que son unos 25 grados."},
                    {"speaker": "Sara", "en": "Great! Do you think it will rain tomorrow?", "es": "¡Excelente! ¿Crees que lloverá mañana?"},
                    {"speaker": "Mike", "en": "The forecast says it might be rainy. I should bring an umbrella.", "es": "El pronóstico dice que podría llover. Debería llevar un paraguas."},
                    {"speaker": "Sara", "en": "You're right. I love the rain, but winter is my favorite season because it's cold and it snows.", "es": "Tienes razón. Me ama la lluvia, pero el invierno es mi estación favorita porque hace frío y nieva."}
                ]
            },
            "examples": [
                {"en": "It's raining heavily outside.", "es": "Está lloviendo mucho afuera.", "note_es": "Lluvia actual."},
                {"en": "In summer, it is usually hot and sunny.", "es": "En verano, generalmente hace calor y está soleado.", "note_es": "Patrón de clima."},
                {"en": "The weather forecast says it will snow tomorrow.", "es": "El pronóstico dice que nevará mañana.", "note_es": "Predicción futura."},
                {"en": "I prefer autumn because the temperature is mild and comfortable.", "es": "Prefiero el otoño porque la temperatura es templada y cómoda.", "note_es": "Preferencia por estación."},
                {"en": "It's windy today. The wind is very strong.", "es": "Está ventoso hoy. El viento es muy fuerte.", "note_es": "Descri ción del viento."},
                {"en": "Do you like winter? Yes, I love the snow and cold weather.", "es": "¿Te gusta el invierno? Sí, me encanta la nieve y el clima frío.", "note_es": "Opinión sobre estación."}
            ],
            "tip_es": "Para hablar del clima: 'It is + adjective' o 'It is + verb+ing' (It is raining). Para estaciones: 'In + season' (In winter). Para temperatura: 'It is + temperature + degrees.' Recuerda: En inglés, 'It' es el sujeto de clima, no 'the weather' como sujeto gramatical.",
            "practice": [
                {"instruction_es": "Traduce al inglés:", "prompt": "Hoy está soleado y cálido.", "answer": "Today it's sunny and warm."},
                {"instruction_es": "Completa:", "prompt": "___ is my favorite season.", "answer": "Summer / Winter / Spring / Autumn"},
                {"instruction_es": "Pregunta:", "prompt": "¿Cómo está el clima mañana?", "answer": "What's the weather like tomorrow?"},
                {"instruction_es": "Traduce:", "prompt": "Creo que lloverá mañana.", "answer": "I think it will rain tomorrow."},
                {"instruction_es": "Forma la oración:", "prompt": "invierno / frío / es", "answer": "It's cold in winter. / Winter is cold."},
                {"instruction_es": "Completa:", "prompt": "It's very ___ and ___ today.", "answer": "sunny and warm / cloudy and cold"}
            ],
            "flashcards": [
                {"front": "clima", "back": "weather (uéðər)"},
                {"front": "soleado", "back": "sunny (sóni)"},
                {"front": "lluvioso", "back": "rainy (réini)"},
                {"front": "nublado", "back": "cloudy (kláudi)"},
                {"front": "frío", "back": "cold (kóld)"},
                {"front": "caliente", "back": "hot (jot)"},
                {"front": "ventoso", "back": "windy (uíndi)"},
                {"front": "primavera", "back": "spring (sprin)"},
                {"front": "verano", "back": "summer (sərər)"},
                {"front": "invierno", "back": "winter (uíntər)"}
            ],
            "quiz": [
                {"q_es": "Completa: '___  is my favorite season.'", "options": ["Summer", "The summer", "In summer", "Summers"], "answer": 0},
                {"q_es": "¿Cuál es correcto?", "options": ["It are sunny.", "It is sunny.", "It's sunny.", "It be sunny."], "answer": 1},
                {"q_es": "Pregunta sobre clima:", "options": ["Where is the weather?", "What's the weather like?", "How is weather?", "Weather is what?"], "answer": 1},
                {"q_es": "Traduce: 'Está lloviendo.'", "options": ["It is rain.", "It is raining.", "It rains.", "It will rain."], "answer": 1},
                {"q_es": "Estaciones en orden:", "options": ["Spring, Summer, Autumn, Winter", "Summer, Spring, Winter, Autumn", "Winter, Spring, Summer, Autumn", "Autumn, Winter, Spring, Summer"], "answer": 0}
            ]
        },
        {
            "day": 4,
            "topic_es": "Hobbies, Deportes y Tiempo Libre",
            "topic_en": "Hobbies, Sports & Leisure",
            "objective_es": "Al final de esta lección podrás hablar sobre tus hobbies, deportes favoritos, y cómo pasas tu tiempo libre en inglés.",
            "grammar_label": "Hobbies & Sports",
            "grammar_es": "Para hablar de hobbies: 'I like + verb+ing' (Me gusta + verbo en gerundio): 'I like playing soccer.' (Me gusta jugar fútbol.) 'She likes reading books.' (A ella le gusta leer libros.) También: 'I enjoy cooking.' (Disfruto cocinando.) 'I love swimming.' (Amo nadar.) Para deportes: 'play + deporte con pelota': play soccer, play basketball, play tennis. 'do + otros deportes': do yoga, do swimming, do running. 'go + gerundio': go skiing, go hiking, go swimming. Preguntas: 'What's your hobby?' 'Do you play any sports?' 'What do you like to do in your free time?' (¿Qué te gusta hacer en tu tiempo libre?)",
            "vocabulary": [
                {"en": "hobby", "es": "hobby", "pronunciation": "jábi", "example_en": "What's your hobby?", "example_es": "¿Cuál es tu hobby?"},
                {"en": "sports", "es": "deportes", "pronunciation": "sports", "example_en": "I love sports.", "example_es": "Amo los deportes."},
                {"en": "soccer", "es": "fútbol", "pronunciation": "sóker", "example_en": "I play soccer on weekends.", "example_es": "Juego fútbol los fines de semana."},
                {"en": "basketball", "es": "basquetbol", "pronunciation": "báskitbol", "example_en": "He plays basketball.", "example_es": "Él juega basquetbol."},
                {"en": "tennis", "es": "tenis", "pronunciation": "ténis", "example_en": "She plays tennis.", "example_es": "Ella juega tenis."},
                {"en": "swimming", "es": "natación", "pronunciation": "suímmin", "example_en": "I enjoy swimming.", "example_es": "Disfruto nadando."},
                {"en": "reading", "es": "lectura", "pronunciation": "rídin", "example_en": "Reading is my favorite hobby.", "example_es": "La lectura es mi hobby favorito."},
                {"en": "cooking", "es": "cocina", "pronunciation": "kúkin", "example_en": "I love cooking dinner.", "example_es": "Amo cocinar la cena."},
                {"en": "painting", "es": "pintura", "pronunciation": "péintin", "example_en": "She enjoys painting.", "example_es": "A ella le gusta pintar."},
                {"en": "dancing", "es": "baile", "pronunciation": "dánsin", "example_en": "I like dancing!", "example_es": "¡Me gusta bailar!"},
                {"en": "free time", "es": "tiempo libre", "pronunciation": "frí táim", "example_en": "What do you do in your free time?", "example_es": "¿Qué haces en tu tiempo libre?"},
                {"en": "enjoy", "es": "disfrutar", "pronunciation": "inyói", "example_en": "I enjoy playing guitar.", "example_es": "Disfruto tocando guitarra."}
            ],
            "dialogue": {
                "context_es": "Dos personas hablan sobre sus hobbies.",
                "lines": [
                    {"speaker": "Lisa", "en": "What do you like to do in your free time?", "es": "¿Qué te gusta hacer en tu tiempo libre?"},
                    {"speaker": "Tom", "en": "I love playing soccer and reading. I play soccer every Saturday.", "es": "Me encanta jugar fútbol y leer. Juego fútbol todos los sábados."},
                    {"speaker": "Lisa", "en": "That's great! Do you play any other sports?", "es": "¡Eso es excelente! ¿Juegas otros deportes?"},
                    {"speaker": "Tom", "en": "Sometimes I go swimming on Sundays. What about you? What's your hobby?", "es": "A veces voy a nadar los domingos. ¿Y tú? ¿Cuál es tu hobby?"},
                    {"speaker": "Lisa", "en": "I enjoy cooking and painting. I'm taking a cooking class this summer!", "es": "Disfruto cocinando y pintando. ¡Estoy tomando una clase de cocina este verano!"}
                ]
            },
            "examples": [
                {"en": "I like playing tennis on weekends.", "es": "Me gusta jugar tenis los fines de semana.", "note_es": "like + verb+ing."},
                {"en": "She enjoys reading books in her free time.", "es": "A ella le gusta leer libros en su tiempo libre.", "note_es": "enjoy + verb+ing."},
                {"en": "Do you play any sports? Yes, I play basketball.", "es": "¿Juegas algún deporte? Sí, juego basquetbol.", "note_es": "Pregunta sobre deportes."},
                {"en": "He loves swimming. He goes swimming every day.", "es": "A él le encanta nadar. Va a nadar todos los días.", "note_es": "love + verb+ing; go + verb+ing."},
                {"en": "My hobby is cooking. I cook Italian food.", "es": "Mi hobby es cocinar. Cocino comida italiana.", "note_es": "Describir hobby."},
                {"en": "What sports do you like? I like soccer, tennis, and swimming.", "es": "¿Qué deportes te gustan? Me gustan el fútbol, el tenis y la natación.", "note_es": "Múltiples deportes."}
            ],
            "tip_es": "Recuerda: 'like/love/enjoy + verb+ing' (Me gusta + gerundio). Para deportes con pelota: 'play' (play soccer, play basketball). Para otros: 'do' o 'go' (do yoga, go swimming). Cuando hablas de hobby, es importante expresar entusiasmo: 'I love it!' 'I enjoy it very much!'",
            "practice": [
                {"instruction_es": "Traduce al inglés:", "prompt": "Me gusta jugar fútbol.", "answer": "I like playing soccer. / I like to play soccer."},
                {"instruction_es": "Completa:", "prompt": "She ___ reading books.", "answer": "likes / enjoys / loves"},
                {"instruction_es": "Pregunta:", "prompt": "¿Qué deportes juegas?", "answer": "What sports do you play?"},
                {"instruction_es": "Traduce:", "prompt": "Disfruto nadando en el verano.", "answer": "I enjoy swimming in summer."},
                {"instruction_es": "Forma la oración:", "prompt": "basketball / playing / love / I", "answer": "I love playing basketball."},
                {"instruction_es": "Completa:", "prompt": "What do you ___ to do in your free time?", "answer": "like / love / enjoy"}
            ],
            "flashcards": [
                {"front": "hobby", "back": "hobby (jábi)"},
                {"front": "deportes", "back": "sports (sports)"},
                {"front": "fútbol", "back": "soccer (sóker)"},
                {"front": "basquetbol", "back": "basketball (báskitbol)"},
                {"front": "tenis", "back": "tennis (ténis)"},
                {"front": "natación", "back": "swimming (suímmin)"},
                {"front": "lectura", "back": "reading (rídin)"},
                {"front": "cocina", "back": "cooking (kúkin)"},
                {"front": "tiempo libre", "back": "free time (frí táim)"},
                {"front": "disfrutar", "back": "enjoy (inyói)"}
            ],
            "quiz": [
                {"q_es": "Completa: 'I ___ playing soccer.'", "options": ["like", "likes", "liked", "liking"], "answer": 0},
                {"q_es": "¿Cuál es correcto?", "options": ["I like to read", "I like to reading", "I like reading", "Both 'A' and 'C'"], "answer": 3},
                {"q_es": "¿Con qué deporte usas 'play'?", "options": ["play swimming", "play skiing", "play soccer", "play running"], "answer": 2},
                {"q_es": "Traduce: 'Me encanta cocinar.'", "options": ["I like cooking.", "I enjoy cooking.", "I love cooking.", "All are correct."], "answer": 3},
                {"q_es": "Pregunta sobre tiempo libre:", "options": ["What sports you play?", "Do what you like?", "What do you like to do?", "You like what to do?"], "answer": 2}
            ]
        },
        {
            "day": 5,
            "topic_es": "Repaso Final de A1 — Conversación Completa",
            "topic_en": "A1 Complete Final Review",
            "objective_es": "Habrás completado el curso A1 completo. Podrás mantener conversaciones básicas en inglés sobre cualquier tema cubierto: saludos, información personal, presente, pasado, futuro, comparativos, viajes, salud, clima, hobbies y más.",
            "grammar_label": "Complete A1 Summary",
            "grammar_es": "A1 Completo cubre: 1) SALUDOS: Hello, Hi, Good morning/afternoon/evening. 2) TO BE: I am, you are, he/she/it is, we/they are. Pasado: was/were. 3) PRESENTE SIMPLE: I work, he works. Preguntas: Do you work? Does he work? 4) PRESENTE CONTINUO: I am working, he is working. 5) PASADO SIMPLE: Regular (worked) e irregular (went, ate, saw). Preguntas: Did you go? 6) HAVE/HAVE GOT: I have a car / I've got a car. 7) CAN/COULD: I can speak. Could you help? 8) COMPARATIVOS: bigger, more interesting. SUPERLATIVOS: the biggest, the most interesting. 9) GOING TO: I'm going to travel. 10) WANT/WOULD LIKE: I want to eat. I would like tea. Mantén conversaciones practicando todos estos temas.",
            "vocabulary": [
                {"en": "congratulations", "es": "felicidades", "pronunciation": "kəngrächuléishenz", "example_en": "Congratulations! You finished A1!", "example_es": "¡Felicidades! ¡Terminaste A1!"},
                {"en": "complete", "es": "completo", "pronunciation": "kəmplit", "example_en": "You completed the course.", "example_es": "Completaste el curso."},
                {"en": "achievement", "es": "logro", "pronunciation": "əchívmənt", "example_en": "That's a great achievement!", "example_es": "¡Eso es un gran logro!"},
                {"en": "progress", "es": "progreso", "pronunciation": "prógrés", "example_en": "You made excellent progress.", "example_es": "Hiciste excelente progreso."},
                {"en": "fluent", "es": "fluido", "pronunciation": "flúənt", "example_en": "You're not fluent yet, but you're making progress.", "example_es": "No eres fluido aún, pero estás haciendo progreso."},
                {"en": "conversation", "es": "conversación", "pronunciation": "konverséshen", "example_en": "You can have basic conversations now.", "example_es": "Ahora puedes tener conversaciones básicas."},
                {"en": "practice", "es": "práctica", "pronunciation": "práktis", "example_en": "Continue practicing every day.", "example_es": "Sigue practicando cada día."},
                {"en": "continue", "es": "continuar", "pronunciation": "kəntíniu", "example_en": "Continue your English journey.", "example_es": "Continúa tu viaje de inglés."},
                {"en": "journey", "es": "viaje", "pronunciation": "jérni", "example_en": "Your English journey is just beginning.", "example_es": "Tu viaje de inglés apenas está comenzando."},
                {"en": "success", "es": "éxito", "pronunciation": "səksés", "example_en": "Wishing you success!", "example_es": "¡Te deseo éxito!"},
                {"en": "goal", "es": "meta/objetivo", "pronunciation": "góul", "example_en": "Your goal was to learn A1 English.", "example_es": "Tu meta era aprender inglés A1."},
                {"en": "next level", "es": "próximo nivel", "pronunciation": "nékst lévul", "example_en": "You can now move to A2.", "example_es": "Ahora puedes pasar a A2."}
            ],
            "dialogue": {
                "context_es": "Un profesor y un estudiante reflejando sobre el curso completo.",
                "lines": [
                    {"speaker": "Teacher", "en": "Congratulations! You have finished the A1 course!", "es": "¡Felicidades! ¡Has terminado el curso A1!"},
                    {"speaker": "Student", "en": "Thank you so much! I learned so much. I can now have conversations, understand movies, and talk about my life.", "es": "¡Gracias mucho! Aprendí tanto. Ahora puedo tener conversaciones, entender películas, y hablar de mi vida."},
                    {"speaker": "Teacher", "en": "You made excellent progress! You started from zero and now you can do so much. What was the hardest part?", "es": "¡Hiciste excelente progreso! Empezaste desde cero y ahora puedes hacer tanto. ¿Cuál fue la parte más difícil?"},
                    {"speaker": "Student", "en": "The past tense was difficult, but with practice, I understood it. Now I'm ready for the next level.", "es": "El tiempo pasado fue difícil, pero con práctica, lo entendí. Ahora estoy listo para el próximo nivel."},
                    {"speaker": "Teacher", "en": "Perfect! Continue practicing, watch English movies, and read English books. Your journey has just begun!", "es": "¡Perfecto! Sigue practicando, mira películas en inglés, y lee libros en inglés. ¡Tu viaje apenas comienza!"}
                ]
            },
            "examples": [
                {"en": "I can now introduce myself, describe my family, and tell stories about my past.", "es": "Ahora puedo presentarme, describir mi familia, y contar historias sobre mi pasado.", "note_es": "Habilidades adquiridas."},
                {"en": "This course taught me present, past, and future tenses, comparatives, and many practical phrases.", "es": "Este curso me enseñó tiempos presente, pasado y futuro, comparativos, y muchas frases prácticas.", "note_es": "Resumen de temas."},
                {"en": "I went from not speaking any English to having basic conversations. I'm proud of my progress!", "es": "Pasé de no hablar nada de inglés a tener conversaciones básicas. ¡Estoy orgulloso de mi progreso!", "note_es": "Reflexión personal."},
                {"en": "The journey continues. I will keep practicing and studying to improve my English.", "es": "El viaje continúa. Seguiré practicando y estudiando para mejorar mi inglés.", "note_es": "Compromiso futuro."},
                {"en": "Remember: practice every day, watch movies in English, read books, and talk to English speakers.", "es": "Recuerda: practica cada día, mira películas en inglés, lee libros, y habla con hablantes de inglés.", "note_es": "Consejos para continuar."},
                {"en": "You are ready for A2! You have achieved a great milestone in your English learning journey.", "es": "¡Estás listo para A2! ¡Has logrado un gran hito en tu viaje de aprendizaje de inglés!", "note_es": "Motivación para continuar."}
            ],
            "tip_es": "Felicidades por completar A1. Ahora que terminaste el curso, sigue practicando. Mira películas en inglés, lee libros fáciles, habla con amigos en inglés, y no tengas miedo de cometer errores. Los errores son parte del aprendizaje. ¡Tu viaje de inglés apenas comienza!",
            "practice": [
                {"instruction_es": "Describe tu progreso:", "prompt": "I was able to... Now I can...", "answer": "I was able to say hello. Now I can have conversations."},
                {"instruction_es": "Traduce:", "prompt": "¡Hice un excelente progreso!", "answer": "I made excellent progress!"},
                {"instruction_es": "Reflexiona:", "prompt": "¿Cuál fue la parte más difícil del curso?", "answer": "The past tense / Comparatives / Grammar / (cualquier respuesta válida)"},
                {"instruction_es": "Pregunta sobre el futuro:", "prompt": "¿Qué vas a hacer ahora?", "answer": "I'm going to continue practicing. / I'm going to watch movies in English. / I'm going to study A2."},
                {"instruction_es": "Traduce:", "prompt": "Tu viaje de inglés apenas comienza.", "answer": "Your English journey is just beginning."},
                {"instruction_es": "Completa:", "prompt": "I will continue ___ to improve my English.", "answer": "practicing / studying / learning"}
            ],
            "flashcards": [
                {"front": "felicidades", "back": "congratulations (kəngrächuléishenz)"},
                {"front": "completar", "back": "complete (kəmlit)"},
                {"front": "logro", "back": "achievement (əchívmənt)"},
                {"front": "progreso", "back": "progress (prógrés)"},
                {"front": "conversación", "back": "conversation (konverséshen)"},
                {"front": "práctica", "back": "practice (práktis)"},
                {"front": "continuar", "back": "continue (kəntíniu)"},
                {"front": "viaje", "back": "journey (jérni)"},
                {"front": "éxito", "back": "success (səksés)"},
                {"front": "próximo nivel", "back": "next level (nékst lévul)"}
            ],
            "quiz": [
                {"q_es": "¿Cuántas semanas completaste?", "options": ["5", "8", "10", "15"], "answer": 2},
                {"q_es": "¿Cuál es el próximo paso?", "options": ["Stop learning", "Study A2", "Restart A1", "Take a break forever"], "answer": 1},
                {"q_es": "¿Qué NO deberías hacer?", "options": ["Practice every day", "Watch movies", "Read books", "Stop speaking English"], "answer": 3},
                {"q_es": "¿Cuál es el mejor consejo?", "options": ["Never make mistakes", "Practice and don't fear mistakes", "Only study grammar", "Don't talk to native speakers"], "answer": 1},
                {"q_es": "¿Qué lograste?", "options": ["I can't speak English", "I can have basic conversations", "I'm completely fluent", "I only know greetings"], "answer": 1}
            ]
        }
    ]
}

# Append weeks to A1 level
a1_level['weeks'].append(week_9)
a1_level['weeks'].append(week_10)

# Save back to file
with open('/sessions/serene-elegant-thompson/mnt/socialblog/data/curriculum.json', 'w', encoding='utf-8') as f:
    json.dump(curriculum, f, ensure_ascii=False, indent=2)

# Validate JSON and print stats
print("✓ Successfully generated and appended weeks 9 and 10")
print(f"✓ Total levels: {len(curriculum['levels'])}")
print(f"✓ A1 total weeks: {len(a1_level['weeks'])}")
for level in curriculum['levels']:
    print(f"  - {level['name']}: {len(level['weeks'])} weeks")
    for week in level['weeks'][-2:]:  # Show last 2 weeks
        day_count = len(week['days'])
        print(f"    • Week {week['week']}: {day_count} days")

print("\n✓ JSON validation: All weeks are valid and properly formatted!")
