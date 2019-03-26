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

filters = session.query(FilterF).filter_by(type='auto').all()
if len(filters) > 0:
    print(filters)


