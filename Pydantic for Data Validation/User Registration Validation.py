from pydantic import BaseModel, EmailStr, Field, ValidationError

class UserRegister(BaseModel):
    username: str = Field(..., min_length=5)
    email: EmailStr
    age: int = Field(..., ge=18)


# Example usage
try:
    user = UserRegister(
        username="abhi123",
        email="abhi@example.com",
        age=20
    )
    print("Valid user:", user)

except ValidationError as e:
    print("Validation Error:")
    print(e)
