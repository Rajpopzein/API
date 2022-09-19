from enum import unique
from pickle import TRUE
import string
from sqlalchemy import Table, Column , UniqueConstraint
from sqlalchemy.sql.sqltypes import Integer , String
from database.database import engine , Meta


Employee = Table("Employee",Meta, Column("id",Integer,primary_key = True,autoincrement = True),Column("email", String(50), nullable = False),Column("name", String(255)),Column("address", String(255)))

Meta.create_all(engine)