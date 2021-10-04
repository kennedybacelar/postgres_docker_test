import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))
from unittest import TestCase, main
from SRC import queries
from SRC.connection_db import ConnectionDB
import datetime

class TestDB(TestCase):

  @classmethod
  def setUpClass(cls):

    cls.table_names = ['users', 'user_interaction']

    cls.user_select_response = (3, '18-45', 'DE')
    cls.user_interaction_select_response = ('C301272F-1D61-01DB-4855-F2715E149D4F', 3, 'CLICK', datetime.datetime.strptime('2019-05-05 14:05:20', '%Y-%m-%d %H:%M:%S'))

    cls.conn = ConnectionDB().conn

  def test_select_db(self):

    list_of_select_responses = []
    for table_name in self.table_names:
      query = queries.select(table=table_name)
      curr = self.conn.cursor()
      curr.execute(query)
      records = curr.fetchall()
      list_of_select_responses.append(records[0])

    first_line_user = list_of_select_responses[0]
    first_line_u_interaction = list_of_select_responses[1]

    self.assertEqual(first_line_user, self.user_select_response)
    self.assertEqual(first_line_u_interaction, self.user_interaction_select_response)

if __name__ == '__main__':
  main()