from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My store",
        "items": [
            {
                "name": "cadeira",
                "price": 15
            }
        ]
    }
]

@app.get("/store")
def get_stores():
    return {"stores": stores}

@app.post("/store")
def post_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"]}
    stores.append(new_store)
    return new_store, 201


@app.post("/store/<string:name>/add-product")
def post_product(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_product = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_product)
        
        return new_product, 201