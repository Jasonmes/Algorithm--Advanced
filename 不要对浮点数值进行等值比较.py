#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess


# 不要对浮点数进行等值比较
# 可以检查它们之间是否近乎相等

def almost_equal(x, y, places=7):
    return round(abs(x-y), places) == 0


print(almost_equal(sum(0.1 for i in range(10)), 1.0))