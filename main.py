from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return("Hello, World!")

products = [
    Product(id = 1, name = "Phone", description = "Budget Phones",price = 9999, quantity = 10),
    Product(id = 2, name= "Laptop", description = "Budget Laptop", price = 59999, quantity = 5)
]

@app.get("/products")
def get_all_products():
    return products
