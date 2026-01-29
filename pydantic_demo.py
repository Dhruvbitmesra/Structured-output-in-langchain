from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):

    name:str
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10,default=5,description="decimal value representing the cgpa")

new_student={'name':'Dhruv'}

student=Student(**new_student)

student_dict=dict(student)

print(student_dict)

