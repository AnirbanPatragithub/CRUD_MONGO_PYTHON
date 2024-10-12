from fastapi import APIRouter
from datetime import datetime
from models.user import User,Item
from bson import ObjectId
from config.db import conn
from typing import Optional
from schemas.user import userEntity,usersEntity,itemsEntity

user = APIRouter()
item = APIRouter()

@user.get('/all_user')
async def find_all_user():
    return usersEntity(conn.local.user.find())

@user.get('/clock-in/{id}')
async def get_user_by_id(id):
    return usersEntity([conn.local.user.find_one({"_id":ObjectId(id)})])


@user.get('/clock-filter/')
async def filter_users(
    email: Optional[str] = None,
    location: Optional[str] = None,
    clock_in: Optional[datetime] = None
):
    # Dynamically construct the query based on the provided filters
    query = {}
    
    if email:
        query["email"] = email
    if location:
        query["location"] = location
    if clock_in:
        query["clock_in"] = {"$gte": clock_in}
    
    # Execute the query
    users = conn.local.user.find(query)
    return usersEntity(users)


@user.post('/clock-in')
async def create_user(user:User):
    new_user = {
        "email": user.email,
        "location": user.location,
        "clock_in": datetime.now().isoformat()  # Automatically set clock_in
    }
    conn.local.user.insert_one(dict(new_user))
    return usersEntity(conn.local.user.find())

@user.put('/clock-in/{id}')
async def update_user_clock_in(id,user:User):
    conn.local.user.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": {"clock_in": user.clock_in}}
    )
    return usersEntity([conn.local.user.find_one({"_id": ObjectId(id)})])
    # conn.local.user.find_one_and_update({"_id":ObjectId(id)},
    #                                     {"$set":dict(user)})
    # return usersEntity([conn.local.user.find_one({"_id":ObjectId(id)})])

@user.delete('/clock-in/{id}')
async def delete_user(id):
    return usersEntity([conn.local.user.find_one_and_delete({"_id":ObjectId(id)})])







@item.get('/all_item')
async def find_all_item():
    return itemsEntity(conn.local.item.find())

@item.get('/item/{id}')
async def get_item_by_id(id):
    return itemsEntity([conn.local.item.find_one({"_id":ObjectId(id)})])


@item.get('/item-filter/')
async def filter_items(
    email: Optional[str] = None,
    quantity : Optional[int] = None,
    insert_date: Optional[datetime] = None,
    expiry_date: Optional[datetime] = None,
):
    # Dynamically construct the query based on the provided filters
    query = {}
    
    if email:
        query["email"] = email
    if quantity:
        query["quantity"] = {"$gte": quantity}
    if insert_date:
        query["insert_date"] = {"$gte": insert_date}
    if expiry_date:
        query["expiry_date"] = {"$gte": expiry_date}
    
    # Execute the query
    users = conn.local.item.find(query)
    return itemsEntity(users)


@item.post('/item')
async def create_item(item:Item):
    new_item = {
        "email": item.email,
        "name": item.name,
        "item_name": item.item_name,
        "quantity": item.quantity,
        "expiry_date":item.expiry_date,
        "insert_date": datetime.now().isoformat()  # Automatically set clock_in
    }
    conn.local.insert_one(dict(new_item))
    return itemsEntity(conn.local.item.find())

@item.put('/update_item_details/{id}')
async def update_item_details(id: str, item: Item):
    # Find the existing item by ID
    existing_item = conn.local.item.find_one({"_id": ObjectId(id)})

    if not existing_item:
        return {"error": "Item not found"}

    # Dynamically construct the update data based on fields that are provided (non-None)
    update_data = {
        "email": item.email if item.email is not None else existing_item["email"],
        "name": item.name if item.name is not None else existing_item["name"],
        "item_name": item.item_name if item.item_name is not None else existing_item["item_name"],
        "expiry_date": item.expiry_date if item.expiry_date is not None else existing_item["expiry_date"],
        "quantity": item.quantity if item.quantity is not None else existing_item["quantity"]
        # Do not include insert_date, it will remain unchanged
    }

    # Execute the update query
    conn.local.item.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": update_data}
    )
    
    # Return the updated item
    return itemsEntity([conn.local.item.find_one({"_id": ObjectId(id)})])

@item.get('/items/count-by-email')
async def count_items_by_email():
    # MongoDB aggregation pipeline
    pipeline = [
        {
            "$group": {
                "_id": "$email",  # Group by the email field
                "count": {"$sum": 1}  # Count the number of items for each email
            }
        }
    ]

    # Execute the aggregation
    result = conn.local.item.aggregate(pipeline)

    # Convert the result to a list and format it as needed
    count_by_email = [{"email": doc["_id"], "count": doc["count"]} for doc in result]

    return count_by_email


@item.delete('/item/{id}')
async def delete_user(id):
    return itemsEntity([conn.local.item.find_one_and_delete({"_id":ObjectId(id)})])
