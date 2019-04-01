from base import Session, engine, Base
from competitive import Competitive
from data import Data
from filterf import FilterF
from compatitive_filter import CompativeFilterf
from category import Category
from sqlalchemy import and_

session = Session()

# print(session.query(Competitive).all())
# print(session.query(FilterF).filter_by(column_nr=31).one_or_none())
# c1 = Category('C1', [])
# c2 = Category('C2', [])
# c3 = Category('C3', [])
#
# session.add(c1)
# session.add(c2)
# session.add(c3)
#
# session.commit()

c1 = session.query(Category).get(4)
c2 = session.query(Category).get(5)
c3 = session.query(Category).get(6)
#
# f = FilterF('Filter1', 1, [1, 2])
# f.categorys.extend((c1, c2, c3))
# session.commit()

# session.query(FilterF).filter_by(id=2).delete()
# session.commit()
#
# f1 = session.query(FilterF).filter_by(id=3).one()
# f1.categorys.extend((c1, c2, c3))
# session.commit()

#JAK USUNAC ELEMENTY W TABLICY
# delete_q = Category.__table__.delete().where(Category.filter_id == 3)
# session.execute(delete_q)
# session.commit()

# session = Session()
# filter_ = session.query(FilterF).get(1)
# # print(filter_.categorys)
# for cat in filter_.categorys:
#     print(cat.name)
#     print(cat.items)
# compative_name = 'nowy3'
#
# # compativedata = session.query(Competitive).filter(Competitive.name.ilike(f'{compative_name}%')).all()
# compativedata = session.query(Competitive).filter_by(name = compative_name).first()
# print(compativedata)

# filters = session.query(FilterF).filter_by(type='auto').all()
# if len(filters) > 0:
#     print(filters)

# data_filter = session.query(Data).all()
# print(data_filter)


com_fil = session.query(Competitive).filter_by(name='query').one()
print(com_fil)

data_filter = session.query(Data).filter_by(competitive_id=com_fil.id)
# print(data_filter)

from sqlalchemy import text
from sqlalchemy import union_all, intersect_all
# week1 = "week_nr=1"
# data_filter_w1 = session.query(Data).filter(text("week_nr=1"))
# print(data_filter_w1)
#
# las = data_filter.intersect_all(data_filter_w1).all()

# for la in las:
#     print(la.week_nr)

# print(set([la.week_nr for la in las]))

# week_two = session.query(Data).filter(Data.week_nr.in_([1, 50])).all()
# print([la.week_nr for la in week_two])
# zrobi combo box z disting do zaznaczenia danych
#
# year
# month
# week_nr
# prorucer

#wybieram compative
com_fil = session.query(Competitive).filter_by(name='query').one()
data_id = session.query(Data).filter_by(competitive_id=com_fil.id)

#funkcja przeliczajaca pola kombi
year_nr = [2018]
data_year = session.query(Data).filter(Data.year.in_(year_nr))

month_nr = [12]
month_ = session.query(Data).filter(Data.month.in_(month_nr))

week_nr = [1, 48]
week_ = session.query(Data).filter(Data.week_nr.in_(week_nr))

producer = ['Fiat', 'Opel']
producer_ = session.query(Data).filter(Data.producer.in_(producer))

result = data_id.intersect_all(data_year, month_, week_, producer_).all()
print(len(result))
print(result[0].competitive_id)











