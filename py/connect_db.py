from sqlalchemy import (create_engine, MetaData, Table, Column, ForeignKey, UniqueConstraint,
                        Integer, Float, String, DateTime, Date)
from sqlalchemy.orm import DeclarativeBase, mapped_column, sessionmaker
from datetime import date


class Base(DeclarativeBase):
    pass


class TinkoffTransaction(Base):
    __tablename__ = "tinkoff"
    
    pay_id = mapped_column(Integer, primary_key=True)
    bank = mapped_column(String)
    op_datetime = mapped_column(DateTime)
    pay_datetime = mapped_column(Date)
    card = mapped_column(String)
    status = mapped_column(String)
    op_sum = mapped_column(Float)
    op_currency = mapped_column(String)
    pay_sum = mapped_column(Float)
    pay_currency = mapped_column(String)
    cashback = mapped_column(String)
    category = mapped_column(String)
    mcc = mapped_column(String)
    description = mapped_column(String)
    bonus = mapped_column(Float)
    rounding = mapped_column(Float)
    sum_with_rounding = mapped_column(Float)
    debit = mapped_column(Float)
    credit = mapped_column(Float)
    load_date = mapped_column(Date, default=date.today())
    user = mapped_column(ForeignKey("users.user_id"))
    
    __table_args__ = (
       UniqueConstraint(
           'bank',
           'op_datetime',
           'card',
           'status',
           'debit',
           'credit',
           'op_currency',
           'pay_sum',
           'pay_currency',
           'category',
           'mcc'
       ),
    )


class User(Base):
    __tablename__ = "users"
    
    user_id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(30))


engine = create_engine('postgresql+psycopg2://postgres:_password_@_serveraddr_:_port_/_dbname_', echo=True)
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

session = Session()
session.commit()
