
import extpickle
from StringIO import StringIO
from nose.tools import assert_equal

#import better_exchook
#better_exchook.replace_traceback_format_tb()


def pickle(o):
    f = StringIO()
    pickler = extpickle.Pickler(f)
    pickler.dump("foo")
    return f.getvalue()

def unpickle(s):
    f = StringIO(s)
    unpickler = extpickle.Unpickler(f)
    return unpickler.load()

def check_pickle(o):
    s = pickle(o)
    o2 = unpickle(s)
    assert_equal(o, o2)


def test_pickle_str():
    check_pickle("foo")

