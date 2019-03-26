from sqlalchemy import Column, String, Integer, ForeignKey, Float, Numeric
from base import Base
from sqlalchemy.orm import relationship, backref


class Data(Base):
    __tablename__ = 'data'

    id = Column(Integer, primary_key=True)
    competitive_id = Column(Integer, ForeignKey('competitives.id', ondelete='CASCADE'))
    year = Column(Integer)
    month = Column(Integer)
    week_nr = Column(Integer)
    sector = Column(String)
    category = Column(String)
    sub_category = Column(String)
    product = Column(String)  #Produkt(4)
    trade = Column(String)    #Branza(I)
    category_2 = Column(String) #Kategoria(II)
    division = Column(String) #Dzail
    producer = Column(String)
    brand = Column(String)
    sub_brand = Column(String)
    film_code = Column(String)
    film_codenr = Column(String)
    media = Column(String)
    main_medium = Column(String) # glowne medium
    medium = Column(String) #medium
    publisher = Column(String) #wydawca nadawca
    periodicity = Column(String) #periodycznosc
    duration = Column(Integer)
    spot_class = Column(String) #spot reklamy
    form_advertising = Column(String) # forma reklamy
    page_type = Column(String) #typ strony
    emision_count = Column(Integer) #liczba emisji
    sum_str = Column(Float)
    cost = Column(Float)
    pt_off = Column(String)
    trp = Column(Float)
    trp30 = Column(Float)
    spcount = Column(Integer)
    channel_group = Column(String)
    channel_type = Column(String)
    wyprz = Column(String)
    upus = Column(String)
    rabat = Column(String)
    wyprz_upust_rabat = Column(String)

    competitive = relationship('Competitive', cascade="all, delete",
                               backref="datas")

    def __init__(self,
                 year,
                 month,
                 week_nr,
                 sector,
                 category,
                 sub_category,
                 product,
                 trade,
                 category_2,
                 division,
                 producer,
                 brand,
                 sub_brand,
                 film_code,
                 film_codenr,
                 media,
                 main_medium,
                 medium,
                 publisher,
                 periodicity,
                 duration,
                 spot_class,
                 form_advertising,
                 page_type,
                 emision_count,
                 sum_str,
                 cost,
                 pt_off,
                 trp,
                 trp30,
                 spcount,
                 channel_group,
                 channel_type,
                 wyprz,
                 upus,
                 rabat,
                 wyprz_upust_rabat,

                 ):

        self.year = year
        self.month = month
        self.week_nr = week_nr
        self.sector = sector
        self.category = category
        self.sub_category = sub_category
        self.product = product
        self.trade = trade
        self.category_2 = category_2
        self.division = division
        self.producer = producer
        self.brand = brand
        self.sub_brand = sub_brand
        self.film_code = film_code
        self.film_codenr = film_codenr
        self.media = media
        self.main_medium = main_medium
        self.medium = medium
        self.publisher = publisher
        self.periodicity = periodicity
        self.duration = duration
        self.spot_class = spot_class
        self.form_advertising = form_advertising
        self.page_type = page_type
        self.emision_count = emision_count
        self.sum_str = sum_str
        self.cost = cost
        self.pt_off = pt_off
        self.trp = trp
        self.trp30 = trp30
        self.spcount = spcount
        self.channel_group = channel_group
        self.channel_type = channel_type
        self.wyprz = wyprz
        self.upus = upus
        self.rabat = rabat
        self.wyprz_upust_rabat = wyprz_upust_rabat

    # def __repr__(self):
    #     return f'{self.year}, {self.month}, {self.producer}'
    #
    def values(self):
        return [self.year,
                self.month,
                self.week_nr,
                self.sector,
                self.category,
                self.sub_category,
                self.product,
                self.trade,
                self.category_2,
                self.division,
                self.producer,
                self.brand,
                self.sub_brand,
                self.film_code,
                self.film_codenr,
                self.media,
                self.main_medium,
                self.medium,
                self.publisher,
                self.periodicity,
                self.duration,
                self.spot_class,
                self.form_advertising,
                self.page_type,
                self.emision_count,
                self.sum_str,
                self.cost,
                self.pt_off,
                self.trp,
                self.trp30,
                self.spcount,
                self.channel_group,
                self.channel_type,
                self.wyprz,
                self.upus,
                self.rabat,
                self.wyprz_upust_rabat
               ]

