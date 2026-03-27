from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test():
    return {"mensaje": "API funcionando correctamente"}