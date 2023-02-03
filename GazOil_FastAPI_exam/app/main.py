from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import json

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 

#Get wells method
@app.get("/wells", response_model=list[schemas.Well])
async def get_wells(skip: int = 0, limit: int = 100, db: Session =Depends(get_db)):
    wells = crud.get_wells(db, skip=skip, limit=limit)
    return wells

#Get one well method by ID
@app.get("/wells/{well_id}", response_model=schemas.Well)
async def get_well_by_id(well_id: int, db: Session = Depends(get_db)):
    db_well = crud.get_well(db, well_id=well_id)
    if db_well is None:
        raise HTTPException(status_code=404, detail="well not found")
    return db_well

#Get materials method
@app.get("/materials", response_model=list[schemas.Material])
async def get_materials(skip: int = 0, limit: int = 100, db: Session =Depends(get_db)):
    materials = crud.get_materials(db, skip=skip, limit=limit)
    return materials

#Get materials by name method
@app.get("/materials/{name}", response_model=schemas.Material)
async def get_material_by_name(name:str, db: Session = Depends(get_db)):
    db_material = crud.get_material_by_name(db, name)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material

#Get productions for a specific well id
@app.get("/productions/wells/{well_id}", response_model=schemas.Well)
async def get_well_by_productions(well_id: int, db: Session = Depends(get_db)):
    db_well = crud.get_well(db, well_id=well_id)
    if db_well is None:
        raise HTTPException(status_code=404, detail="well not found")
    prod_wells = crud.get_productions_well(db, well_id=well_id)
    return prod_wells


@app.post("/wells/new", response_model=schemas.Well)
async def create_well(well: schemas.WellCreate, db: Session =Depends(get_db)):
    db_well = crud.get_well_by_name(db, name=well.name)
    if db_well:
        raise HTTPException(status_code=400, detail="Well already exist")
    well = crud.create_well(db=db, well=well)
    if well.field not in ["CENTER","NORTH","SOUTH"]:
        raise HTTPException(status_code=400, detail="this field is not okey")
    else:
        return well
    

@app.post("/materials/new", response_model=schemas.Material)
async def create_material(material: schemas.MaterialCreate, db: Session =Depends(get_db)):
    db_material = crud.get_material_by_name(db, name=material.name)
    if db_material:
        raise HTTPException(status_code=400, detail="material already exist")
    material = crud.create_material(db=db, material=material)
    if material.uom not in ["M3","Tonne"]:
        raise HTTPException(status_code=400, detail="this material is not okey")
    else:
        return material


#Update well
@app.put("/wells/update/{well_id}", response_model=schemas.Well)
async def update_well(well:schemas.WellsUpdate,well_id: int,db:Session =Depends(get_db)):
    db_well = crud.get_well(db, well_id=well_id)
    if db_well is None:
        raise HTTPException(status_code=404, detail="Well not found")
    well_data = well.dict(exclude_unset=True)
    #User data :pour récupérer les éléments  (key,value)
    for key, value in well_data.items():
        setattr(db_well, key, value)
    db.add(db_well)
    db.commit()
    db.refresh(db_well)
    return db_well

#Template
templates = Jinja2Templates(directory="templates")
@app.get("/wells_interface")
async def home(request: Request,skip: int = 0, limit: int = 100, db: Session =Depends(get_db)):
    df = crud.get_wells(db, skip=skip, limit=limit)
    return templates.TemplateResponse("/wells.html",
    {"request":request, 
    "wells":df })


