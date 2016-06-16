
from nose.tools import assert_equal, assert_is, assert_is_not
import extpickle
if extpickle.PY3:
    from io import BytesIO as StringIO
else:
    # noinspection PyUnresolvedReferences
    from StringIO import StringIO

import better_exchook
better_exchook.replace_traceback_format_tb()


def pickle(o):
    f = StringIO()
    pickler = extpickle.Pickler(f)
    pickler.dump(o)
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

def test_pickle_list():
    check_pickle([1, 2, "foo", {}])

def test_pickle_dict():
    check_pickle({1: 2, "foo": "bar", "x": [3, 4], "y": {}})

def test_pickle_numpy():
    import numpy
    x = numpy.array([[1.0, 2.0], [3.0, 4.0]])
    x2 = unpickle(pickle(x))
    from numpy.testing.utils import assert_allclose
    assert_allclose(x, x2)

def test_pickle_module():
    mod = extpickle
    mod2 = unpickle(pickle(mod))
    assert_is(mod, mod2)

def test_pickle_module_dict():
    mod = extpickle
    mod_dict = mod.__dict__
    mod_dict2 = unpickle(pickle(mod_dict))
    assert_is(mod_dict, mod_dict2)

def test_pickle_buffer():
    if not extpickle.PY3:
        b = extpickle.make_buffer("foo")
        check_pickle(b)

def test_pickle_old_style_class():
    if not extpickle.PY3:
        class cls:
            x = "foo"
        assert_equal(cls.__name__, "cls")
        assert_equal(cls.__bases__, ())
        assert_equal(cls.x, "foo")
        cls2 = unpickle(pickle(cls))
        assert_equal(cls2.__name__, "cls")
        assert_equal(
            (cls.__name__, cls.__bases__, cls.__dict__, cls.x),
            (cls2.__name__, cls2.__bases__, cls2.__dict__, cls2.x))

def test_pickle_new_style_class():
    class cls(object):
        x = "foo"
    cls2 = unpickle(pickle(cls))
    assert_equal(cls2.__name__, "cls")
    # __dict__ is not really comparable
    assert_equal(
        (cls.__name__, cls.__bases__, cls.x),
        (cls2.__name__, cls2.__bases__, cls2.x))

def test_pickle_func():
    def f(x):
        return x + 23
    assert_equal(f(1), 24)
    f2 = unpickle(pickle(f))
    assert_is_not(f, f2)
    assert_equal(f(2), 25)
