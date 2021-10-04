import sys, os
import queries
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))
from connection_db import ConnectionDB

class ETL:

  def __init__(self):
    """
    attributes - dictionary format { table_name : file_name }
    """
    self.table_file_info = { 
      'users' : 'DATA/users.csv',
      'user_interaction' : 'DATA/user_interaction.csv'
    }

    self.db_connection = ConnectionDB()
  

  def read_files_and_populating_db(self):

    for table_name, file_name in self.table_file_info.items():

      with open(file_name, 'r') as csv_file:
        for line in csv_file.readlines():
          try:
            query = queries.insert(table=table_name, values=line.replace('\n', ''))
            self.db_connection.insert(query)
          except Exception as error:
            pass

    return None