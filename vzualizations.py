import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd


SF_dremio = pd.read_csv('SF_dremio2.csv')
SF_reflections = pd.read_csv('SF_dremio_reflections2.csv')
SF_pandas = pd.read_csv('SF_pandas.csv')
SF_postgres = pd.read_csv('SF_postgres.csv')
SF_python_sql = pd.read_csv('SF_python_sql2.csv')

SF_dremio_trace = go.Scatter(x=SF_dremio.index,
                             y=SF_dremio['duration'],
                             name='Dremio')
SF_reflections_trace = go.Scatter(x=SF_reflections.index,
                                  y=SF_reflections['duration'],
                                  name='Dremio Reflections')
SF_postgres_trace = go.Scatter(x=SF_postgres.index,
                               y=SF_postgres['duration'],
                               name='PostgreSQL pgAgent')
SF_pandas_race = go.Scatter(x=SF_pandas.index,
                            y=SF_pandas['duration'],
                            name='Pandas')
SF_python_sql_trace = go.Scatter(x=SF_python_sql.index,
                                 y=SF_python_sql['duration'],
                                 name='Python and SQL')

# py.plot([SF_dremio_trace,
#          SF_postgres_trace,
#          SF_reflections_trace,
#          SF_pandas_race,
#          SF_python_sql_trace])

py.plot([SF_dremio_trace,
         SF_postgres_trace,
         SF_reflections_trace,
         SF_python_sql_trace])
