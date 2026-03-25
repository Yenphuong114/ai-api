from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    data: str

@app.post("/predict")
def predict(input: InputData):
    text = input.data.lower()

    if "good" in text or "happy" in text:
        result = "positive"
    elif "bad" in text or "sad" in text:
        result = "negative"
    else:
        result = "neutral"

    return {"prediction": result}