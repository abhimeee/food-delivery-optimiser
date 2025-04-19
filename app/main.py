from fastapi import FastAPI
from app.schemas import OrderRequest, RouteResponse
from app.optimizer import optimize_route

app = FastAPI()

@app.get("/test")
def root():
    return {"message": "Food Delivery Optimization API is running"}

@app.post("/optimize", response_model=RouteResponse)
def optimize(data: OrderRequest):
    return optimize_route(data)
