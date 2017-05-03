from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker
from datetime import datetime, timedelta
import json

Base = declarative_base()


class Rate(Base):
    __tablename__ = 'rates'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    rate = Column(String, nullable=False)
    currency = Column(String, nullable=False)

    def __init__(self, date, currency, rate):
        self.date = date
        self.currency = currency
        self.rate = rate

    def getDict(self):
        return {
            'date': self.date.strftime("%Y-%m-%d"),
            'currency': self.currency,
            'rate': self.rate
        }

    def __repr__(self):
        return json.dumps(
            self.getDict(),
            sort_keys=True, indent=4, separators=(',', ': '))


class Database:
    engine = create_engine('sqlite:///rates.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    @classmethod
    def insert(cls, rates):
        for rate in rates:
            cls.session.add(rate)
        cls.session.commit()

    @classmethod
    def getRates(cls, date_from, date_to, curr):
        return cls.session.query(Rate)\
            .filter(
                Rate.currency == curr,
                Rate.date >= date_from,
                Rate.date <= date_to
                ).order_by(Rate.date).all()

    @classmethod
    def getLastRow(cls):
        return cls.session.query(Rate)\
            .order_by(desc(Rate.date))\
            .limit(1).all()


if __name__ == "__main__":
    Database.insert(
        [Rate(datetime.strptime('16Sep2012', '%d%b%Y'), "CZK", 0.1)])
    print(Database.getRates(
        datetime(2000, 1, 1), datetime(2001, 1, 1), "CZK"))
