from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, ForeignKey,Integer, String, DateTime, Text,Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
#Create a Base class using declarative_base(). Used to
Base = declarative_base()
class Well(Base):
    __tablename__ = "wells"
    id = Column(Integer, primary_key=True, index=True,
    autoincrement = True)
    name = Column(String(45), nullable=False, unique=True)
    field = Column(String(20), unique=True, index=True)
    daily_productions = relationship("Daily_production", back_populates="wells")

class Daily_production(Base):
    __tablename__ = "daily_productions"
    id = Column(Integer, primary_key=True, index=True,
    autoincrement = True)
    production_date = Column(DateTime(),nullable=True, server_default=func.current_date())
    well_id = Column(Integer, ForeignKey("wells.id"))
    material_id = Column(Integer, ForeignKey("materials.id"))
    qte = Column(Float)
    wells = relationship("Well", back_populates="daily_productions")
    materials = relationship("Material", back_populates="daily_productions")

class Material(Base):
    __tablename__ = "materials"
    id = Column(Integer, primary_key=True, index=True,
    autoincrement = True)
    name = Column(String(20), nullable=False,unique=True)
    uom = Column(String(10), unique=True)
    daily_productions = relationship("Daily_production", back_populates="materials")
