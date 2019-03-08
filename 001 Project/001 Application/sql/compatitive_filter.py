from sqlalchemy import Column, String, Integer, ARRAY, ForeignKey
from base import Base
from sqlalchemy.orm import relationship, backref


class CompativeFilterf(Base):
    __tablename__ = 'compative_filterf'

    competitive_id = Column(Integer, ForeignKey('competitives.id'))
    filterf_id = Column(Integer, ForeignKey('filters.id'))

    compatitive = relationship('Competitive', backref='compatitive_filterf')
    filterf = relationship('FilterF', backref='filterf_compatitive')

    # def __init__(self, name, column_nr, columns):
    #     self.name = name
    #     self.column_nr = column_nr
    #     self.columns = columns
    #
    # def __repr__(self):
    #     return f'name :{self.name}, column_nr: {self.column_nr}, columns: {self.columns}'