from fastapi import APIRouter

from app.calc.dao import RodDAO, CoilDAO

router_calc = APIRouter(prefix="/calc", tags=["Calculation"])


@router_calc.post("/rod")
async def calc_rod(name: str, percentage: int):
    return await RodDAO.calc_wear(name=name, percentage=percentage)


@router_calc.post("/coil")
async def calc_coil(name: str, percentage: int):
    return await CoilDAO.calc_wear(name=name, percentage=percentage)
