from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def recommendation(age: int):
    if age < 18:
        return {"recommendation": "You are a minor. We recommend you to watch cartoons."}
    elif 18 <= age < 30:
        return {"recommendation": "You are a young adult. We recommend you to watch action movies."}
    elif 30 <= age < 50:
        return {"recommendation": "You are an adult. We recommend you to watch drama movies."}
    else:
        return {"recommendation": "You are a senior. We recommend you to watch classic movies."}
