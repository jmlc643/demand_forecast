from fastapi import FastAPI
from pydantic import BaseModel
from model import DemandForecastModel
import uvicorn

app = FastAPI()
model = DemandForecastModel()

class PredictionInput(BaseModel):
    UnitPrice: float
    Discount: float
    ShippingCost: float
    Category: str
    PaymentMethod: str
    SalesChannel: str
    InvoiceDate: str

@app.post("/predict")
async def predict(input_data: PredictionInput):
    """Endpoint para realizar predicciones"""
    return model.predict(input_data.dict())

@app.get("/")
async def root():
    """Endpoint de bienvenida"""
    return {"message": "Welcome to the Demand Forecasting API!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)