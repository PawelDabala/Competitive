from base import Session, engine, Base
from competitive import Competitive

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


if __name__=="__main__":
    # generete_database_schema()
    # add_competitive()
    # commit_()
