from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)


@app.route("/")
def home():
    # Homepage route - returns a simple welcome message as JSON
    return jsonify({"message": "Welcome to the Product Catalog API"}), 200


@app.route("/products")
def get_products():
    # Optional query param filtering by category, e.g. /products?category=books
    category = request.args.get("category")

    if category:
        # Normalize both sides to lowercase to avoid mismatches (Books vs books)
        filtered = [p for p in products if p["category"].lower() == category.lower()]
        return jsonify(filtered), 200

    # No filter provided - return the full product list
    return jsonify(products), 200


@app.route("/products/<int:id>")
def get_product_by_id(id):
    # Look for a product matching the given id
    product = next((p for p in products if p["id"] == id), None)

    if product:
        return jsonify(product), 200
    else:
        # No matching product - return 404 with a clear JSON error message
        return jsonify({"error": f"Product with id {id} not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)