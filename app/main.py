from fastapi import FastAPI
from database.database import conn
from module.employee import Employee
from schemas.edit import edit_emp
from schemas.new_employee import new_emp
app = FastAPI()


@app.get("/")
def root():
    return {"data": "hello"}



@app.get("/user")
def get_user(id: int):
    #commend to fetch data from database using sqlalchmy and mysql
    data = conn.execute(Employee.select().where(Employee.c.id == id)).first()
    if data:
        return data
    else:
        return {"data": "data not found"}



@app.post("/adduser")
async def set_user(emp : new_emp):
        value = {'name' : emp.name.capitalize() ,'email' : emp.email,'address' : emp.address.capitalize()}
        emails = conn.execute(Employee.select().where(Employee.c.email == emp.email)).first()
        if emails:
            return{'data':'email already exist'}
        else:
            #command to pass data to the database
            conn.execute(Employee.insert().values(value))
            id = conn.execute(Employee.select().where(Employee.c.email == emp.email)).first()
            if id:
                return {'data':'Employee added sucessfully'}



@app.put("/edituser")
def edt_use(id : int, emp : edit_emp):
            ids = conn.execute(Employee.select().where(Employee.c.id == id)).first()
            if ids:
                conn.execute(Employee.update().where(Employee.c.id == id).values(name = emp.name.capitalize(),address = emp.address.capitalize()))
                return{'data':'Updated success'}
            else:
                return{'data':'Data not found'}
        

@app.delete("/deleteuser")
def del_usr(id : int):
    ids = conn.execute(Employee.select().where(Employee.c.id == id)).first()
    if ids:
        conn.execute(Employee.delete().where(Employee.c.id == id))
        return{'Employee deleted sucessfully'}
    else:
        return{'Employee record not found'}        

