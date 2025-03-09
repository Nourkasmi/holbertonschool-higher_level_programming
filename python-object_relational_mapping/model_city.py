#!/usr/bin/python3
"""
Defines a City class mapped to the cities table in MySQL.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base  # Import Base from model_state.py


class City(Base):
    """
    Represents a city in the MySQL table `cities`.
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
