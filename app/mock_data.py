from datetime import datetime, timedelta
from .schemas import Delivery, DeliveryItem, Location, Driver, DeliveryStatus

# Mock drivers data
MOCK_DRIVERS = {
    "driver1": Driver(
        id="driver1",
        name="John Doe",
        phone="+1234567890",
        email="john@example.com",
        vehicleType="bike",
        vehicleNumber="BIKE123",
        rating=4.8,
        totalDeliveries=150
    ),
    "driver2": Driver(
        id="driver2",
        name="Jane Smith",
        phone="+0987654321",
        email="jane@example.com",
        vehicleType="scooter",
        vehicleNumber="SCOOT456",
        rating=4.9,
        totalDeliveries=200
    )
}

# Mock deliveries data
MOCK_DELIVERIES = {
    "driver1": [
        Delivery(
            id="delivery1",
            orderId="order1",
            customerName="Alice Johnson",
            customerAddress="123 Main St, City",
            customerPhone="+1112223333",
            items=[
                DeliveryItem(
                    id="item1",
                    name="Burger",
                    quantity=2,
                    price=12.99
                ),
                DeliveryItem(
                    id="item2",
                    name="Fries",
                    quantity=1,
                    price=4.99
                )
            ],
            status=DeliveryStatus.IN_TRANSIT,
            pickupLocation=Location(
                latitude=40.7128,
                longitude=-74.0060,
                address="Restaurant A, 456 Food St"
            ),
            deliveryLocation=Location(
                latitude=40.7148,
                longitude=-74.0080,
                address="123 Main St, City"
            ),
            estimatedTime=(datetime.now() + timedelta(minutes=15)).isoformat(),
            notes="Please ring bell twice"
        ),
        Delivery(
            id="delivery2",
            orderId="order2",
            customerName="Bob Wilson",
            customerAddress="789 Oak Ave, Town",
            customerPhone="+4445556666",
            items=[
                DeliveryItem(
                    id="item3",
                    name="Pizza",
                    quantity=1,
                    price=18.99
                )
            ],
            status=DeliveryStatus.PENDING,
            pickupLocation=Location(
                latitude=40.7138,
                longitude=-74.0070,
                address="Restaurant B, 789 Pizza St"
            ),
            deliveryLocation=Location(
                latitude=40.7158,
                longitude=-74.0090,
                address="789 Oak Ave, Town"
            ),
            estimatedTime=(datetime.now() + timedelta(minutes=30)).isoformat()
        )
    ],
    "driver2": [
        Delivery(
            id="delivery3",
            orderId="order3",
            customerName="Charlie Brown",
            customerAddress="321 Pine St, Village",
            customerPhone="+7778889999",
            items=[
                DeliveryItem(
                    id="item4",
                    name="Sushi Combo",
                    quantity=1,
                    price=25.99
                )
            ],
            status=DeliveryStatus.PICKED_UP,
            pickupLocation=Location(
                latitude=40.7120,
                longitude=-74.0050,
                address="Restaurant C, 123 Sushi St"
            ),
            deliveryLocation=Location(
                latitude=40.7140,
                longitude=-74.0070,
                address="321 Pine St, Village"
            ),
            estimatedTime=(datetime.now() + timedelta(minutes=20)).isoformat()
        )
    ]
} 