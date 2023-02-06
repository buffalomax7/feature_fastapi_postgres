# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# #SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost:5432/postgres"

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(bind=engine)
# Base = declarative_base()


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost:5432/temp"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()