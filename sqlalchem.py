import sqlalchemy
from sqlalchemy import create_engine
import mysql.connector
# sqlalchemy.__version__

mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlroot",
    database="project"
)
#create engine 
engine = create_engine("mysql://root:mysqlroot@localhost/project")
#mysql://username:password@hostname/database

#create 
from sqlalchemy import Column, Integer, String;
from sqlalchemy.orm import Relationship

class restraunt(Base):
  restraunts="restraunt1"
  res_id=Column(Integer, primary_key=True)
  name=Column(String(80),nullable=False)
  city=Column(String(50),nulallable=False)
  state=Column(String(50),nullable=False)
  zipcode=Column(String(50), nullable=False)
  Country=Column(String(50), nullable=False)
  Cuisines=Column(Integer(120), nullable=False)
  pickup_enable=Column(Integer, nullable=False)
  Delivery_Enabled=Column(Integer, nullable=False)
  weighted_rating=Column(Integer, nullable=False)
  Aggregated=Column(Integer, nullable=False)

  Base.metadata.create_all(engine)