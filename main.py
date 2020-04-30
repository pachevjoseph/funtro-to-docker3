from fastapi import FastAPI
from random import randrange

app = FastAPI()


answer = randrange(1, 15)

@app.get("/api/health")
def status():
    """
    Health Check for the application
    """
    return {"status": "Ok"}


@app.get("/api/guess/{guess}")
def is_guess_right(guess: int):
    """
    The main application endpoint that checks if your guess is correct
    and returns appropriate responess

    :guess: The integer passed in to be checked against
    :return: A JSON representation of whether the guess was right, too high or too low
    """

    if guess < answer:
        return {"response": "low"}
    if guess > answer:
        return {"response": "high"}
    else:
        return {"response": "correct"}
