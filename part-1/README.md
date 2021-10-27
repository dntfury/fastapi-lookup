## Info of command

    The command uvicorn main:app refers to:

    main: the file main.py (the Python "module").
    app: the object created inside of main.py with the line app = FastAPI().
    --reload: make the server restart after code changes.

- FastAPI is a Python class
- app variable will be an "instance" of the class FastAPI

## Operation or methods
in OpenAPI, each of the HTTP methods is called an "operation".

    POST: to create data.
    GET: to read data.
    PUT: to update data.
    DELETE: to delete data.

    The @app.get("/") tells FastAPI that the function right below is in charge of handling requests that go to:
    the path (/) and using a *get* operation
    
    You can also use the other operations:

    @app.post()
    @app.put()
    @app.delete()
    
    @app.get("/") is decorator


## Return value
- You can return a dict, list, singular values as str, int, etc.



## Type hint eg:
    This is the "type hints":

    @app.get("/message/{message}")
    async def root(message:str):
            return {"message": message+!!!!}

