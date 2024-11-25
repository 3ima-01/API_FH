from fastapi import APIRouter, Depends

from app.profiles.dao import ProfileDAO
from app.profiles import schemas
from app.users.dependencies import get_current_user

router_profiles = APIRouter(prefix="/profiles", tags=["Profiles"])


@router_profiles.get("/me", response_model=schemas.Profile)
async def get_profile(user_data=Depends(get_current_user)):
    current_user, _ = user_data
    return await ProfileDAO.find_one_or_none(user_uuid=current_user.uuid)


@router_profiles.patch("/upgrade")
async def update_profile(
    profile_data: schemas.Profile, user_data=Depends(get_current_user)
):
    current_user, _ = user_data
    profile = await ProfileDAO.find_one_or_none(user_uuid=current_user.uuid)
    return await ProfileDAO.update(
        uuid=profile.uuid,
        name=profile_data.name,
        avatar=profile_data.avatar,
        bio=profile_data.bio,
        lvl=profile_data.lvl,
    )
