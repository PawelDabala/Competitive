from sqlalchemy import Column, String, Integer
from base import Base
from sqlalchemy.orm import relationship, backref




class Competitive(Base):
    __tablename__ = 'competitives'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f'{self.name}'
