from fastapi import APIRouter, HTTPException, status

from app.api.deps import AuthDep
from app.schemas.target import TargetAchievement, TargetCreate, TargetOut, TargetUpdate
from app.services.target_service import TargetService

router = APIRouter()


@router.get("/", response_model=list[TargetOut])
def list_targets(token: AuthDep):
    return TargetService.list_targets()


# Specific routes before parameterized ones
@router.get("/seller/{seller_id}", response_model=list[TargetOut])
def list_targets_by_seller(seller_id: int, token: AuthDep):
    return TargetService.list_by_seller(seller_id)


@router.get("/{target_id}/achievement", response_model=TargetAchievement)
def get_achievement(target_id: int, token: AuthDep):
    result = TargetService.get_achievement(target_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Target not found")
    return result


@router.get("/{target_id}", response_model=TargetOut)
def get_target(target_id: int, token: AuthDep):
    target = TargetService.get_target(target_id)
    if not target:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Target not found")
    return target


@router.post("/", response_model=TargetOut, status_code=status.HTTP_201_CREATED)
def create_target(payload: TargetCreate, token: AuthDep):
    return TargetService.create_target(payload)


@router.patch("/{target_id}", response_model=TargetOut)
def update_target(target_id: int, payload: TargetUpdate, token: AuthDep):
    target = TargetService.update_target(target_id, payload)
    if not target:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Target not found")
    return target
