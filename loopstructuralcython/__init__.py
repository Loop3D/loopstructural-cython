try:
    from ._version_generated import __version__
except ImportError:
    __version__ = "unreleased"
from .cg import cg, fold_cg
