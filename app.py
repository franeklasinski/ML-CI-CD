import os
from fastapi import FastAPI, HTTPException, Request, Query
from pydantic import BaseModel
import numpy as np
from sklearn.linear_model import LinearRegression

app = FastAPI()

# Pobieranie klucza API ze zmiennej środowiskowej
API_KEY = os.getenv("API_KEY", "12345")  # domyślny tylko do lokalnych testów

# Dane treningowe i model
X_train = np.array([[1], [2], [3], [4], [5]])
y_train = np.array([2, 4, 6, 8, 10])
model = LinearRegression()
model.fit(X_train, y_train)

# Model danych wejściowych
class InputData(BaseModel):
    feature: float

# Endpoint predykcji z autoryzacją przez query param
@app.post("/predict")
async def predict(request: Request, api_key: str = Query(None, alias="API_KEY")):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Nieautoryzowany dostęp: zły klucz API")

    try:
        data = await request.json()
        if 'feature' not in data:
            raise HTTPException(status_code=400, detail="Brak wymaganej wartosci 'feature'")
        x_value = data['feature']
        prediction = model.predict([[x_value]])
        return {"status": "success", "message": "Dziala poprawnie", "prediction": prediction.tolist()}
    except Exception as e:
        return {"status": "error", "message": "Zla wartosc", "details": str(e)}

# Endpoint z informacjami o modelu
@app.get("/info")
async def info():
    model_info = {
        "model_type": str(type(model)),
        "num_features": model.coef_.shape[0],
        "intercept": model.intercept_,
        "coefficients": model.coef_.tolist(),
    }
    return {"status": "success", "model_info": model_info}

# Endpoint zdrowia
@app.get("/health")
async def health():
    return {"status": "jest online"}

# (opcjonalnie) do testów środowiskowych
@app.get("/show-key")
async def show_key():
    return {"API_KEY": API_KEY}
