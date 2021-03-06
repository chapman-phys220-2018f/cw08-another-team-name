#!/usr/bin/env python3

"""sinesum.py Test Module

Verify implementation of the Fourier sine series using numpy arrays.
"""

import math
import numpy as np
import sinesum

def test_sum():
    assert math.isclose(sinesum.sum(np.pi/2, 100000), 1.0, rel_tol=1e-5)

def test_func_pi_div_2():
    assert sinesum.func(np.pi/2) == 1

def test_func_0():
    assert sinesum.func(0) == 0

def test_func_neg_pi_div_2():
    assert sinesum.func(-np.pi/2) == -1