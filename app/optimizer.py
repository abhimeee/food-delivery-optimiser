from app.schemas import OrderRequest, RouteResponse

def optimize_route(data: OrderRequest) -> RouteResponse:
    # Simple sort by delivery deadline for now
    sorted_orders = sorted(data.orders, key=lambda o: o.delivery_deadline)
    return RouteResponse(optimized_order_ids=[order.order_id for order in sorted_orders])
