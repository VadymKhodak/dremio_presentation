# -*- coding: koi8-r -*-
  

def xor(a=False, b=False):
    """
    This is "xor" function

    :param a: boolean
    :param b: boolean
    :return: True and True is False, False and False is False, True and False is True, False and True is True
    """

    if a:
        if b:
            return False
        else:
            return True
    elif b:
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
        x = input('%s' % arg)
        try:
            if type(int(x)) == int:
                break
        except ValueError:
                print('Retry to enter integer number')
    return int(x)


def get_str(arg=''):
    """
    This function  gets integer number

    :param arg: String that print in a line where enter a string (optional parameter)
    :return: integer number
    """

    while True:
        x = input('%s' % arg)
        try:
            if type(str(x)) == str:
                break
        except ValueError:
                print('Retry to enter string')
    return str(x)


def get_float(arg=''):
    """
    This function  gets float number

    :param arg: A string that prints in a line where to enter a number (optional parameter)
    :return: float number
    """

    while True:
        x = input('%s' % arg)
        try:
            if type(float(x)) == float:
                break
        except ValueError:
                print('Retry to enter float number')
    return float(x)


def connect_to_dremio():
    from connections import dremio_conn
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
    return connect(f"Driver={driver};ConnectionType=Direct;HOST={host};PORT={port};AuthenticationType=Plain;UID={uid};PWD={pwd}",autocommit=True)


def connect_to_postgres():
    from connections import postgres_conn
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
    from sqlalchemy import create_engine
    from connections import redshift_conn

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
    from connections import mysql_conn
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

    return create_engine(f'mysql://{username}:{password}@{host}/{database}', isolation_level="READ UNCOMMITTED")



def connect_to_mongodb():
    from connections import mongodb_conn
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