import wordle

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

database = dict()


@app.get('/play')
async def play(token: str, test: str = None, mark: str = None):
    if token not in database or test is None or mark is None:
        database[token] = wordle.read_word_list()
    else:
        database[token] = list(filter(lambda word: wordle.is_suitable(test, mark, word), database[token]))

    if len(database[token]) > 1:
        return {'status': 'ask', 'word': database[token][0], 'cnt': len(database[token])}
    elif len(database[token]) == 1:
        return {'status': 'answer', 'word': database[token][0]}
    else:
        return {'status': 'fail'}
