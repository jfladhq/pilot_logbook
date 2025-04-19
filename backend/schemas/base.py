from pydantic import BaseModel


class Base(BaseModel):
    class Config:
        pass
        from_attributes = True
        #orm_mode = True
