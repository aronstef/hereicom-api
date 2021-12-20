from typing import Any, List
from pydantic import BaseModel

from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session

import crud, models, schemas
from api import deps


router = APIRouter()


# @router.get("/", response_model=List[apikey.ApiKey])
# def read_apikeys(
#     db: Session = Depends(deps.get_db),
#     skip: int = 0,
#     limit: int = 100,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Retrieve apikeys.
#     """
#     if crud.user.is_superuser(current_user):
#         apikeys = crud.apikey.get_multi(db, skip=skip, limit=limit)
#     else:
#         apikeys = crud.apikey.get_multi_by_owner(
#             db=db, owner_id=current_user.id, skip=skip, limit=limit
#         )
#     return apikeys


@router.post("/chirpstack")
def add_lora_frame(*, data=Body(...), db: Session = Depends(deps.get_db), api_key: models.ApiKey = Depends(deps.get_api_key)) -> Any:
    """
    Add a Raw LoRa Frame
    """
    return data


# @router.put("/{id}", response_model=schemas.ApiKey)
# def update_apikey(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Update an apikey.
#     """
#     apikey = crud.apikey.get(db=db, id=id)
#     if not apikey:
#         raise HTTPException(status_code=404, detail="apikey not found")
#     if not crud.user.is_superuser(current_user) and (apikey.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     apikey_in = schemas.ApiKeyCreate(apikey=create_api_key())
#     apikey = crud.apikey.update(db=db, db_obj=apikey, obj_in=apikey_in)
#     return apikey


# @router.get("/{id}", response_model=schemas.ApiKey)
# def read_apikey(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Get apikey by ID.
#     """
#     apikey = crud.apikey.get(db=db, id=id)
#     if not apikey:
#         raise HTTPException(status_code=404, detail="apikey not found")
#     if not crud.user.is_superuser(current_user) and (apikey.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     return apikey


# @router.delete("/{id}", response_model=schemas.ApiKey)
# def delete_apikey(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Delete an apikey.
#     """
#     apikey = crud.apikey.get(db=db, id=id)
#     if not apikey:
#         raise HTTPException(status_code=404, detail="apikey not found")
#     if not crud.user.is_superuser(current_user) and (apikey.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     apikey = crud.apikey.remove(db=db, id=id)
#     return apikey
