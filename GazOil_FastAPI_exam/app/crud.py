from sqlalchemy.orm import Session
from . import models, schemas

def get_wells(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Well).offset(skip).limit(limit).all()

def get_materials(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Material).offset(skip).limit(limit).all()

def get_well(db: Session, well_id: int):
    return db.query(models.Well).filter(models.Well.id == well_id).first()

def get_material_by_name(db: Session, name: str):
    return db.query(models.Material).filter(models.Material.name == name).first()

def get_well_by_name(db: Session, name: str):
    return db.query(models.Well).filter(models.Well.name == name).first()

def get_productions_well(db:Session,well_id:int):
    return db.query(models.Daily_production).filter(models.Daily_production.well_id == well_id).all()

def create_well(db: Session, well: schemas.WellCreate):
    db_well = models.Well(name=well.name,field=well.field)
    # instance object added to database session
    db.add(db_well)
    # changes are saved to the database
    db.commit()
    # instance is refreshed to contain any new data from the database, like the generated ID
    db.refresh(db_well)
    return db_well


def create_material(db: Session, material: schemas.MaterialCreate):
    db_material = models.Material(name=material.name,uom=material.uom)
    # instance object added to database session
    db.add(db_material)
    # changes are saved to the database
    db.commit()
    # instance is refreshed to contain any new data from the database, like the generated ID
    db.refresh(db_material)
    return db_material

