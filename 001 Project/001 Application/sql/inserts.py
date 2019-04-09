from base import Session, engine, Base
from competitive import Competitive
from data import Data
from filterf import FilterF
from compatitive_filter import CompativeFilterf
from category import Category

from sqlalchemy import func
from mydictionary import MakeDictionary

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
    name1.datas.append(Data(2019,11,"Audi","Stary film"))
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

def dalate_in_data():
    comat = session.query(Competitive).filter(Competitive.name.ilike('%name1%')).first()
    data1 = session.query(Data).filter_by(competitive_id=comat.id).delete()
    print(data1)

def columns_names():
    session = Session()
    q = session.query(Data)
    print(q.column_descriptions)

def add_filter():
    f1 = FilterF('Channel', 3, (1,2))
    f2 = FilterF('Channel2', 6, (4,5))
    session.add(f1)
    session.add(f2)

def c_filters():
    c = session.query(Competitive).get(1)
    # print(c)
    # f1 = session.query(FilterF).get(1)
    # f2 = session.query(FilterF).get(2)
    # c.filters_.append(f1)
    # c.filters_.append(f2)
    print(c.filters_)

def add_category():
    cat1 = Category("TVN", ('TVN Style', 'TVN 24'))
    cat2 = Category('TVP', ('TVP 1', 'TVP 2'))
    cat3 = Category('Polast Tematyczne', (['2017', 'th Street Universal Hallmark']))
    # session.add(cat1)
    # session.add(cat2)
    session.add(cat3)

def join_filter_category():
    f1 = session.query(FilterF).get(3)
    print(f1)
    cat1 = session.query(Category).get(1)
    cat2 = session.query(Category).get(2)

    f1.categorys.append(cat1)
    f1.categorys.append(cat2)

    print(f1.categorys)

def add_filter():

    """
    nie kasowac tej funkcji !!!!
    :return:
    """

    """
    manual filters
    """
    channelgroup = FilterF("channelgroup", 30, (0,17), 'manual')

    brand_final = FilterF('brand_final', 37, [11], 'manual')
    #dane z kolumn brand final
    brand_type = FilterF('brand_type', 39, [37], 'manual')
    segment_detailed = FilterF('segment_detailed', 40, [38], 'manual')
    segment = FilterF('segment', 41, [40], 'manual')
    segment_combined = FilterF('segment_combined', 42, [40], 'manual')
    campaign_type = FilterF('campaign_type', 43, [13], 'manual')

    """
    words
    """

    wyprz = FilterF('WYPRZ', 32, [13], 'words')
    wyprz_cat = Category('WYPZ', words=['wyprz'])
    wyprz.categorys.append(wyprz_cat)

    upus = FilterF('UPUS', 33, [13], 'words')
    upus_cat = Category('UPUS', words=['upus'])
    upus.categorys.append(upus_cat)

    rabat = FilterF('RABAT', 34, [13], 'words')
    rabat_cat = Category('RABAT', words=['rabat '])
    rabat.categorys.append(rabat_cat)

    wy_up_rab = FilterF('WY_UP_RAB', 35, [32, 33, 36], 'words')
    wy_up_rab_cat = Category('WY_UP_RAB', words=['wyprz', 'upus', 'rabat'])
    wy_up_rab.categorys.append(wy_up_rab_cat)

    """
    cut filter
    """
    # Brand 'Sub Brand' obcina pierwsze słowo z slownika
    modelf = FilterF('model', 36, [11, 12], 'cut') # Brand 'Sub Brand'

    #Subbrand (brand+model)
    # Useing Model, Brand Final; conectinc word from both cells
    subbrand_brand_model = FilterF('subbrand_brand_model', 38, [37, 36], 'cut')



    session.add_all([channelgroup,
                     brand_final,
                     wyprz,
                     upus,
                     rabat,
                     wy_up_rab,
                     modelf,
                     subbrand_brand_model,
                     brand_type,
                     segment_detailed,
                     segment,
                     segment_combined,
                     campaign_type
                     ])

def set_auto_filters():

    #Sub Category uspojnienie
    # dic = MakeDictionary("slowniki.xlsx", 'Sub Category uspojnienie').set_dictionary()
    # fil = FilterF('Test', 3, [2,3], 'manual')
    # __set_categorys(dic)

    #sub Stacje
    channelgroup = session.query(FilterF).filter_by(name="channelgroup").one()
    dic = MakeDictionary("slowniki.xlsx", 'Stacje').set_multi_row_dictionary()
    __set_categorys(dic, channelgroup)

    #sub Brand_Final
    brand_final = session.query(FilterF).filter_by(name='brand_final').one()
    dic = MakeDictionary('slowniki.xlsx', 'brand_uspione').set_dictionary()
    __set_categorys(dic, brand_final)

    #sub brand type
    brand_type = session.query(FilterF).filter_by(name='brand_type').one()
    dic = MakeDictionary('slowniki.xlsx', 'brand_type').set_dictionary()
    __set_categorys(dic, brand_type)

    #segment detailed
    segment_detailed = session.query(FilterF).filter_by(name='segment_detailed').one()
    dic = MakeDictionary('slowniki.xlsx', 'segment_detailed').set_dictionary()
    __set_categorys(dic, segment_detailed)

    # segment
    segment = session.query(FilterF).filter_by(name='segment').one()
    dic = MakeDictionary('slowniki.xlsx', 'segment').set_dictionary()
    __set_categorys(dic, segment)

    #segment_combined
    segment_combined = session.query(FilterF).filter_by(name='segment_combined').one()
    dic = MakeDictionary('slowniki.xlsx', 'segment_combined').set_dictionary()
    __set_categorys(dic, segment_combined)

    #campaign type
    campaign_type = session.query(FilterF).filter_by(name='campaign_type').one()
    dic = MakeDictionary('slowniki.xlsx', 'campaign_type').set_dictionary()
    __set_categorys(dic, campaign_type)


def __set_categorys(dic, fil=None):

    for key, value in dic.items():
        cat = Category(key, items=value)
        if fil:
            fil.categorys.append(cat)
            session.add(fil)
        else:
            session.add(cat)


def check_er_all():
    rezults = session.query(func.count(Competitive.id))
    print(rezults)

if __name__=="__main__":
    generete_database_schema()
    add_filter()
    set_auto_filters()
    commit_()
