from pydantic import BaseModel


class new_emp(BaseModel):
    name : str
    email : str
    address : str
