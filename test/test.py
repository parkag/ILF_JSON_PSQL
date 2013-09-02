import settings
import orm
import datetime
import tester
import unittest
from sqlalchemy.exc import IntegrityError

__author__ = 'gp'

"""
sess = settings.Session()

orm.Base.metadata.create_all(settings.engine)
sess.close()
"""

class CheckSchemaTestCase(tester.SchemaUnittest, unittest.TestCase):

    def test_create_user(self):
	sess = settings.Session()
	raised_exception = False
	try:
		sess.add( orm.Uzytkownik( nazwa_uzytkownika = 'gp') )
		sess.add( orm.Uzytkownik(nazwa_uzytkownika = "jb") )
		sess.add( orm.Uzytkownik(nazwa_uzytkownika = "kowalcp4") )
		sess.commit()
        except IntegrityError:
            raised_exception = True
        finally:
            sess.close()

        self.assertFalse(raised_exception)


    def test_create_experiment_rights(self):
	sess = settings.Session()
	raised_exception = False		
	try:
		sess.add( orm.EksperymentyDostep(id_uzytkownika = 1, sesja_id = 1) )
		sess.add( orm.EksperymentyDostep(id_uzytkownika = 2, sesja_id = 2) )
		sess.add( orm.EksperymentyDostep(id_uzytkownika = 3, sesja_id = 3) )
		sess.add( orm.EksperymentyDostep(id_uzytkownika = 1, sesja_id = 4) )
		sess.add( orm.EksperymentyDostep(id_uzytkownika = 2, sesja_id = 4) )
		sess.commit()
        except IntegrityError:
            raised_exception = True
        finally:
            sess.close()

        self.assertFalse(raised_exception)


    def test_create_session(self):
	sess = settings.Session()
	raised_exception = False	
	try:
		sess.add( orm.SesjaPomiarowa(nazwa_id = 1) )
		sess.add( orm.SesjaPomiarowa(nazwa_id = 1) )
		sess.add( orm.SesjaPomiarowa(nazwa_id = 1) )
		sess.add( orm.SesjaPomiarowa(nazwa_id = 2) )
		sess.add( orm.SesjaPomiarowa(nazwa_id = 3) )
		sess.commit()        
	except IntegrityError:
            raised_exception = True
        finally:
            sess.close()

        self.assertFalse(raised_exception)


    def test_create_experiment(self):
	sess = settings.Session()
	raised_exception = False		
	try:
		sess.add( orm.Eksperyment(nazwa = 'EKSPERYMENT COMPTONA') ) 
		sess.add( orm.Eksperyment(nazwa = 'PRAWO OHMA') )
		sess.add( orm.Eksperyment(nazwa = 'OGNIWA PELTIERA') )
		sess.commit()        
	except IntegrityError:
            raised_exception = True
        finally:
            sess.close()

        self.assertFalse(raised_exception)


    def test_create_serie(self):
	sess = settings.Session()
	raised_exception = False	
	try:
		sess.add(orm.Serie(sesja_id = 1, data = "1/1/2001", wynik='{ "betaArray": {"value": [0, 1, 2], "pragma": "replace"}, "constants": {"value": [3.1415], "pragma": "append"}}'))
		sess.add(orm.Serie(sesja_id = 1, data = "1/1/2001", wynik='{ "betaArray": {"value": [0, 1, 2], "pragma": "replace"}, "constants": {"value": [3.1415], "pragma": "append"}}'))
		sess.commit()		
	except IntegrityError:
            raised_exception = True
        finally:
            sess.close()

        self.assertFalse(raised_exception)


"""
sess.commit()
sess.flush()
print( sess.query(orm.Uzytkownik).all() )
print "\n"
print( sess.query(orm.Eksperyment).all() )
print "\n"
print( sess.query(orm.Serie).all() )
print "\n"


sess.close()
"""

if __name__ == "__main__":
    unittest.main()
