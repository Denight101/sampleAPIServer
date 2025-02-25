from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory dictionary to store items
data_store = {}
current_id = 1  # Auto-incrementing ID for items

@app.route("/items", methods=["GET"])
def get_items():
    """
    Retrieve all items stored on the server.

    Returns:
        JSON response containing a list of all stored items.
        HTTP 200 status code.
    """
    return jsonify(list(data_store.values())), 200

@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    """
    Retrieve a single item by its unique ID.

    Args:
        item_id (int): The ID of the item to retrieve.

    Returns:
        JSON response containing the requested item if found (HTTP 200).
        JSON error message if the item does not exist (HTTP 404).
    """
    item = data_store.get(item_id)
    if item:
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404

@app.route("/items", methods=["POST"])
def create_item():
    """
    Create a new item and store it in the dictionary.

    Expected JSON payload:
        {
            "name": "<string>",
            "value": "<any>"
        }

    Returns:
        JSON response with the newly created item (HTTP 201).
        JSON error message for invalid input (HTTP 400).
    """
    global current_id
    data = request.get_json()
    if not data or "name" not in data or "value" not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    item = {"id": current_id, "name": data["name"], "value": data["value"]}
    data_store[current_id] = item
    current_id += 1
    return jsonify(item), 201

@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    """
    Update an existing item in the dictionary.

    Args:
        item_id (int): The ID of the item to update.

    Expected JSON payload:
        {
            "name": "<string>",
            "value": "<any>"
        }

    Returns:
        JSON response with the updated item (HTTP 200).
        JSON error message if the item does not exist (HTTP 404).
        JSON error message for invalid input (HTTP 400).
    """
    data = request.get_json()
    if not data or "name" not in data or "value" not in data:
        return jsonify({"error": "Invalid input"}), 400

    if item_id not in data_store:
        return jsonify({"error": "Item not found"}), 404

    data_store[item_id] = {"id": item_id, "name": data["name"], "value": data["value"]}
    return jsonify(data_store[item_id]), 200

@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    """
    Delete an item from the dictionary by its ID.

    Args:
        item_id (int): The ID of the item to delete.

    Returns:
        JSON response confirming deletion (HTTP 200).
        JSON error message if the item does not exist (HTTP 404).
    """
    if item_id in data_store:
        del data_store[item_id]
        return jsonify({"message": "Item deleted"}), 200
    return jsonify({"error": "Item not found"}), 404

if __name__ == "__main__":
    """
    Start the Flask API server.

    The server listens on all available network interfaces (`0.0.0.0`)
    and runs on port 5000.
    """
    app.run(host="0.0.0.0", port=5000)
