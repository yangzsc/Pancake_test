# encoding: utf-8
# module psycopg2._psycopg
# from /usr/local/lib/python3.6/dist-packages/psycopg2/_psycopg.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
""" psycopg2 PostgreSQL driver """

# imports
import psycopg2 as __psycopg2
import psycopg2.extensions as __psycopg2_extensions


from .object import object

class Binary(object):
    """ Binary(buffer) -> new binary object """
    def getquoted(self): # real signature unknown; restored from __doc__
        """ getquoted() -> wrapped object value as SQL-quoted binary string """
        pass

    def prepare(self, conn): # real signature unknown; restored from __doc__
        """ prepare(conn) -> prepare for binary encoding using conn """
        pass

    def __conform__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, buffer): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    adapted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



