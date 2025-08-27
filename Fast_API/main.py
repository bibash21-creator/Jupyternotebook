from fastapi import FastAPI

app = FastAPI()

# Endpoitns

@app.get('/')

def display():
    return { 'Hello': 'Everyone'}

@app.get('/about')

def message():
    return {'Message': 'Today is Friday'}

