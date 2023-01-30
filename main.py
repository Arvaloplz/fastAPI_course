
from typing import Optional
from enum import Enum
from pydantic import BaseModel, Field, EmailStr
from fastapi import FastAPI
from fastapi import Body, Query, Path


class HairColor(Enum):
    white = 'white'
    black = 'black'
    blue = 'blue'
    green = 'green'


class Location(BaseModel):
    # * Default body with Field
    city: str = Field(default=None, example='Calama')
    state: str = Field(default=None, example='Loa')
    contry: str = Field(default=None, example='Chile')


class Person(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    email: EmailStr = Field(...)
    age: int = Field(..., gt=0, lt=115)
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)

    class Config:
        # * Default body
        schema_extra = {
            'example': {
                'first_name': 'Dremian',
                'last_name': 'Androide',
                'email': 'arvaloplz@gmail.com',
                'age': 31,
                'hair_color': 'white',
                'is_married': False,
            }
        }


app = FastAPI()


@app.get('/')   # * Path Operation decoration
def Home():     # * Path Operation function
    return {'hello ': 'world'}

# * Req Res


@app.post('/person/new')
def create_person(person: Person = Body(...)):
    # Body(...) quiere decir que el parametro es obligatorio lol
    return person

# * Validation: Query parameter


@app.get('/person/detail')
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length=50, title='Person Name',
                                description='This is the person name, It´s between 1 and 50 characters'),
    # no se utiliza obligatorio practicamente nunca
    age: Optional[int] = Query(..., title='Person Age',
                               description='This is the person age, It´s required')
):
    return {name: age}

# * Validation: Path parameter


@app.get('/person/detail/{person_id}')
def show_person(person_id: int = Path(..., gt=0, title='Person Id',
                                      description='This is the person ID, It´s greater than 0 and required')):
    return {person_id: 'it exist'}


@app.put('/person/{person_id}')
def update_person(
    person_id: int = Path(..., gt=0, title='PersonId',
                          description='This is the person ID, It´s greater than 0 and required'),
    location: Location = Body(...),
    person: Person = Body(...)
):
    result = location.dict()
    result.update(person.dict())
    return result
