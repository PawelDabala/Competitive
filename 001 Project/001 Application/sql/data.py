from sqlalchemy import Column, String, Integer, ForeignKey
from base import Base
from sqlalchemy.orm import relationship, backref


class Data(Base):
    __tablename__ = 'data'

    id = Column(Integer, primary_key=True)
    competitive_id = Column(Integer, ForeignKey('competitives.id', ondelete='CASCADE'))
    year = Column(Integer)
    month = Column(Integer)
    producer = Column(String)
    film = Column(String)

    competitive = relationship('Competitive', cascade="all, delete",
                               backref="datas")

    def __init__(self, year, month, producer, film):
        self.year = year
        self.month = month
        self.producer = producer
        self.film = film

    def __repr__(self):
        return f'{self.year}, {self.month}, {self.producer}'

    def values(self):
        return [self.year, self.month, self.producer, self.film]

