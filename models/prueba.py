from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class Prueba(Base):

    __tablename__ = "pruebas"

    id = Column(Integer, primary_key = True)
    title = Column(String)