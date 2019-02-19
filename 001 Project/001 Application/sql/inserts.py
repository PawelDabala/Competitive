from base import Session, engine, Base
from competitive import Competitive

def generete_database_schema():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


session = Session()


def commit_():
    session.commit()
    session.close()


if __name__=="__main__":
    generete_database_schema()
