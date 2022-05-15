from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def roof():
    return {"message": "Hello World"}
