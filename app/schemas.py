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

class TemperatureSensitivity(str, Enum):
    NONE = "none"
    AMBIENT = "ambient"  # Room temperature items
    CHILLED = "chilled"  # Items that need to be kept cool (4-8°C)
    FROZEN = "frozen"    # Items that need to be kept frozen (-18°C)
    HOT = "hot"          # Items that need to be kept hot (>60°C)

class Location(BaseModel):
    latitude: float
    longitude: float
    address: str

class DeliveryItem(BaseModel):
    id: str
    name: str
    quantity: int
    price: float
    temperature_sensitivity: TemperatureSensitivity = TemperatureSensitivity.NONE
    max_safe_time_minutes: Optional[int] = None
    special_handling_instructions: Optional[str] = None

class DeliveryWindow(BaseModel):
    start_time: datetime
    end_time: datetime
    priority: int = 1  # 1-5, 5 being highest priority
    late_penalty: Optional[float] = None  # Penalty amount for late delivery

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
    delivery_window: DeliveryWindow
    actualTime: Optional[datetime] = None
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
    delivery_priority: str
    delivery_deadline: datetime

class OrderRequest(BaseModel):
    orders: List[Order]

class RouteResponse(BaseModel):
    optimized_order_ids: List[str]
