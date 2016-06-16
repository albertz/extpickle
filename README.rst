===========================
extpickle - extended pickle
===========================

Extends the original `Pickler class <https://docs.python.org/library/pickle.html>`_
to be able to pickle some otherwise non-supported types.
The emphasis is to be fast and for communication via pipes/sockets
with the same Python version on the other end - thus we don't care that much for compatibility with other versions.

A similar project is `dill <https://pypi.python.org/pypi/dill>`_, which is much bigger though.

This project is registered `on PyPI <https://pypi.python.org/pypi/extpickle>`_ and can be installed via

.. code-block::
  
  pip install extpickle
  
For some usage examples, see `the test code <https://github.com/albertz/extpickle/blob/master/tests/test_extpickle.py>`_.

Over the base ``Pickler`` class, it adds pickling support for:

* ``types.FunctionType``, ``types.CodeType`` and cell-types.
  I.e. you can pickle lamdas and functions.
  Note this will use the ``marshal`` module for the byte-code, so this is not portable across different Python versions.
* Modules. This is done by referencing it via its name.
  Note that is has some extra handling for ``__main__``, which is allowed to be a different module.
* ``mod.__dict__`` where ``mod`` is a module is also stored just as a reference to the module, not a copy of the dict.
* (Python 2) ``buffer``.
* ``numpy.ndarray``.
  This is also supported by the base class but our implementation is much faster.
  Actually this is a bit weird because the default implementation should also be just as fast but it isn't.
  Our implementation basically just uses ``fromstring``/``tostring``.
* New-style classes.
  The base class would try to look them up in a module. This will fail whenever it cannot be find in such namespace.
  Our implementation, if that fails, will actually store the information to construct a new class,
  i.e. the name, the bases and its dict.
* (Python 2) Old-style classes. This is the same behavior as for the new-style classes.

This was used in the `TaskSystem project <https://github.com/albertz/TaskSystem>`_.
