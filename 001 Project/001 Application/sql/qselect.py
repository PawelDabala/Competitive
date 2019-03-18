from base import Session, engine, Base
from competitive import Competitive
from data import Data
from filterf import FilterF
from compatitive_filter import CompativeFilterf
from category import Category

session = Session()

# print(session.query(Competitive).all())
print(session.query(FilterF).filter_by(column_nr=31).one_or_none())