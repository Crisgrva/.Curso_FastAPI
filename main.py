# Python
from lib2to3.pgen2.token import TILDE
from lib2to3.pytree import Base
from turtle import title
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastApi
from fastapi import FastAPI
from fastapi import Body, Query, Path


app = FastAPI()


# Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


@app.get("/")
def home():
    return {"Hello": "World"}


# Requests and Response Body

@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person


# Validations: query parameters
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title="Person name",
        description="This is the person name. It's between 1 and 50 characteres"
    ),
    age: str = Query(
        ...,
        title="Person Age",
        description="This is the person age. It's required"
    )
):
    return {name: age}


# Validations: Path parameters
@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Person id",
        description="This is the person id. It's required",
    )
):
    return {person_id: "It exists!"}
