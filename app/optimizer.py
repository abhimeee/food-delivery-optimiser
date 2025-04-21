from typing import List
from .schemas import Delivery, TemperatureSensitivity
from datetime import datetime, timedelta
import math

def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    # Haversine formula to calculate distance between two points
    R = 6371  # Earth's radius in kilometers
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    return R * c

def calculate_urgency_score(delivery: Delivery, current_time: datetime) -> float:
    # Calculate time remaining until delivery window end
    time_remaining = (delivery.delivery_window.end_time - current_time).total_seconds() / 60
    
    # Base urgency score from priority (higher priority = more urgent)
    urgency_score = delivery.delivery_window.priority * 2
    
    # Adjust for time remaining (less time = more urgent)
    if time_remaining < 30:  # Less than 30 minutes remaining
        urgency_score *= 1.5
    
    # Add penalty for late deliveries
    if current_time > delivery.delivery_window.end_time:
        urgency_score *= 2
    
    return urgency_score

def calculate_temperature_risk(delivery: Delivery, current_time: datetime) -> float:
    risk_score = 0
    
    for item in delivery.items:
        if item.temperature_sensitivity == TemperatureSensitivity.FROZEN:
            # Ice cream and other frozen items
            risk_score += 3
        elif item.temperature_sensitivity == TemperatureSensitivity.HOT:
            # Hot food items
            risk_score += 2
        elif item.temperature_sensitivity == TemperatureSensitivity.CHILLED:
            # Chilled items
            risk_score += 1.5
        
        # Adjust risk based on remaining safe time
        if item.max_safe_time_minutes:
            time_elapsed = (current_time - delivery.delivery_window.start_time).total_seconds() / 60
            time_remaining = item.max_safe_time_minutes - time_elapsed
            if time_remaining < 10:  # Less than 10 minutes of safe time remaining
                risk_score *= 1.5
    
    return risk_score

def calculate_route_score(delivery: Delivery, current_location: tuple[float, float], current_time: datetime) -> float:
    # Get pickup and delivery locations
    pickup_lat, pickup_lon = delivery.pickupLocation.latitude, delivery.pickupLocation.longitude
    delivery_lat, delivery_lon = delivery.deliveryLocation.latitude, delivery.deliveryLocation.longitude
    
    # Calculate distances
    distance_to_pickup = calculate_distance(current_location[0], current_location[1], pickup_lat, pickup_lon)
    distance_to_delivery = calculate_distance(pickup_lat, pickup_lon, delivery_lat, delivery_lon)
    total_distance = distance_to_pickup + distance_to_delivery
    
    # Calculate scores
    urgency_score = calculate_urgency_score(delivery, current_time)
    temperature_risk = calculate_temperature_risk(delivery, current_time)
    
    # Combine scores
    # Higher urgency and temperature risk increase the score
    # Longer distances decrease the score
    route_score = (urgency_score * 2 + temperature_risk * 1.5) / (total_distance + 1)
    
    # Add penalty for late deliveries
    if current_time > delivery.delivery_window.end_time:
        route_score *= 0.8  # Reduce score for late deliveries
    
    return route_score

def optimize_route(deliveries: List[Delivery], current_location: tuple[float, float], current_time: datetime) -> List[str]:
    """
    Optimize delivery route based on multiple factors:
    1. Delivery priority and time windows
    2. Temperature sensitivity of items
    3. Distance to pickup and delivery locations
    4. Current time and delivery deadlines
    """
    if not deliveries:
        return []
    
    # Calculate scores for all deliveries
    delivery_scores = [
        (delivery.id, calculate_route_score(delivery, current_location, current_time))
        for delivery in deliveries
    ]
    
    # Sort deliveries by score (higher score = higher priority)
    sorted_deliveries = sorted(delivery_scores, key=lambda x: x[1], reverse=True)
    
    # Return ordered list of delivery IDs
    return [delivery_id for delivery_id, _ in sorted_deliveries]
