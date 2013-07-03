import psycopg2
import unittest

class TestDataBase(unittest.TestCase):

	def setUp(self):
		conn = psycopg2.connect("dbname=ilf_json user=postgres")
		cur = conn.cursor()
		db_setup_script = open('schema.sql', 'r').read()
		cur.execute("""%s""", [db_setup_script])
		#conn.commit()

	def tearDown(self):
		pass
		#conn.close()

	def testSample(self):
		#sample_data_file = open('sample_data.sql', 'r')
		#cur.execute("""%s""", sample_data_file.read())
		#conn.commit()	
		#cur.execute('SELECT * from "WYNIKI"')
		#x = cur.fetchone()
		#print x
		self.assertFalse(2==1)	


	#if __name__ == '__main__':
suite = unittest.TestLoader().loadTestsFromTestCase(TestDataBase)
unittest.TextTestRunner(verbosity=2).run(suite)

