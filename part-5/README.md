## Multiple body parameters

<hr>

FastAPI will notice that there are more than one body parameters in the function



<hr>

![code and output](code-output.png)

<hr>

## Singular values in body

    importance: int = Body(...)
    
    and in body define it as 
    {
    ....
    ...
    
        "importance": 5
    }

<hr>

## Multiple body params and query 

    @app.put("/items/{item_id}")
    async def update_item(
        *,
        item_id: int,
        item: Item,
        user: User,
        importance: int = Body(..., gt=0),
        q: Optional[str] = None
    ):
        results = {"item_id": item_id, "item": item, "user": user,  "importance": importance}
        if q:
            results.update({"q": q})
        return results





## Embed a single body parameter

    In this case FastAPI will expect a body like:


    {
        "item": {
            "name": "Foo",
            "description": "The pretender",
            "price": 42.0,
            "tax": 3.2
        }
    }
    instead of:


    {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
