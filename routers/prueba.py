from fastapi import APIRouter
from config.database import Session
from typing import Optional, List
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from fastapi.responses import JSONResponse
from services.prueba import PruebaService
from schemas.prueba import Prueba


prueba_router = APIRouter()


@prueba_router.get('/pruebas', tags=['pruebas'], response_model=List[Prueba], status_code=200)
def get_pruebas() -> List[Prueba]:
    db = Session()
    result = PruebaService(db).get_pruebas()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))