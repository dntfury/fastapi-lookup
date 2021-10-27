from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/message/{message}")
async def root(message:str):
    return {"message": message+"!!!!"}
