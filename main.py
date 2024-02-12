from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router
from routers.prueba import prueba_router

###################################
import pywhatkit
import time 
import pywhatkit
import pyautogui


app = FastAPI()
app.title = "Mi aplicación con  FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)

app.include_router(movie_router)
app.include_router(user_router)
app.include_router(prueba_router)

Base.metadata.create_all(bind=engine)


movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	},
    {
		"id": 2,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	}
]

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')


@app.post("/msg", tags=["msg"])  
async def send_message(number: str = Body(...), message: str = Body(...)):
    pywhatkit.sendwhatmsg(number, message, 10, 33, 20)
    return {"message": "Mensaje enviado con éxito"}       
