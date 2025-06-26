from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import DemandForecastModel
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)

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