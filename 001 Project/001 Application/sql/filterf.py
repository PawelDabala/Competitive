from sqlalchemy import Column, String, Integer, ARRAY
from base import Base
from sqlalchemy.orm import relationship, backref


class FilterF(Base):
    __tablename__ = 'filters'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    # column where initialize filter
    column_nr = Column(Integer, unique=True)
    # list with column used in filter
    columns = Column(ARRAY(Integer, dimensions=1))
    #what type is the filter (manual, words, cut)
    type = Column(String)

    competitives_ = relationship('Competitive', secondary='compative_filterf', back_populates='filters_')
    categorys = relationship('Category', back_populates='filter_')

    def __init__(self, name, column_nr, columns, type):
        self.name = name
        self.column_nr = column_nr
        self.columns = columns
        self.type = type

    def __repr__(self):
        return f'name :{self.name}, column_nr: {self.column_nr}, columns: {self.columns}, type: {self.type}'
