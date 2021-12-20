from pydantic import BaseModel


# Shared properties
class ApiKeyBase(BaseModel):
    apikey: str

# Properties to receive on apikey creation
class ApiKeyCreate(ApiKeyBase):
    pass


# Properties to receive on apikey update
class ApiKeyUpdate(ApiKeyBase):
    pass


# Properties shared by models stored in DB
class ApiKeyInDBBase(ApiKeyBase):
    id: int
    owner_id: int
    class Config:
        orm_mode = True


# Properties to return to client
class ApiKey(ApiKeyInDBBase):
    pass


# Properties properties stored in DB
class ApiKeyInDB(ApiKeyInDBBase):
    pass
