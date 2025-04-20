from datetime import datetime, timedelta
from .schemas import Delivery, DeliveryItem, Location, Driver, DeliveryStatus

# Mock drivers data
MOCK_DRIVERS = {
    "driver1": Driver(
        id="driver1",
        name="Rahul Kumar",
        phone="+919876543210",
        email="rahul@example.com",
        vehicleType="bike",
        vehicleNumber="TS09AB1234",
        rating=4.8,
        totalDeliveries=150
    ),
    "driver2": Driver(
        id="driver2",
        name="Priya Sharma",
        phone="+919876543211",
        email="priya@example.com",
        vehicleType="scooter",
        vehicleNumber="TS09CD5678",
        rating=4.9,
        totalDeliveries=200
    )
}

# Create individual delivery objects
delivery1 = Delivery(
    id="delivery1",
    orderId="order1",
    customerName="Amit Patel",
    customerAddress="Flat 302, Green Valley Apartments, Jubilee Hills, Hyderabad - 500033",
    customerPhone="+919876543212",
    items=[
        DeliveryItem(
            id="item1",
            name="Hyderabadi Biryani",
            quantity=2,
            price=450.00
        ),
        DeliveryItem(
            id="item2",
            name="Mirchi Ka Salan",
            quantity=1,
            price=180.00
        )
    ],
    status=DeliveryStatus.IN_TRANSIT,
    pickupLocation=Location(
        latitude=17.4332,
        longitude=78.4070,
        address="Paradise Restaurant, Secunderabad, Hyderabad - 500003"
    ),
    deliveryLocation=Location(
        latitude=17.4330,
        longitude=78.4072,
        address="Flat 302, Green Valley Apartments, Jubilee Hills, Hyderabad - 500033"
    ),
    estimatedTime=(datetime.now() + timedelta(minutes=15)).isoformat(),
    notes="Please call before delivery"
)

delivery2 = Delivery(
    id="delivery2",
    orderId="order2",
    customerName="Sneha Reddy",
    customerAddress="Flat 405, Sri Sai Residency, Khajaguda, Hyderabad - 500008",
    customerPhone="+919876543213",
    items=[
        DeliveryItem(
            id="item3",
            name="Chicken 65",
            quantity=1,
            price=320.00
        ),
        DeliveryItem(
            id="item4",
            name="Butter Naan",
            quantity=4,
            price=160.00
        )
    ],
    status=DeliveryStatus.PENDING,
    pickupLocation=Location(
        latitude=17.4232,
        longitude=78.4470,
        address="Bawarchi Restaurant, RTC X Roads, Hyderabad - 500020"
    ),
    deliveryLocation=Location(
        latitude=17.4500,
        longitude=78.3800,
        address="Flat 405, Sri Sai Residency, Khajaguda, Hyderabad - 500008"
    ),
    estimatedTime=(datetime.now() + timedelta(minutes=30)).isoformat()
)

delivery3 = Delivery(
    id="delivery3",
    orderId="order3",
    customerName="Vikram Singh",
    customerAddress="Flat 501, Cyber Towers, HITEC City, Hyderabad - 500081",
    customerPhone="+919876543214",
    items=[
        DeliveryItem(
            id="item5",
            name="Veg Thali",
            quantity=1,
            price=250.00
        ),
        DeliveryItem(
            id="item6",
            name="Gulab Jamun",
            quantity=2,
            price=80.00
        )
    ],
    status=DeliveryStatus.PICKED_UP,
    pickupLocation=Location(
        latitude=17.4432,
        longitude=78.3770,
        address="Chutneys Restaurant, Madhapur, Hyderabad - 500081"
    ),
    deliveryLocation=Location(
        latitude=17.4430,
        longitude=78.3772,
        address="Flat 501, Cyber Towers, HITEC City, Hyderabad - 500081"
    ),
    estimatedTime=(datetime.now() + timedelta(minutes=20)).isoformat()
)

# Mock deliveries data by driver
MOCK_DELIVERIES = {
    "driver1": [delivery1, delivery2],
    "driver2": [delivery3]
}

# Mock deliveries data by ID for easy lookup
MOCK_DELIVERIES_BY_ID = {
    delivery.id: delivery for delivery in [delivery1, delivery2, delivery3]
} 