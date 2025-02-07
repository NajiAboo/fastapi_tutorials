from  fastapi import FastAPI

app = FastAPI()


fake_item = [{
    "item_name": "foo"
},
{
    "item_name": "Bar"
},
{
    "item_name": "Baz"
}

]


@app.get("/itemes/")
async def read_item(skip: int, limit:int ):
    return fake_item[skip: limit]

@app.get("/itesm/{item_id}")
async def read_item(items_id: str, q: str | None=None):
    if q:
        return {"item_id": items_id, "q": q}
    return {"item_id": items_id}