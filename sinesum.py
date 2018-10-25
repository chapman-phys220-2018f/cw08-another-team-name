#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Jacob Anabi, Grady Lynch
# Student ID: 2294644, 02297574
# Email: anabi@chapman.edu, grlynch@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: CW08
###

"""Sinesum Module Description
This module computes the sum S_n(t) and the function f(t).
S_n(t) = (4/pi)*((1/(2*k-1))*sin((2*(2*k-1)*pi*t)/(T)) where k exists in the interval [1, n])
f(t) is a piecewise function where:
    f(t) = 1 for 0 < t < T/2, 0 for t = 0, -1 for -T/2 < t < 0
"""

import numpy as np

def sum(t, n, T=2*np.pi):
    """Sum function description
    Computes the sum S_n(t) = (4/pi)*((1/(2*k-1))*sin((2*(2*k-1)*pi*t)/(T)) where k exists in the interval [1, n])

    Args:
        t: the t value
        n: the upper bound of the sum

    Keyword Arguments:
        T -- the T value (default 2*pi)
    """
    k = np.arange(1, n, 1)
    s = (1/(2*k-1))*np.sin((2*(2*k-1)*np.pi*t)/(T))
    return (4/np.pi)*np.sum(s)

def func(t, T=2*np.pi):
    """Func function description
    Computes the piecewise function f(t) where:
        f(t) = 1 for 0 < t < T/2, 0 for t = 0, -1 for -T/2 < t < 0

    Args:
        t: the t value

    Keyword Arguments:
        T -- the T value (default 2*pi)
    """
    if (t > 0 and t < T/2):
        return 1
    elif (t == 0):
        return 0
    elif (t > -T/2 and t < 0):
        return -1
    else:
        return 0

print(sum(np.pi, 100000))