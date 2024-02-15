from pydantic import BaseModel, Field

from utils.fakers import (
    random_date,
    random_number,
    random_string,
    random_boolean,
)


class Order(BaseModel):
    """
    {
    "id": 0,
    "petId": 0,
    "quantity": 0,
    "shipDate": "2023-11-18T18:38:33.309Z",
    "status": "placed",
    "complete": true
    }
    """

    id: int = Field(default_factory=random_number)
    pet_id: int = Field(alias="petId", default_factory=random_number)
    quantity: int = Field(default_factory=random_number)
    shipDate: str = Field(default_factory=random_date)
    status: str = Field(default_factory=random_string)
    complete: bool = Field(default_factory=random_boolean)


class WrongOrder(BaseModel):
    """
    {
    "id": 0,
    "petId": 0,
    "quantity": "summer", - mistake
    "shipDate": "2023-11-18T18:38:33.309Z",
    "status": "placed",
    "complete": true
    }
    """

    id: int = Field(default_factory=random_number)
    pet_id: int = Field(alias="petId", default_factory=random_number)
    quantity: str = Field(default_factory=random_string)
    shipDate: str = Field(default_factory=random_date)
    status: str = Field(default_factory=random_string)
    complete: bool = Field(default_factory=random_boolean)


class DefaultUser(BaseModel):
    """
    {
    "id": 0,
    "username": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
    }
    """

    id: int = Field(default_factory=random_number)
    username: str = Field(default_factory=random_string)
    first_name: str = Field(alias="firstName", default_factory=random_string)
    last_name: str = Field(alias="lastName", default_factory=random_string)
    email: str = Field(default_factory=random_string)
    password: str = Field(default_factory=random_string)
    phone: str = Field(default_factory=random_string)
    user_status: str = Field(alias="userStatus", default_factory=random_number)
    


class WrongUser(BaseModel):
    """
    {
    "id": 0,
    "username": "string",
    "firstName": "int", - mistake
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
    }
    """

    id: int = Field(default_factory=random_number)
    username: str = Field(default_factory=random_string)
    first_name: int = Field(alias="firstName", default_factory=random_number)
    last_name: str = Field(alias="lastName", default_factory=random_string)
    email: str = Field(default_factory=random_string)
    password: str = Field(default_factory=random_string)
    phone: str = Field(default_factory=random_string)
    user_status: str = Field(alias="userStatus", default_factory=random_number)
