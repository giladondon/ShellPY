__author__ = 'Gilad Barak'

from sys import argv


def hello(username):
    """
    :param username: String contains name of user
    :return : N/A
    """
    print "Hello " + username + " (:"


try:
    hello(argv[1])
except IndexError:
    print "No username entered after Hello"