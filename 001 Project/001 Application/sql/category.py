from sqlalchemy import Column, String, Integer, ARRAY, ForeignKey
from base import Base
from sqlalchemy.orm import relationship, backref


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    filter_id = Column(Integer, ForeignKey('filters.id'))
    #name for invidual category
    name = Column(String, unique=True)
    #list with category used in list
    items = Column(ARRAY(String, dimensions=1))

    filter_ = relationship("FilterF", back_populates='categorys')

    def __init__(self, name, items):
        self.name = name
        self.items = items

    def __repr__(self):
        return f'name :{self.name}, items: {self.items}'
