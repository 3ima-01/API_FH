from fastapi import APIRouter

from app.calc.dao import RodDAO, CoilDAO

router_parts = APIRouter(
    prefix="/parts",
    tags=["Parts"],
)


@router_parts.get("/rods")
async def get_rods():
    return await RodDAO.find_all()


@router_parts.get("/rods/{type}")
async def get_rods_by_type(type: str):
    return await RodDAO.find_all(type=type)


@router_parts.get("/coils")
async def get_coils():
    return await CoilDAO.find_all()


@router_parts.get("/coils/{type}")
async def get_coils_by_type(type: str):
    return await CoilDAO.find_all(type=type)
