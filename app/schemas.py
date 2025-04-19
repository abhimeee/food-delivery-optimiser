from pydantic import BaseModel
from typing import List
from datetime import datetime

class Order(BaseModel):
    order_id: str
    order_time: datetime
    restaurant_id: str
    customer_id: str
    customer_lat: float
    customer_long: float
    product_type: str
    delivery_priority: str  # make it enum maybe later
    delivery_deadline: datetime

class OrderRequest(BaseModel):
    orders: List[Order]

class RouteResponse(BaseModel):
    optimized_order_ids: List[str]
