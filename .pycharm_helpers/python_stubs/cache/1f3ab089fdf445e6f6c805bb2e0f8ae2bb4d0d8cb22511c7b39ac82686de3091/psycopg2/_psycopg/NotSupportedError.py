# encoding: utf-8
# module psycopg2._psycopg
# from /usr/local/lib/python3.6/dist-packages/psycopg2/_psycopg.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
""" psycopg2 PostgreSQL driver """

# imports
import psycopg2 as __psycopg2
import psycopg2.extensions as __psycopg2_extensions


class NotSupportedError(__psycopg2.DatabaseError):
    """ A method or database API was used which is not supported by the database. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


