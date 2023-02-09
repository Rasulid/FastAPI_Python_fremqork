from fastapi import APIRouter, Query, HTTPException, status, Body
from api.responses.detail import DetailResponse
from pydantic import BaseModel
from starlette.responses import JSONResponse

router = APIRouter(prefix="/demo", tags=["demo"], responses={404: {"response": "msg"}})


class NameModel(BaseModel):
    name: str
    perifix: str = "mr"


@router.get("/", response_model=DetailResponse)
def hello_world():
    """
    This is hello word endpoint
    """
    return DetailResponse(message="helo")


@router.post("/hello/{name_id}", response_model=DetailResponse)
def sent_det(name: str = Body(..., title="BODYYY", description="it is a BOOOODYYY")):
    return DetailResponse(message=f"hello {name}")


@router.post("/hello/{name}", response_model=DetailResponse)
def sent_deta(name: str = Query(..., title="names", description="The name")):
    return DetailResponse(message=f"hello  {name}")


@router.delete("/delete", response_model=DetailResponse)
async def delete_data():
    return DetailResponse(message="Data deleted")


@router.delete(
    "/delete/{name}",
    response_model=DetailResponse,
    responses={404: {"model": DetailResponse}},
)
async def delete_data(name: str):
    if name == "root":
        raise JSONResponse(status_code=status.HTTP_423_LOCKED)
    return DetailResponse(message=f"Data deleted fro {name}")
