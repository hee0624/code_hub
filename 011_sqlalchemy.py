#!/usr/bin/env python
# coding=utf-8
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.orm import sessionmaker


#engine = create_engine('mysql+mysqldb://root:chenhe1993@127.0.0.1:3306/ssb',echo=False)
engine = create_engine('mysql://root:chenhe1993@127.0.0.1:3306/ssb',echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    fullname = Column(String(32))
    password = Column(String(64))
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)


    def __repr__(self):
        return "<User(name='%s', fullname='%s')>" % (self.name, self.fullname)


def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)


if __name__ == '__main__':

    #session.add(
    #    User(name='lirui', fullname='chenhe', password='123')
    #    )
    session.query(User).filter(User.name=='lirui').update({User.name:'liruisd'})
    session.commit()


