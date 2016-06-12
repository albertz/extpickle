# extpickle - extended pickle

Extends the original [`Pickler` class](https://docs.python.org/ibrary/pickle.html)
to be able to pickle some otherwise non-supported types.
The emphasis is to be fast and for communication via pipes/sockets
with the same Python version on the other end
- thus we don't care that much for compatibility with other versions.

