from models.prueba import Prueba as PruebaModel
from schemas.prueba import Prueba


class PruebaService():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_pruebas(self):
        result = self.db.query(PruebaModel).all()
        return result