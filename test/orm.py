# coding=utf8
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine, Column, String, SmallInteger, ForeignKey
from sqlalchemy.orm import relation
from sqlalchemy.types import Integer
from sqlalchemy.types import DateTime

Base = declarative_base()

#klasy modeli
class Uzytkownik(Base):
	__tablename__ = "UZYTKOWNIK"

	id = Column(Integer(), primary_key = True)
	nazwa_uzytkownika = Column(String())

	def __repr__(self):
        	return "<Uzytkownik id:%s, nazwa_uzytkownika:%s>" % (self.id, self.nazwa_uzytkownika)

class EksperymentyDostep(Base):
	__tablename__ = "EKSPERYMENTY_DOSTEP"

	id = Column(Integer(), primary_key = True)
	id_uzytkownika = Column(Integer())
	sesja_id = Column(Integer())

	def __repr__(self):
        	return "<EksperymentyDostep id:%s, id_uzytkownika:%s, id_uzytkownika:%s>" % (self.id, self.id_uzytkownika, self.sesja_id)


class SesjaPomiarowa(Base):
	__tablename__ = "SESJA_POMIAROWA"
	
	id = Column(Integer(), primary_key = True)
	nazwa_id = Column(Integer())

	def __repr__(self):
        	return "<SesjaPomiarowa id:%s, nazwa_id:%s>" % (self.id, self.nazwa_id)


class Serie(Base):
	__tablename__ = "SERIE"

	id = Column(Integer(), primary_key = True)
	sesja_id = Column(Integer())
	data = Column(DateTime())
	wynik = Column(String())

	def __repr__(self):
        	return "<Serie id:%s, sesja_id:%s, data:%s, wynik:%s>" % (self.id, self.sesja_id, self.data, self.wynik)


class Eksperyment(Base):
	__tablename__ = "EKSPERYMENT"

	id = Column(Integer(), primary_key = True)
	nazwa = Column(String())

	def __repr__(self):
        	return "<Eksperyment id:%s, nazwa:%s>" % (self.id, self.nazwa)
