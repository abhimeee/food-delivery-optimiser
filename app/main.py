from fastapi import FastAPI, HTTPException
from app.schemas import OrderRequest, RouteResponse, Delivery
from app.optimizer import optimize_route
from .mock_data import MOCK_DELIVERIES

app = FastAPI()

@app.get("/test")
def root():
    return {"message": "Food Delivery Optimization API is running"}

@app.post("/optimize", response_model=RouteResponse)
def optimize(data: OrderRequest):
    return optimize_route(data)

@app.get("/deliveries/active/{driver_id}", response_model=list[Delivery])
async def get_active_deliveries(driver_id: str):
    if driver_id not in MOCK_DELIVERIES:
        raise HTTPException(status_code=404, detail="Driver not found")
    
    return MOCK_DELIVERIES[driver_id]
