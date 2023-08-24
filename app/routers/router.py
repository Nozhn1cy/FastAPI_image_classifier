from fastapi import APIRouter
from fastapi import Request
from routers import prediction

router = APIRouter()
router.include_router(prediction.router)


@router.get("/status")
def status(request: Request) -> dict:
    """Status of application

    :param request: request
    :returns dictionary
    """
    return {"request": "Сервис работает."}
