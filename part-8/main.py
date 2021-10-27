from typing import FrozenSet
from fastapi import FastAPI, Form , File , UploadFile
from fastapi.responses import FileResponse


some_file_path = "file.jpg"

app=FastAPI()

@app.post("/login/")
async def login(username : str = Form(...), password : str = Form(...)):
    return {"username":username}

@app.post("/files/")
async def create_file(file : bytes = File(...)):
    return {"File size" : len(file) }


@app.post("/uploadfile/" , response_class=FileResponse)
async def upload_file(file : UploadFile = File(...)):
    return  FileResponse(some_file_path) 

