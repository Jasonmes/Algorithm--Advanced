#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

a, b, c, d, e, f, g, h = range(8)
N = [[0, 1, 1, 1, 1, 1, 0, 0],
     [0, 0, 1, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 1, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 1, 0, 1],
     [0, 0, 0, 0, 0, 1, 0, 1],
     [0, 0, 0, 0, 0, 1, 1, 0],
     ]

# neighborhood membership
print(N[a][b])

# Degree
print(sum(N[f]))
