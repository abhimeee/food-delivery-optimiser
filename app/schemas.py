from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from enum import Enum

class DeliveryStatus(str, Enum):
    PENDING = "pending"
    PICKED_UP = "picked_up"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class Location(BaseModel):
    latitude: float
    longitude: float
    address: str

class DeliveryItem(BaseModel):
    id: str
    name: str
    quantity: int
    price: float

class Delivery(BaseModel):
    id: str
    orderId: str
    customerName: str
    customerAddress: str
    customerPhone: str
    items: List[DeliveryItem]
    status: DeliveryStatus
    pickupLocation: Location
    deliveryLocation: Location
    estimatedTime: str
    actualTime: Optional[str] = None
    notes: Optional[str] = None

class Driver(BaseModel):
    id: str
    name: str
    phone: str
    email: str
    vehicleType: str
    vehicleNumber: str
    rating: float
    totalDeliveries: int

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
