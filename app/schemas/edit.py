from pydantic import BaseModel


class edit_emp(BaseModel):
    name : str
    address : str