#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

# 邻接列表
a, b, c, d, e, f, g, h, j, k = range(10)
N = [
    {b, c, d, e, f},
    {c, e},
    {d},
    {e},
    {f},
    {c, g, h},
    {f, h},
    {f, g}
]

# neighborhoods membership
if b in N[a]:
    print(True)
    print(N[a])
    print(N[b])

# degree
print(len(N[f]))