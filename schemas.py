# from pydantic import BaseModel
# from typing import Optional

# class DeviceInfo(BaseModel):
#     token: str
#     username: Optional[str]

#     class Config:
#         orm_mode = True


# class Configuration(BaseModel):
#     modelUrl: str
#     frequency: int
#     federated: bool

#     class Config:
#         orm_mode = True

# class DataList(BaseModel):
#     dataTitle: str
#     data: str

#     class Config:
#         orm_mode = True
from typing import Union

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True