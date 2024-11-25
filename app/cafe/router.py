from fastapi import APIRouter

from app.cafe.dao import CafeDAO

router_cafe = APIRouter(
    prefix="/cafe",
    tags=["Cafe"],
)


@router_cafe.get("/")
async def get_all():
    return await CafeDAO.find_all()


@router_cafe.get("/{location}/{fish}")
async def get_one(location: str, fish: str):
    return await CafeDAO.find_all(location=location, fish=fish)
