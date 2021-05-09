from sqlalchemy import Column, String
from sqlalchemy import create_engine, MetaData, Table, Float, Integer
from sqlalchemy.ext.declarative import declarative_base

from config import URI

engine = create_engine(URI, echo=True)
meta = MetaData()

Base = declarative_base()
customers = Table(
    "Customers",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("age", String),
)

meta.create_all(engine)
