#!/usr/bin/env python3
"""Type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies the float"""
    def multiply(x: float) -> float:
        """ multiply the float"""
        return x * multiplier
    return multiply
