import settings
import orm
import datetime
import tester
import unittest
from sqlalchemy.exc import IntegrityError

__author__ = 'gp'


class CheckSchemaTestCase(tester.SchemaUnittest, unittest.TestCase):
    """
	Simple tests
    """
    def test_create_user(self):
	sess = settings.Session()
	raised_exception = False
	try:
		sess.add( orm.Uzytkownik( nazwa_uzytkownika = "gp") )
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
		sess.commit()	
		sess.add(orm.Serie(sesja_id = 1, data = "1/1/2001", wynik='{ "betaArray": {"value": [0, 1, 2], "pragma": "replace"}, "constants": {"value": [3.1415], "pragma": "append"}}'))
		sess.commit()
	except IntegrityError:
            raised_exception = True
        finally:
            sess.close()

        self.assertFalse(raised_exception)

    """
	Tests of plpython trigger
    """
    def test_pragma_single_replace(self):
	sess = settings.Session()
	expected_result = """{"betaArray":{"value":[1,2,3]}}"""	
	try:
		sess.add(orm.Serie(sesja_id = 1, data = "1/1/2001", wynik='{ "betaArray": {"value": [0, 1, 2], "pragma": "replace"}}'))
		sess.commit()	
		sess.add(orm.Serie(sesja_id = 1, data = "1/1/2001", wynik='{ "betaArray": {"value": [1, 2, 3], "pragma": "replace"}}'))
		sess.commit()
		result = sess.query(orm.Serie).first().wynik
		self.assertEquals( result, expected_result )
        finally:
            sess.close()

    def test_pragma_single_transient(self):
	sess = settings.Session()
	expected_result = """{"betaArray":{"value":[0,1,2]}}"""	
	try:
		sess.add(orm.Serie(sesja_id = 1, data = "1/1/2001", wynik='{ "betaArray": {"value": [0, 1, 2], "pragma": "replace"}}'))
		sess.commit()	
		sess.add(orm.Serie(sesja_id = 1, data = "1/1/2001", wynik='{ "betaArray": {"value": [1, 2, 3], "pragma": "transient"}}'))
		sess.commit()
		result = sess.query(orm.Serie).first().wynik
		self.assertEquals( result, expected_result )
        finally:
            sess.close()

    def test_pragma_single_append(self):
	sess = settings.Session()
	expected_result = """{"betaArray":{"value":[0,1,2]},"constants":{"value":[3.1415,3.1415]}}"""	
	try:
		sess.add(orm.Serie(sesja_id = 1, data = "1/1/2001", wynik='{ "betaArray": {"value": [0, 1, 2], "pragma": "replace"}, "constants": {"value": [3.1415], "pragma": "append"}}'))
		sess.commit()	
		sess.add(orm.Serie(sesja_id = 1, data = "1/1/2001", wynik='{ "betaArray": {"value": [0, 1, 2], "pragma": "replace"}, "constants": {"value": [3.1415], "pragma": "append"}}'))
		sess.commit()
		result = sess.query(orm.Serie).first().wynik
		self.assertEquals( result, expected_result )
        finally:
            sess.close()

    def test_pragma_multiple_replace(self):
	sess = settings.Session()
	expected_result = """{"betaArray":{"value":[0,1,2]}}"""	
	try:
		for i in xrange(0, 10):
			sess.add(orm.Serie(sesja_id = 1, data = "1/1/2001", wynik='{ "betaArray": {"value": [0, 1, 2], "pragma": "replace"}}'))
			sess.commit()	

		result = sess.query(orm.Serie).first().wynik
		self.assertEquals( result, expected_result )
        finally:
            sess.close()

    def test_pragma_multiple_transient(self):
	sess = settings.Session()
	expected_result = """{}"""	
	try:
		for i in xrange(0, 10):
			sess.add(orm.Serie(sesja_id = 1, data = "1/1/2001", wynik='{ "betaArray": {"value": [1, 2, 3], "pragma": "transient"}}'))
			sess.commit()

		result = sess.query(orm.Serie).first().wynik
		self.assertEquals( result, expected_result )
        finally:
            sess.close()

    def test_pragma_multiple_append(self):
	sess = settings.Session()
	expected_result = """{"betaArray":{"value":[0,1,2]},"constants":{"value":[3.1415,3.1415,3.1415]}}"""	
	try:
		for i in xrange(0,3):
			sess.add(orm.Serie(sesja_id = 1, data = "1/1/2001", wynik='{ "betaArray": {"value": [0, 1, 2], "pragma": "replace"}, "constants": {"value": [3.1415], "pragma": "append"}}'))
			sess.commit()
		result = sess.query(orm.Serie).first().wynik
		self.assertEquals( result, expected_result )
        finally:
            sess.close()



if __name__ == "__main__":
    unittest.main()
