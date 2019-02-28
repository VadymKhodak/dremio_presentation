# -*- coding: koi8-r -*-
"""
Simple module that has functions:
    xor(first=False, second=False)
    get_int(arg='')
    get_str(arg='')
    get_float(arg='')
    connect_to_dremio()
    connect_to_postgres()
    connect_to_redshift()
    connect_to_mysql()
    connect_to_mongodb()
"""


def xor(first=False, second=False):
    """
    This is "xor" function

    :param first: boolean
    :param second: boolean
    :return: True and True is False, False and False is False,
             True and False is True, False and True is True
    """

    if first:
        if second:
            return False
        else:
            return True
    elif second:
        return True
    else:
        return False


def get_int(arg=''):
    """
    This function  gets integer number

    :param arg: String that print in a line where enter a number (optional parameter)
    :return: integer number
    """

    while True:
        integer_number = input('%s' % arg)
        try:
            if type(int(integer_number)) is int:
                break
        except ValueError:
            print('Retry to enter integer number')
    return int(integer_number)


def get_str(arg=''):
    """
    This function  gets integer number

    :param arg: String that print in a line where enter a string (optional parameter)
    :return: integer number
    """

    while True:
        string = input('%s' % arg)
        try:
            if type(str(string)) is str:
                break
        except ValueError:
            print('Retry to enter string')
    return str(string)


def get_float(arg=''):
    """
    This function  gets float number

    :param arg: A string that prints in a line where to enter a number (optional parameter)
    :return: float number
    """

    while True:
        float_number = input('%s' % arg)
        try:
            if type(float(float_number)) is float:
                break
        except ValueError:
            print('Retry to enter float number')
    return float(float_number)


def connect_to_dremio():
    """
    Function to create connection to Dremio using ODBC

    :return: pyodbc.connect
    """

    from my_python.connections import dremio_conn
    from pyodbc import connect

    try:
        host = dremio_conn["host"]
    except KeyError:
        host = input("Host: ")
    try:
        port = dremio_conn["port"]
    except KeyError:
        port = input("Port: ")
    try:
        uid = dremio_conn["uid"]
    except KeyError:
        uid = input("User name: ")
    try:
        pwd = dremio_conn["pwd"]
    except KeyError:
        pwd = input("Password: ")
    try:
        driver = dremio_conn["driver"]
    except KeyError:
        driver = input("Driver: ")
    return connect(f"Driver={driver};"
                   f"ConnectionType=Direct;"
                   f"HOST={host};"
                   f"PORT={port};"
                   f"AuthenticationType=Plain;"
                   f"UID={uid};"
                   f"PWD={pwd}",
                   autocommit=True)


def connect_to_postgres():
    """
    Function to create connection to PostgreSQL database using sqlalchemy.
    Function try to read file connections with connection data.

    :return: sqlalchemy.create_engine
    """

    from my_python.connections import postgres_conn
    from sqlalchemy import create_engine

    try:
        host = postgres_conn["host"]
    except KeyError:
        host = input("Host: ")
    try:
        database = postgres_conn["database"]
    except KeyError:
        host = input("Database: ")
    try:
        username = postgres_conn["username"]
    except KeyError:
        username = input("User name: ")
    try:
        password = postgres_conn["password"]
    except KeyError:
        password = input("Password: ")

    return create_engine(f'postgresql://{username}:{password}@{host}/{database}')


def connect_to_redshift():
    """
    Function to create connection to Redshit database using sqlalchemy.
    Function try to read file connections with connection data.

    :return: sqlalchemy.create_engine
    """

    from sqlalchemy import create_engine
    from my_python.connections import redshift_conn

    try:
        host = redshift_conn['host']
    except KeyError:
        host = input("Host: ")
    try:
        port = redshift_conn['port']
    except KeyError:
        port = input("Port: ")
    try:
        user = redshift_conn['user']
    except KeyError:
        user = input("User: ")
    try:
        password = redshift_conn['password']
    except KeyError:
        password = input("Password: ")
    try:
        dbname = redshift_conn['dbname']
    except KeyError:
        dbname = input("Database: ")
    return create_engine(f'redshift+psycopg2://{user}:{password}@{host}:{port}/{dbname}')


def connect_to_mysql():
    """
    Function to create connection to MySQL database using sqlalchemy.
    Function try to read file connections with connection data.

    :return: sqlalchemy.create_engine
    """

    from my_python.connections import mysql_conn
    from sqlalchemy import create_engine
    try:
        host = mysql_conn["host"]
    except KeyError:
        host = input("Host: ")
    try:
        database = mysql_conn["database"]
    except KeyError:
        database = input("Database: ")
    try:
        username = mysql_conn["username"]
    except KeyError:
        username = input("User name: ")
    try:
        password = mysql_conn["password"]
    except KeyError:
        password = input("Password: ")

    return create_engine(f'mysql://{username}:{password}@{host}/{database}',
                         isolation_level="READ UNCOMMITTED")


def connect_to_mongodb():
    """
    Function to create connection to MongoDB database using pymongo.
    Function try to read file connections with connection data.

    :return: pymongo.MongoClient(host, int(port))[database][collection]
    """

    from my_python.connections import mongodb_conn
    import pymongo
    try:
        host = mongodb_conn['host']
    except KeyError:
        host = input("Host: ")
    try:
        port = mongodb_conn['port']
    except KeyError:
        port = input("Port: ")
    try:
        database = mongodb_conn['database']
    except KeyError:
        database = input("Database: ")
    try:
        collection = mongodb_conn['collection']
    except KeyError:
        collection = input("Collection: ")

    client = pymongo.MongoClient(host, int(port))
    return client[database][collection]
