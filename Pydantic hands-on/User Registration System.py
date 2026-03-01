from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Address(BaseModel):
    city: str = Field(min_length = 3)
    pincode: str = Field(min_length = 6, max_length = 6)

address_info = {'city': 'Delhi', 'pincode': '110091'}

add = Address(**address_info)

class User(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    age: int = Field(ge=18)
    address : Address
    is_premium: bool = False 

user_info = {'user_id': '7', 'name': 'Abhi', 'email': 'abhi@gmail.com', 'age': '26', 'address' : address_info}

user = User(**user_info)

print(user.age)
