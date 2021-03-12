#!/usr/bin/env python3
import sys
import os
import numpy as np
import mpmath as mp

def arith(nums):
    return np.sum(nums)/nums.size

def root(x, y):
    return x ** (1./y)

def geom(nums):
    #return float(mp.root(np.prod(nums),  np.size(nums)))
    return float(root(np.prod(nums), np.size(nums)))

def f(nums):
    return np.array([arith(nums), geom(nums), np.median(nums)])

if __name__ == '__main__':
    foo = np.array([1., 1., 2., 3., 5.])

    #print(arith(foo))
    #print(geom(foo))
    #print(np.median(foo))
    #print('')

    for i in range(1, 30):
        print(i)
        print(f(foo))
        foo = f(foo)
        print('')

