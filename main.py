# from main import app 
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def root():
    return 'Hello'

@app.get('/home')
async def root():
    return {'message':'Home', 'code': 200}
