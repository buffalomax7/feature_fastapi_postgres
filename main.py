# from fastapi import FastAPI, Depends, HTTPException
# from database import SessionLocal, engine
# from sqlalchemy.orm import Session
# from schema import DeviceInfo, Configuration, DataList
# import crud, models

# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()

# def db():
#     try:
#         db = SessionLocal()
#         yield db
#     finally:
#         db.close()

# @app.post('/device/info')
# def save_device_info(info: DeviceInfo, db=Depends(db)):
#     object_in_db = crud.get_device_info(db, info.token)
#     if object_in_db:
#         raise HTTPException(400, detail= crud.error_message('This device info already exists'))
#     return crud.save_device_info(db,info)

# @app.get('/device/info/{token}')
# def get_device_info(token: str, db=Depends(db)):
#     info = crud.get_device_info(db,token)
#     if info:
#         return info
#     else:
#         raise HTTPException(404, crud.error_message('No device found for token {}'.format(token)))

# @app.get('/device/info')
# def get_all_device_info(db=Depends(db)):
#     return crud.get_device_info(db)

# @app.post('/configuration')
# def save_configuration(config: Configuration, db=Depends(db)):
#     # always maintain one config
#     crud.delete_nudges_configuration(db)
#     return crud.save_nudges_configuration(db, config)

# @app.get('/configuration')
# def get_configuration(db=Depends(db)):
#     config = crud.get_nudges_configuration(db)
#     if config:
#         return config
#     else:
#         raise HTTPException(404, crud.error_message('No configuration set'))


from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items