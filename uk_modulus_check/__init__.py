import sys
from importlib.metadata import version as _get_version

from .sort_code_substitution_table import SortCodeSubstitutionTable
from .uk_modulus_checker import UKModulusChecker, ValidationResult
from .weight_table import ModMode, ModRule, Weights, WeightTable

__all__: tuple[str, ...] = (
    # sort_code_substitution_table.py
    "SortCodeSubstitutionTable",
    # uk_modulus_checker.py
    "UKModulusChecker",
    "ValidationResult",
    # weight_table.py
    "ModMode",
    "ModRule",
    "WeightTable",
    "Weights",
)

__version__ = _get_version("uk-modulus-check")

version = f"{__version__}, Python {sys.version}"
