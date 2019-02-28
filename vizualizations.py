"""
Built graphs using plotly library
"""

import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd

SF_DREMIO = pd.read_csv(f'SF_dremio.csv')
SF_REFLECTIONS = pd.read_csv('SF_dremio_reflections.csv')
SF_PANDAS = pd.read_csv('SF_pandas.csv')
SF_POSTGRES = pd.read_csv('SF_postgres.csv')
SF_PYTHON_SQL = pd.read_csv('SF_python_sql.csv')

SF_DREMIO_TRACE = go.Scatter(x=SF_DREMIO.index,
                             y=SF_DREMIO['duration'],
                             name='Dremio')
SF_REFLECTIONS_TRACE = go.Scatter(x=SF_REFLECTIONS.index,
                                  y=SF_REFLECTIONS['duration'],
                                  name='Dremio Reflections')
SF_POSTGRES_TRACE = go.Scatter(x=SF_POSTGRES.index,
                               y=SF_POSTGRES['duration'],
                               name='PostgreSQL pgAgent')
SF_PANDAS_TRACE = go.Scatter(x=SF_PANDAS.index,
                             y=SF_PANDAS['duration'],
                             name='Pandas')
SF_PYTHON_SQL_TRACE = go.Scatter(x=SF_PYTHON_SQL.index,
                                 y=SF_PYTHON_SQL['duration'],
                                 name='Python and SQL')

py.plot([SF_DREMIO_TRACE,
         SF_POSTGRES_TRACE,
         SF_REFLECTIONS_TRACE,
         SF_PANDAS_TRACE,
         SF_PYTHON_SQL_TRACE])
