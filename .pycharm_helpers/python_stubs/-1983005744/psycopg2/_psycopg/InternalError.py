# encoding: utf-8
# module psycopg2._psycopg
# from /usr/local/lib/python3.6/dist-packages/psycopg2/_psycopg.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
""" psycopg2 PostgreSQL driver """

# imports
import psycopg2 as __psycopg2
import psycopg2.extensions as __psycopg2_extensions


class InternalError(__psycopg2.DatabaseError):
    """ The database encountered an internal error. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


