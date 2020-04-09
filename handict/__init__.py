import logging

from .handict import Handict  # noqa: F401


logging.getLogger(__name__).addHandler(logging.NullHandler())
