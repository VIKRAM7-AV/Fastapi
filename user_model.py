from pydantic import BaseModel, EmailStr
class User(BaseModel):
    name:str
    email:EmailStr
    password:str
    age:int


User1 = User(name="Vikram",email="vikram@example.com",password="secret123",age=25)

print(User1);