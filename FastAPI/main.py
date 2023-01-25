from typing import Union, List
from models import User, uuid4, Gender, Role,UUID
from fastapi import FastAPI

app = FastAPI()

db: List[User] = [
    User(id=UUID("df03b203-8370-40bb-a6e1-7ced9ff5003b"), 
         first_name='Jamila', 
         last_name='Ahmed',
         gender = Gender.female,
         roles = [Role.studant]),
    User(id=UUID("400d8685-78c0-4da4-8ed6-40a2fbad4761"), 
         first_name='Roberta', 
         last_name='Silveira',
         gender = Gender.male,
         roles = [Role.admin, Role.user])
]



@app.get("/")
async def read_root():
    # await foo()
    return {"Hello": "World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {'id': user.id}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
