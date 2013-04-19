from nose.tools import *
import PROJECT.foo as foo

def setup():
    print "SETUP!"

def teardown():    
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"
    assert foo.add(1,1) == 2
    