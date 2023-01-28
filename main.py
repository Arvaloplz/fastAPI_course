from fastapi import FastAPI

app = FastAPI()

@app.get('/')   # * Path Operation decoration
def Home():     # * Path Operation function
    return {'hello ': 'world'}