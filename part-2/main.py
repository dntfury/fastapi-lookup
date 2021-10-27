from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/files/{file_path:path}")
async def read_file(file_path:str):
    return {"path":file_path}


@app.get("/item/")
async def get_item(a:int=0 , b:int=10):
    return{"sum":a+b}

