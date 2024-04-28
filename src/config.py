import pandas as pd
import sqlalchemy

credentials = {
  'user': 'WILLYWILSEN',
  'password': 'IF4044BigData',
  'account': 'trebcba-op98541',
  'warehouse': 'COMPUTE_WH',
  'database': 'UK_FLOODS',
  'schema': 'PUBLIC'
}
snowflake_engine = sqlalchemy.create_engine(f"snowflake://{credentials['user']}:{credentials['password']}@{credentials['account']}/{credentials['database']}/{credentials['schema']}?warehouse={credentials['warehouse']}")

df = pd.read_sql_query('SELECT * FROM UK_FLOODS.PUBLIC."flood_warning_levels"', snowflake_engine)
print(df)