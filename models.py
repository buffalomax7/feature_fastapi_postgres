# from database import Base
# from sqlalchemy import Column, String, Boolean, Integer


# class DeviceInfo(Base):
#     __tablename__ = 'DeviceInfo'
#     token = Column(String, primary_key = True)
#     username = Column(String, default = 'user')


# class Configuration(Base):
#     __tablename__ = 'Configuration'
#     id = Column(Integer, primary_key = True, autoincrement = True)
#     modelUrl = Column(String)
#     frequency = Column(Integer)
#     federated = Column(Boolean)

# class DataList(Base):
#     __tablename__ = 'DataList'
#     id = Column(Integer, primary_key = True, autoincrement = True)
#     dataTitle = Column(String)
#     data = Column(String)

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")