from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.apikey import ApiKey
from schemas.apikey import ApiKeyCreate, ApiKeyUpdate


class CRUDApiKey(CRUDBase[ApiKey, ApiKeyCreate, ApiKeyUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: ApiKeyCreate, owner_id: int
    ) -> ApiKey:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[ApiKey]:
        return (
            db.query(self.model)
            .filter(ApiKey.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_from_apikey(self, db: Session, *, apikey: str) -> ApiKey:
        return db.query(self.model).filter(ApiKey.apikey == apikey).one_or_none()


apikey = CRUDApiKey(ApiKey)
