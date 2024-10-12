# CRUD_MONGO_PYTHON
# Setup and Run the Project Locally

This section explains how to set up and run the FastAPI project locally on your machine.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:
- **Python 3.7+**: FastAPI requires Python 3.7 or higher.
- **MongoDB**: This project uses MongoDB as its database.
- **pip**: Python's package installer.

## Steps to Set Up the Project

### 1. Clone the Repository

First, clone the project repository from your version control system (e.g., GitHub):

```bash
git clone https://github.com/AnirbanPatragithub/CRUD_MONGO_PYTHON.git
cd CRUD_MONGO_PYTHON
```

### 2. Create and Activate a Virtual Environment

It is recommended to use a virtual environment for managing dependencies:

- On Windows:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

- On macOS/Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

### 3. Install the Dependencies

With the virtual environment activated, install the necessary dependencies using `pip`:

```bash
pip install -r requirements.txt
```

Make sure the `requirements.txt` file includes the following (and possibly other dependencies as needed):
```text
fastapi
uvicorn
pymongo
bson
```

### 4. Set Up MongoDB

Ensure MongoDB is installed and running locally. The FastAPI application connects to a MongoDB instance using `localhost`.

To install MongoDB, refer to the official [MongoDB installation documentation](https://docs.mongodb.com/manual/installation/).

After installation, start MongoDB:
- On Windows:
    ```bash
    net start MongoDB
    ```

- On macOS/Linux:
    ```bash
    brew services start mongodb/brew/mongodb-community
    ```

Alternatively, if you want to use a hosted MongoDB instance (e.g., MongoDB Atlas), ensure that you update your MongoDB connection string in the `config/db.py` file.

### 5. Configure MongoDB Connection

In the `config/db.py` file, you should configure the MongoDB connection details. For example:

```python
from pymongo import MongoClient

conn = MongoClient('mongodb://localhost:27017')
```

If using a cloud-hosted MongoDB instance (e.g., MongoDB Atlas), update the connection string accordingly.

### 6. Run the FastAPI Application

Start the FastAPI server using Uvicorn. You can run it in development mode by using the `--reload` option:

```bash
uvicorn index:app --reload
```

This will start the server and make it available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### 7. Access the API Documentation

Once the server is running, you can access the automatically generated API documentation by visiting:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
  
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Both provide interactive documentation where you can test the APIs.

---

## Example `.env` File (Optional)

If you want to manage sensitive configuration values like the MongoDB connection string using environment variables, you can use a `.env` file and a package like `python-dotenv` to load these variables into your FastAPI application.

1. Install the package:

    ```bash
    pip install python-dotenv
    ```

2. Create a `.env` file in the root directory with the following content:

    ```text
    MONGO_URI=mongodb://localhost:27017
    ```

3. Modify your MongoDB connection code in `config/db.py` to use this environment variable:

    ```python
    from pymongo import MongoClient
    import os
    from dotenv import load_dotenv

    load_dotenv()

    MONGO_URI = os.getenv("MONGO_URI")
    conn = MongoClient(MONGO_URI)
    ```

---

## Running Tests (Optional)

If your project has tests set up, you can run them using a test runner like `pytest`:

1. Install `pytest`:

    ```bash
    pip install pytest
    ```

2. Run the tests:

    ```bash
    pytest
    ```

This will run all the test cases in the project.

---

## Conclusion

Once you have followed the steps above, your FastAPI application should be running locally, connected to your MongoDB instance, and accessible via the API documentation URLs.

# API Documentation for Clock-In and Item Management System

This documentation provides a detailed explanation of the API endpoints for managing users' clock-in records and items in a MongoDB database using FastAPI.

## Table of Contents
1. [User Clock-In Endpoints](#user-clock-in-endpoints)
   - Get all users
   - Get user by ID
   - Filter users
   - Create user clock-in
   - Update user clock-in
   - Delete user clock-in
2. [Item Management Endpoints](#item-management-endpoints)
   - Get all items
   - Get item by ID
   - Filter items
   - Create an item
   - Update item details
   - Count items by email
   - Delete item

---

## User Clock-In Endpoints

### 1. Get All Users

**Endpoint:** `/all_user`  
**Method:** `GET`  
**Description:** Returns a list of all users.

**Response:**  
```json
[
    {
        "email": "example@example.com",
        "location": "Location A",
        "clock_in": "2024-10-10T09:15:00Z"
    },
    ...
]
```

---

### 2. Get User by ID

**Endpoint:** `/clock-in/{id}`  
**Method:** `GET`  
**Description:** Fetch a user based on the provided user ID.

**Path Parameter:**
- `id` (string) – The ID of the user.

**Response:**  
```json
{
    "email": "example@example.com",
    "location": "Location A",
    "clock_in": "2024-10-10T09:15:00Z"
}
```

---

### 3. Filter Users

**Endpoint:** `/clock-filter/`  
**Method:** `GET`  
**Description:** Filters users based on optional parameters such as email, location, and clock-in time.

**Query Parameters:**
- `email` (string, optional) – Filter by user email.
- `location` (string, optional) – Filter by location.
- `clock_in` (datetime, optional) – Filter by clock-in time (greater than or equal to).

**Response:**  
```json
[
    {
        "email": "example@example.com",
        "location": "Location A",
        "clock_in": "2024-10-10T09:15:00Z"
    },
    ...
]
```

---

### 4. Create User Clock-In

**Endpoint:** `/clock-in`  
**Method:** `POST`  
**Description:** Creates a new user clock-in record. Automatically sets the clock-in time.

**Request Body:**
```json
{
    "email": "example@example.com",
    "location": "Location A"
}
```

**Response:**  
```json
[
    {
        "email": "example@example.com",
        "location": "Location A",
        "clock_in": "2024-10-10T09:15:00Z"
    },
    ...
]
```

---

### 5. Update User Clock-In

**Endpoint:** `/clock-in/{id}`  
**Method:** `PUT`  
**Description:** Updates the clock-in time of a user by ID.

**Path Parameter:**
- `id` (string) – The ID of the user.

**Request Body:**
```json
{
    "clock_in": "2024-10-12T08:45:00Z"
}
```

**Response:**  
```json
{
    "email": "example@example.com",
    "location": "Location A",
    "clock_in": "2024-10-12T08:45:00Z"
}
```

---

### 6. Delete User Clock-In

**Endpoint:** `/clock-in/{id}`  
**Method:** `DELETE`  
**Description:** Deletes a user clock-in record by ID.

**Path Parameter:**
- `id` (string) – The ID of the user.

**Response:**  
```json
{
    "email": "example@example.com",
    "location": "Location A",
    "clock_in": "2024-10-10T09:15:00Z"
}
```

---

## Item Management Endpoints

### 1. Get All Items

**Endpoint:** `/all_item`  
**Method:** `GET`  
**Description:** Returns a list of all items.

**Response:**  
```json
[
    {
        "email": "example@example.com",
        "name": "Item Name",
        "quantity": 10,
        "insert_date": "2024-10-10T09:15:00Z",
        "expiry_date": "2024-12-01T00:00:00Z"
    },
    ...
]
```

---

### 2. Get Item by ID

**Endpoint:** `/item/{id}`  
**Method:** `GET`  
**Description:** Fetches an item by the provided item ID.

**Path Parameter:**
- `id` (string) – The ID of the item.

**Response:**  
```json
{
    "email": "example@example.com",
    "name": "Item Name",
    "quantity": 10,
    "insert_date": "2024-10-10T09:15:00Z",
    "expiry_date": "2024-12-01T00:00:00Z"
}
```

---

### 3. Filter Items

**Endpoint:** `/item-filter/`  
**Method:** `GET`  
**Description:** Filters items based on optional parameters like email, quantity, insert date, and expiry date.

**Query Parameters:**
- `email` (string, optional) – Filter by email.
- `quantity` (integer, optional) – Filter by quantity (greater than or equal to).
- `insert_date` (datetime, optional) – Filter by insert date (greater than or equal to).
- `expiry_date` (datetime, optional) – Filter by expiry date (greater than or equal to).

**Response:**  
```json
[
    {
        "email": "example@example.com",
        "name": "Item Name",
        "quantity": 10,
        "insert_date": "2024-10-10T09:15:00Z",
        "expiry_date": "2024-12-01T00:00:00Z"
    },
    ...
]
```

---

### 4. Create an Item

**Endpoint:** `/item`  
**Method:** `POST`  
**Description:** Creates a new item.

**Request Body:**
```json
{
    "email": "example@example.com",
    "name": "Item Owner Name",
    "item_name": "Item Name",
    "quantity": 10,
    "expiry_date": "2024-12-01T00:00:00Z"
}
```

**Response:**  
```json
[
    {
        "email": "example@example.com",
        "name": "Item Owner Name",
        "item_name": "Item Name",
        "quantity": 10,
        "insert_date": "2024-10-10T09:15:00Z",
        "expiry_date": "2024-12-01T00:00:00Z"
    },
    ...
]
```

---

### 5. Update Item Details

**Endpoint:** `/update_item_details/{id}`  
**Method:** `PUT`  
**Description:** Updates item details by item ID.

**Path Parameter:**
- `id` (string) – The ID of the item.

**Request Body:** (Only include fields that need updating)
```json
{
    "email": "example@example.com",
    "name": "Updated Name",
    "item_name": "Updated Item Name",
    "quantity": 5,
    "expiry_date": "2024-11-01T00:00:00Z"
}
```

**Response:**  
```json
{
    "email": "example@example.com",
    "name": "Updated Name",
    "item_name": "Updated Item Name",
    "quantity": 5,
    "expiry_date": "2024-11-01T00:00:00Z"
}
```

---

### 6. Count Items by Email

**Endpoint:** `/items/count-by-email`  
**Method:** `GET`  
**Description:** Returns the count of items grouped by email.

**Response:**  
```json
[
    {
        "email": "example@example.com",
        "count": 5
    },
    ...
]
```

---

### 7. Delete Item

**Endpoint:** `/item/{id}`  
**Method:** `DELETE`  
**Description:** Deletes an item by ID.

**Path Parameter:**
- `id` (string) – The ID of the item.

**Response:**  
```json
{
    "email": "example@example.com",
    "item_name": "Item Name",
    "quantity": 10,
    "insert_date": "2024-10-10T09:15:00Z",
    "expiry_date": "2024-12-01T00:00:00Z"
}
```
