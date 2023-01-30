
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi import Body


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


app = FastAPI()


@app.get('/')   # * Path Operation decoration
def Home():     # * Path Operation function
    return {'hello ': 'world'}

# * Req Res


@app.post('/person/new')
def create_person(person: Person = Body(...)):
    # Body(...) quiere decir que el parametro es obligatorio lol
    return person
