import pytest
from app.server import app

@pytest.fixture
def client():
    """Fixture to create a test client for the Flask application."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_create_item(client):
    """
    Test creating a new item in the API.

    Steps:
    1. Send a POST request with valid item data.
    2. Verify the response status code is 201 (Created).
    3. Verify the response JSON contains the expected keys and values.
    """
    response = client.post("/items", json={"name": "Test Item", "value": 100})
    assert response.status_code == 201

    data = response.get_json()
    assert "id" in data
    assert data["name"] == "Test Item"
    assert data["value"] == 100

def test_get_item(client):
    """
    Test retrieving an existing item from the API.

    Steps:
    1. Create an item first using a POST request.
    2. Extract the item ID from the response.
    3. Send a GET request to fetch that item.
    4. Verify the response contains the correct data.
    """
    # Create an item first
    create_response = client.post("/items", json={"name": "Sample Item", "value": 42})
    assert create_response.status_code == 201
    item_id = create_response.get_json()["id"]

    # Retrieve the item
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200

    data = response.get_json()
    assert data["id"] == item_id
    assert data["name"] == "Sample Item"
    assert data["value"] == 42
