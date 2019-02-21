from base import Session, engine, Base
from competitive import Competitive
from data import Data

def generete_database_schema():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

session = Session()

def commit_():
    session.commit()
    session.close()


def add_competitive():
    name1 = Competitive("name 1")
    session.add(name1)

def read_competive():
    competi = session.query(Competitive).all()
    print(competi)

def add_new_competiv_and_data():
    name1 = Competitive("name1")
    data1 = Data(2018,12,"BMW","Fajny film")
    data2 = Data(2019,11,"Audi","Stary film")
    name1.datas.append(data1)
    name1.datas.append(data2)
    session.add(name1)

def delete_competititve():
    # name = session.query(Competitive).filter_by(id=1).one()
    # print(name)
    # session.delete(name)

    session.query(Competitive).filter(Competitive.id==1).delete()
    session.commit()

def test_pobierz():
    comat = session.query(Competitive).filter(Competitive.name.ilike('%name1%')).scalar()
    if comat:
        print(comat.datas)
        print(comat.datas[0].year)
        l1 = list(comat.datas)
        print(l1)
        for row in comat.datas:
            print(row)


if __name__=="__main__":
    # generete_database_schema()
    # add_competitive()
    # add_new_competiv_and_data()
    #delete_competititve()
    # commit_()
    # read_competive()
    test_pobierz()
