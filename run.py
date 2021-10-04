import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__),'SRC/'))
from SRC.etl import ETL

def main():
  etl_process = ETL()
  etl_process.read_files_and_populating_db()

if __name__ == '__main__':
    main()