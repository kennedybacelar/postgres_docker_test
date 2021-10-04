def select(columns='*', table=None):
  return f'SELECT {columns} FROM {table}'


def insert(columns=None, table=None, values=None):
  if columns is None:
    return f'INSERT INTO {table} VALUES({values})'
  return f'INSERT INTO {table}({columns}) VALUES({values})'