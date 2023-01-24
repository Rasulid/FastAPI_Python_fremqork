from fastapi import APIRouter

from api.responses.detail import DetailResponse

router = APIRouter(prefix="/demo", tags=["demo"], responses={404: {"response": "msg"}})


@router.get("/", response_model=DetailResponse)
def hello_world():
    """
    This is hello word endpoint
    """
    return DetailResponse(message="helo")
