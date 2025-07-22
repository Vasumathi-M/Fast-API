from fastapi import FastAPI  #fastapi -> package
app=FastAPI() #initialization
from pydantic import BaseModel

@app.get('/')
def index():
    return {'name' : 'vasu', 'message' : 'hi'}

@app.get('/about')
def aboutfunc():
    return {'data': {'name': 'mathi', 'age' : '21'}}

    

#path params

@app.get('/users/certified')
def certified_users():
    return 'certified user'


@app.get('/users/{id}')
def displayUser(id : int):  #str  / int
    #return id
    return f'User with id={id} is displayed'




#pydantic model => validation
#query params
@app.get('/users')
def conditionUser(limit:int,failed:bool=True, sort:str |None=None): #using pydantic validation
    if failed==True:
        return f'Failed {limit} users List'
    else:
        return 'all students'

#pydantic model
class CreateModel(BaseModel): #inheritance -> Base(parent), createmodel(child)
    name:str
    age:int | None=None
    email:str
    phn:int | None=None
     

    

#POST
@app.post('/adduser')
def createUser(request:CreateModel): #taking from users 
    return request