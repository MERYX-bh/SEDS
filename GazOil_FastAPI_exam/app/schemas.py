from pydantic import BaseModel
import datetime
from typing import Optional

class WellBase(BaseModel):
    name: str
    field: str


class DailyProductionBase(BaseModel):
    production_date:datetime.datetime
    qte: float

class MaterialBase(BaseModel):
    name: str
    uom: str




class Well(WellBase):
    id: int
    class Config:
        orm_mode = True

class DailyProduction(DailyProductionBase):
    id: int
    well_id: int
    material_id: int
    class Config:
        orm_mode = True

class Material(MaterialBase):
    id: int
    class Config:
        orm_mode = True

class WellCreate(WellBase):
    daily_production: list[DailyProduction] = []
    pass

class MaterialCreate(MaterialBase):
    daily_production: list[DailyProduction] = []
    pass

class DailyProductionCreate(DailyProductionBase):
    daily_production: list[DailyProduction] = []
    pass

class WellsUpdate(WellBase):
    name: Optional[str] = None
    field: Optional[str] = None



