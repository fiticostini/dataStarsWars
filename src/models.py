import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    email = Column(String(30), nullable=False, unique=True)
    username = Column(String(40), nullable=False, unique=True)
    password = Column(String(30), nullable=False)
    favorite = relationship('favorite')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    birth_year = Column(String(20), nullable=False)
    eye_color = Column(String(15), nullable=False)
    height = Column(String(15), nullable=False)
    origin = Column(String(25), nullable=False)


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surface = Column(String(20), nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(15), nullable=False)
    orbital_period = Column(String(25), nullable=False)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True, nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)

    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    character = relationship(Character)

    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    planet = relationship(Planet)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
