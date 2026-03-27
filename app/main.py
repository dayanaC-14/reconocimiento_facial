from fastapi import FastAPI
from app.config.database import engine
from app.config.database import Base, engine
from app.models.user import User
from app.routes import test_routes

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def test_db():
    try:
        connection = engine.connect()
        return {"mensaje": "Conexión exitosa a la base de datos"}
    except:
        return {"error": "No conecta a la base de datos"}
   
app.include_router(test_routes.router, prefix="/api")