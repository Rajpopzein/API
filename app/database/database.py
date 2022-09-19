from sqlalchemy import create_engine , MetaData


engine = create_engine("mysql+mysqldb://root:1234qwer@localhost:3306/company_set")
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

conn = engine.connect()
 
Meta = MetaData()