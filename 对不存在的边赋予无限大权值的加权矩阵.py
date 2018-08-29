#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

# inf:代表无穷大的值
# 对不存在的边赋予无限大的加权矩阵
a, b, c, d, e, f, g, h = range(8)
inf = float('inf')
w = [[0,     2,   1,   3,   9,   4, inf, inf],
     [inf,   0,   4, inf,   3, inf, inf, inf],
     [inf, inf,   0,   8, inf, inf, inf, inf],
     [inf, inf, inf,   0,   7, inf, inf, inf],
     [inf, inf, inf, inf,   0,   5, inf, inf],
     [inf, inf,   2, inf, inf,   0,   2,   2],
     [inf, inf, inf, inf, inf,   1,   0,   6],
     [inf, inf, inf, inf, inf,   9,   8,   0]
     ]
"""
# 尽管加权矩阵可以使相关权边的访问变得容易，
# 但是目前成员检测 查找某个特定节点的度，
# 或者乃至于在对邻居的遍历操作上都存在着不同之处，
# 也就是说，
# 我们需要对相关的无穷大值进行检测
# neighborhood membership
"""
if w[a][b] < inf:
    print(True)

if w[c][e] < inf:
    print(False)

# degree,对度值求和时，剪掉1，不考虑对角线
print(sum(1 for w in w[a] if w < inf) - 1)




