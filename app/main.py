from fastapi import FastAPI, HTTPException
from app.schemas import OrderRequest, RouteResponse, Delivery, Driver, DeliveryStatusUpdate, DeliveryStatus
from app.optimizer import optimize_route
from .mock_data import MOCK_DELIVERIES, MOCK_DELIVERIES_BY_ID, MOCK_DRIVERS

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

@app.get("/deliveries/{delivery_id}", response_model=Delivery)
async def get_delivery_details(delivery_id: str):
    if delivery_id not in MOCK_DELIVERIES_BY_ID:
        raise HTTPException(status_code=404, detail="Delivery not found")
    
    return MOCK_DELIVERIES_BY_ID[delivery_id]

@app.get("/drivers/{driver_id}", response_model=Driver)
async def get_driver_profile(driver_id: str):
    if driver_id not in MOCK_DRIVERS:
        raise HTTPException(status_code=404, detail="Driver not found")
    
    return MOCK_DRIVERS[driver_id]

@app.patch("/deliveries/{delivery_id}/status", response_model=Delivery)
async def update_delivery_status(delivery_id: str, update: DeliveryStatusUpdate):
    if delivery_id not in MOCK_DELIVERIES_BY_ID:
        raise HTTPException(status_code=404, detail="Delivery not found")
    
    delivery = MOCK_DELIVERIES_BY_ID[delivery_id]
    delivery.status = update.status
    
    # Update the delivery in both dictionaries
    MOCK_DELIVERIES_BY_ID[delivery_id] = delivery
    
    # Find and update the delivery in the driver's list
    for driver_id, deliveries in MOCK_DELIVERIES.items():
        for i, d in enumerate(deliveries):
            if d.id == delivery_id:
                MOCK_DELIVERIES[driver_id][i] = delivery
                break
    
    return delivery
