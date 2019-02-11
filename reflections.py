import datetime

import pandas as pd
from my_python.myfirstlib import connect_to_postgres, connect_to_dremio
"""
my_python.myfirstlib is custom module for different connections
connect_to_postgres() returns sqlalchemy.engine
connect_to_dremio() returns pyodbc.connect("Driver='driver';
                                      ConnectionType=Direct;
                                      HOST='host';
                                      PORT='port';
                                      AuthenticationType=Plain;
                                      UID='username';
                                      PWD='password'",
                                      autocommit=True)
"""

# #########################################################
# Testing connection to PostgreSQL database using Dremio #
#########################################################
# with open('SF_dremio2.csv', 'w') as csv_file:
#     row_title = f"id,date_time,duration\n"
#     csv_file.write(row_title)
#     print("SF_dremio")
# for i in range(100):
#     start = datetime.datetime.now()
#     engine = connect_to_dremio()
#     sql = '''SELECT "Category", "Date", COUNT(*)
#             FROM postgresql.public."SFincidents"
#             WHERE "Time" BETWEEN '08:00' AND '22:00'
#             GROUP BY "Category", "Date"
#           '''
#     result = pd.read_sql(sql, engine)
#     with open('SF_dremio2.csv', 'a') as csv_file:
#         row = f"{i},{datetime.datetime.now()},{(datetime.datetime.now() - start).total_seconds()}\n"
#         csv_file.write(row)
#         print(row.replace("\n", ""))
#     del engine, result
#
# ##########################################################
# # Testing connection to PostgreSQL database using Python #
# ##########################################################
# with open('SF_python_sql2.csv', 'w') as csv_file:
#     row_title = f"id,date_time,duration\n"
#     csv_file.write(row_title)
#     print("SF_python_sql")
# for i in range(100):
#     start = datetime.datetime.now()
#     engine = connect_to_postgres()
#     sql = """
#     SELECT "Category", "Date", COUNT(*)
#     FROM public."SFincidents"
#     WHERE "Time" BETWEEN '08:00' AND '22:00'
#     GROUP BY "Category", "Date";
#      """
#     result = pd.read_sql(sql, engine)
#     with open('SF_python_sql2.csv', 'a') as csv_file:
#         row = f"{i},{datetime.datetime.now()},{(datetime.datetime.now() - start).total_seconds()}\n"
#         csv_file.write(row)
#         print(row.replace("\n", ""))
#     del engine, result

##########################################################
# Testing connection to PostgreSQL database using Pandas #
##########################################################
# with open('SF_pandas.csv2', 'w') as csv_file:
#     row_title = f"id,date_time,duration\n"
#     csv_file.write(row_title)
#     print("SF_pandas")
# for i in range(2):
#     start = datetime.datetime.now()
#     engine = connect_to_postgres()
#     result = pd.read_sql('SELECT * FROM public."SFincidents"', engine)
#     result = result[result.Time >= '08:00']
#     result = result[result.Time < '22:00']
#     result = result.drop(
#         ['IncidntNum', 'Descript', 'DayOfWeek', 'Time', 'PdDistrict', 'Resolution',
#          'Address', 'X', 'Y', 'Location', 'PdId', 'index_id'], axis=1)
#     result = result.groupby(['Category', 'Date']).count()
#     with open('SF_pandas2.csv', 'a') as csv_file:
#         row = f"{i},{datetime.datetime.now()},{(datetime.datetime.now() - start).total_seconds()}\n"
#         csv_file.write(row)
#         print(row.replace("\n", ""))
#     del engine, result

######################################################################
# Testing connection to PostgreSQL database using Dremio Reflections #
######################################################################
with open('SF_dremio_reflections3.csv', 'w') as csv_file:
    row_title = f"id,date_time,duration\n"
    csv_file.write(row_title)
    print("SF_dremio_reflections")
for i in range(100):
    start = datetime.datetime.now()
    engine = connect_to_dremio()
    sql = '''SELECT "Category", "Date", COUNT(*)
            FROM postgresql.public."SFincidents"
            WHERE "Time" BETWEEN '08:00' AND '22:00'
            GROUP BY "Category", "Date"
          '''
    result = pd.read_sql(sql, engine)
    with open('SF_dremio_reflections2.csv', 'a') as csv_file:
        row = f"{i},{datetime.datetime.now()},{(datetime.datetime.now() - start).total_seconds()}\n"
        csv_file.write(row)
        print(row.replace("\n", ""))
    del engine, result
