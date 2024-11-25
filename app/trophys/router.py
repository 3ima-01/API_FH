from fastapi import APIRouter

from app.trophys.dao import TrophyDAO

router_trophy = APIRouter(
    prefix="/trophy",
    tags=["Trophy"],
)


@router_trophy.get("/")
async def get_all():
    return await TrophyDAO.find_all()


@router_trophy.get("/{fish}")
async def get_by_fish(fish: str):
    return await TrophyDAO.find_all(fish=fish)
