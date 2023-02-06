# from sqlalchemy.orm import Session
# import schema, models


# def save_device_info(db: Session, info: schema.DeviceInfo):
#     device_info_model = models.DeviceInfo(**info.dict())
#     db.add(device_info_model)
#     db.commit()
#     db.refresh(device_info_model)
#     return device_info_model

# def get_device_info(db: Session, token: str = None):
#     if token is None:
#         return db.query(models.DeviceInfo).all()
#     else:
#         return db.query(models.DeviceInfo).filter(models.DeviceInfo.token == token).first()

# def save_nudges_configuration(db: Session, config: schema.Configuration):
#     config_model = models.Configuration(**config.dict())
#     db.add(config_model)
#     db.commit()
#     db.refresh(config_model)
#     return config_model

# def get_nudges_configuration(db: Session):
#     return db.query(models.Configuration).first()

# def delete_nudges_configuration(db: Session):
#     db.query(models.Configuration).delete()

# def error_message(message):
#     return {
#         'error': message
#     }
from sqlalchemy.orm import Session

import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item