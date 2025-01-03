from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """
        This is the first endpoint in the tutorial. 
        Hello world !!!!
    """
    return {"message": "Hello World !!!!!"}