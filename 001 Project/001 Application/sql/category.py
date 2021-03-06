from sqlalchemy import Column, String, Integer, ARRAY, ForeignKey
from base import Base
from sqlalchemy.orm import relationship, backref


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    filter_id = Column(Integer, ForeignKey('filters.id', ondelete='CASCADE'))
    #name for invidual category
    name = Column(String)
    #list with category used in list
    items = Column(ARRAY(String, dimensions=1))
    #words use when word search is required
    words = Column(ARRAY(String, dimensions=1))

    filter_ = relationship("FilterF", cascade="all, delete", back_populates='categorys')

    def __init__(self, name, items=[], words=None):
        self.name = name
        self.items = items
        self.words = words

    def __repr__(self):
        return f'name :{self.name}, items: {self.items}, words: {self.words}'
