import pandas
import re

def add_virtual_column(df: pandas.DataFrame, role: str, new_column: str) -> pandas.DataFrame:

   valid_column = re.compile(r'^[A-Za-z_]+$')
   valid_operators = ['+', '-', '*']
   valid_role = re.compile('^[A-Za-z_\s+\-*]+$')


   #validate df
   for col in df.columns:
      if not valid_column.fullmatch(col):
         return pandas.DataFrame([])

   #validate characters in role
   if not valid_role.fullmatch(role):
      return pandas.DataFrame([])

   #tokenize and validate role
   parts = re.split(r'[\+\-\*]', role)
   for part in parts:
      column_name = part.strip()
      if not column_name or column_name not in df.columns:
         return pandas.DataFrame([])

   #validate new_column
   if not valid_column.fullmatch(new_column):
      return pandas.DataFrame([])


   return pandas.DataFrame([])