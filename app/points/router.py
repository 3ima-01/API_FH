from fastapi import APIRouter, Depends

from app.points import schemas
from app.points.dao import PointDAO
from app.users.dependencies import get_current_user

from app.exceptions import NotYourPointException, PointNotFoundException


router_point = APIRouter(
    prefix="/points",
    tags=["Points"],
)


@router_point.post("/create")
async def create_point(point_data: schemas.Point, user_data=Depends(get_current_user)):
    current_user, _ = user_data
    new_point = await PointDAO.create(
        user_uuid=current_user.uuid,
        title=point_data.title,
        fish=point_data.fish.lower(),
        location=point_data.location.lower(),
        coords=point_data.coords,
        images=point_data.images,
    )
    return {"details": "Точка успешно создана"}


@router_point.get("/")
async def get_user_points(user_data=Depends(get_current_user)):
    current_user, _ = user_data
    return await PointDAO.find_all(user_uuid=current_user.uuid)


@router_point.get("/{point_uuid}")
async def get_point_bu_id(point_uuid: str):
    return await PointDAO.find_one_or_none(uuid=point_uuid)


@router_point.patch("/{point_uuid}/update")
async def update_point(
    point_uuid: str, point_data: schemas.Point, user_data=Depends(get_current_user)
):
    current_user, _ = user_data
    old_point = await PointDAO.find_one_or_none(uuid=point_uuid)
    if not old_point:
        raise PointNotFoundException
    if old_point.user_uuid != current_user.uuid:
        raise NotYourPointException
    await PointDAO.update(
        point_uuid,
        title=point_data.title,
        fish=point_data.fish.lower(),
        location=point_data.location.lower(),
        coords=point_data.coords,
        images=point_data.images,
    )
    return {"details": "Точка успешно обновлена"}
