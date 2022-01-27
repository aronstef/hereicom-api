from typing import Any
import base64
import binascii

from fastapi import APIRouter, Depends, HTTPException, status

import models
import schemas
from api import deps


router = APIRouter()


@router.post("/chirpstack/oms", status_code=200)
def add_lora_frame(frame: schemas.ChirpstackUp,
                   api_key: models.ApiKey = Depends(deps.get_api_key)) -> Any:
    """
    Add a Raw LoRa Frame
    """
    frame = frame.dict()
    try:
        frame["dev_eui"] = base64.b64decode(frame["dev_eui"]).hex()
    except (binascii.Error) as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Could not decode devEUI",
        ) from exception
    try:
        frame["data"] = base64.b64decode(frame["data"]).hex()
    except (binascii.Error) as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Could not decode data",
        ) from exception
    frame["api_key_id"] = api_key.id
    frame["user_id"] = api_key.owner_id

    # TODO Parse OMS Frame

    return None
