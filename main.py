
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi import Body, Query, Path


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
