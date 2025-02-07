from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class ModelName(str, Enum):
    alexnet ="alexnet"
    resnet="restnet"


@app.get("/items/items")
async def get_all_items():
    return {"item name": "all item"}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item Name": "item 1"}

@app.get("/models/{model_name}")
async def get_models(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return "This is alexnet"
    elif model_name is ModelName.resnet:
        return "This is from reset"
    
@app.get("/filepath/{file_path:path}")
async def read_file(file_path):
    return {"result": "reading is success"}

