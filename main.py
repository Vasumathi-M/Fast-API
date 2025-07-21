from fastapi import FastAPI  #fastapi -> package
app=FastAPI() #initialization

@app.get('/')
def index():
    return 'Python Fast API is working'

@app.get('/about')
def aboutfunc():
    return 'About page of FastAPI'


    