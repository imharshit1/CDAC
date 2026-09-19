from fastapi import FastAPI
from datetime import datetime
app = FastAPI()
orders = []
@app.get("/")
def home():
    return {"message": "Order Management API is running"}
@app.get("/orders")
def get_orders():
    return {
        "orders": orders
    }
@app.post("/orders")
def create_order(order_id: int, product: str, quantity: int):

    order = {
        "order_id": order_id,
        "product": product,
        "quantity": quantity,
        "created_at": str(datetime.now())
    }

    orders.append(order)

    return {
        "message": "Order created successfully",
        "order": order
    }