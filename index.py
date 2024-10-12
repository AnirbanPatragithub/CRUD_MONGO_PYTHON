from fastapi import FastAPI
from routes.user import user,item

app = FastAPI()

app.include_router(user)
app.include_router(item)

#uvicorn index:app --reload