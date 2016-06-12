===========================
extpickle - extended pickle
===========================

Extends the original `Pickler class <https://docs.python.org/ibrary/pickle.html>`_
to be able to pickle some otherwise non-supported types.
The emphasis is to be fast and for communication via pipes/sockets
with the same Python version on the other end - thus we don't care that much for compatibility with other versions.

A similar project is `dill <https://pypi.python.org/pypi/dill>`_, which is much bigger though.

This was used in the `TaskSystem project <https://github.com/albertz/TaskSystem>`_.
