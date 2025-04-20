from datetime import datetime, timedelta
from .schemas import Delivery, DeliveryItem, Location, Driver, DeliveryStatus, TemperatureSensitivity, DeliveryWindow

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

# Common pickup location (Paradise Restaurant)
PARADISE_LOCATION = Location(
    latitude=17.4332,
    longitude=78.4070,
    address="Paradise Restaurant, Secunderabad, Hyderabad - 500003"
)

# Current time for reference
current_time = datetime.now()

# Create delivery objects for driver1
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
            price=450.00,
            temperature_sensitivity=TemperatureSensitivity.HOT,
            max_safe_time_minutes=45,
            special_handling_instructions="Keep in thermal bag"
        ),
        DeliveryItem(
            id="item2",
            name="Mirchi Ka Salan",
            quantity=1,
            price=180.00,
            temperature_sensitivity=TemperatureSensitivity.HOT,
            max_safe_time_minutes=45
        )
    ],
    status=DeliveryStatus.PENDING,
    pickupLocation=PARADISE_LOCATION,
    deliveryLocation=Location(
        latitude=17.4330,
        longitude=78.4072,
        address="Flat 302, Green Valley Apartments, Jubilee Hills, Hyderabad - 500033"
    ),
    delivery_window=DeliveryWindow(
        start_time=current_time + timedelta(minutes=10),
        end_time=current_time + timedelta(minutes=40),
        priority=3,
        late_penalty=100.00
    )
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
            price=320.00,
            temperature_sensitivity=TemperatureSensitivity.HOT,
            max_safe_time_minutes=30
        ),
        DeliveryItem(
            id="item4",
            name="Butter Naan",
            quantity=4,
            price=160.00,
            temperature_sensitivity=TemperatureSensitivity.HOT,
            max_safe_time_minutes=30
        )
    ],
    status=DeliveryStatus.PENDING,
    pickupLocation=PARADISE_LOCATION,
    deliveryLocation=Location(
        latitude=17.4500,
        longitude=78.3800,
        address="Flat 405, Sri Sai Residency, Khajaguda, Hyderabad - 500008"
    ),
    delivery_window=DeliveryWindow(
        start_time=current_time + timedelta(minutes=20),
        end_time=current_time + timedelta(minutes=50),
        priority=2
    )
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
            price=250.00,
            temperature_sensitivity=TemperatureSensitivity.HOT,
            max_safe_time_minutes=40
        ),
        DeliveryItem(
            id="item6",
            name="Gulab Jamun",
            quantity=2,
            price=80.00,
            temperature_sensitivity=TemperatureSensitivity.AMBIENT,
            max_safe_time_minutes=60
        )
    ],
    status=DeliveryStatus.PENDING,
    pickupLocation=PARADISE_LOCATION,
    deliveryLocation=Location(
        latitude=17.4430,
        longitude=78.3772,
        address="Flat 501, Cyber Towers, HITEC City, Hyderabad - 500081"
    ),
    delivery_window=DeliveryWindow(
        start_time=current_time + timedelta(minutes=30),
        end_time=current_time + timedelta(minutes=70),
        priority=4,
        late_penalty=150.00
    )
)

delivery4 = Delivery(
    id="delivery4",
    orderId="order4",
    customerName="Priya Sharma",
    customerAddress="House No. 12, Banjara Hills, Hyderabad - 500034",
    customerPhone="+919876543215",
    items=[
        DeliveryItem(
            id="item7",
            name="Ice Cream (Vanilla)",
            quantity=2,
            price=120.00,
            temperature_sensitivity=TemperatureSensitivity.FROZEN,
            max_safe_time_minutes=25,
            special_handling_instructions="Keep in insulated bag with ice packs"
        )
    ],
    status=DeliveryStatus.PENDING,
    pickupLocation=PARADISE_LOCATION,
    deliveryLocation=Location(
        latitude=17.4230,
        longitude=78.4472,
        address="House No. 12, Banjara Hills, Hyderabad - 500034"
    ),
    delivery_window=DeliveryWindow(
        start_time=current_time + timedelta(minutes=15),
        end_time=current_time + timedelta(minutes=35),
        priority=5,
        late_penalty=200.00
    )
)

delivery5 = Delivery(
    id="delivery5",
    orderId="order5",
    customerName="Rajesh Kumar",
    customerAddress="Flat 201, Aparna Towers, Gachibowli, Hyderabad - 500032",
    customerPhone="+919876543216",
    items=[
        DeliveryItem(
            id="item8",
            name="Hyderabadi Biryani",
            quantity=1,
            price=450.00,
            temperature_sensitivity=TemperatureSensitivity.HOT,
            max_safe_time_minutes=45
        ),
        DeliveryItem(
            id="item9",
            name="Ice Cream (Chocolate)",
            quantity=1,
            price=60.00,
            temperature_sensitivity=TemperatureSensitivity.FROZEN,
            max_safe_time_minutes=25,
            special_handling_instructions="Keep in insulated bag with ice packs"
        )
    ],
    status=DeliveryStatus.PENDING,
    pickupLocation=PARADISE_LOCATION,
    deliveryLocation=Location(
        latitude=17.4400,
        longitude=78.3500,
        address="Flat 201, Aparna Towers, Gachibowli, Hyderabad - 500032"
    ),
    delivery_window=DeliveryWindow(
        start_time=current_time + timedelta(minutes=20),
        end_time=current_time + timedelta(minutes=40),
        priority=5,
        late_penalty=200.00
    )
)

# Mock deliveries data by driver
MOCK_DELIVERIES = {
    "driver1": [delivery1, delivery2, delivery3, delivery4, delivery5],
    "driver2": []
}

# Mock deliveries data by ID for easy lookup
MOCK_DELIVERIES_BY_ID = {
    delivery.id: delivery for delivery in [delivery1, delivery2, delivery3, delivery4, delivery5]
} 