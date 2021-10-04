import psycopg2, os

class ConnectionDB:
  def __init__(self): 
    self._conn()

  @classmethod
  def _conn(self):
    self.conn = psycopg2.connect(
      database = os.getenv('POSTGRES_DB'),
      user = os.getenv('POSTGRES_USER'),
      port=5432, 
      host='data_psql',
      password=os.getenv('POSTGRES_PASSWORD')
      )
    self.conn.autocommit = True
    return self.conn
  
  def insert(self, insert_query):
    with self.conn.cursor() as curr:
      curr.execute(insert_query)
    return None
  
  def select(self, select_query):
    with self.conn.cursor() as curr:
      curr.execute(select_query)
      records = curr.fetchall()
    return records