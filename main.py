from fastapi import FastAPI, Body, Form, UploadFile, File
from pydantic import BaseModel

app = FastAPI()

# class User(BaseModel):
#     name: str
#     age: int
#     email:str

# class UserResponse(BaseModel):
#     user:User

# @app.get("/")
# def recommendation(age: int):
#     if age < 18:
#         return {"recommendation": "You are a minor. We recommend you to watch cartoons."}
#     elif 18 <= age < 30:
#         return {"recommendation": "You are a young adult. We recommend you to watch action movies."}
#     elif 30 <= age < 50:
#         return {"recommendation": "You are an adult. We recommend you to watch drama movies."}
#     else:
#         return {"recommendation": "You are a senior. We recommend you to watch classic movies."}


# @app.post("/user/", response_model=UserResponse)
# def create_user(user: User):
#     return {"user": user}


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool 

@app.post("/items/")
def create_item(item: Item):
    return {
        "type": "json",
        "Name":item.name,
        "price":item.price,
        "Offer":item.is_offer
    }


@app.post("/items2/")
def plaintext(contant:str = Body(..., media_type="text/plain")):
    return {
        "type": "plaintext",
        "content": contant
    }

@app.post("/items3/")
def CreateForm(Username:str = Form(...), Password:str = Form(...)):
    return {
        "type": "form",
        "Username": Username,
        "Password": Password
    }

@app.post("/items4/")
def CreateFile(file: UploadFile = File(...)):
    return {
        "type": "file",
        "filename": file.filename,
        "content_type": file.content_type
    }