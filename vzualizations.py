import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd


SF_dremio = pd.read_csv('SF_dremio.csv')
SF_dremio_reflections = pd.read_csv('SF_dremio_reflections.csv')
SF_pandas = pd.read_csv('SF_pandas.csv')
SF_postgres = pd.read_csv('SF_postgres.csv')
SF_python_sql = pd.read_csv('SF_python_sql.csv')

SF_dremio_trace = go.Scatter(x=SF_dremio.index,
                             y=SF_dremio['duration'],
                             name='Dremio')
SF_dremio_reflections_trace = go.Scatter(x=SF_dremio_reflections.index,
                                         y=SF_dremio_reflections['duration'],
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


def plot_all():
    py.plot([SF_dremio_trace, SF_postgres_trace,
             SF_dremio_reflections_trace,
             SF_pandas_race, SF_python_sql_trace])


def plot_extend_sf_pandas():
    py.plot([SF_dremio_trace,
             SF_postgres_trace,
             SF_dremio_reflections_trace,
             SF_python_sql_trace])


plot_extend_sf_pandas()
plot_all()
