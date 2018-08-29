#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess
#
# from random import randrange
# seg = [randrange(8*8) for i in range(60)]
# dd = float('inf')
# for x in seg:
#     for y in seg:
#         if x == y: continue
#         d = abs(x-y)
#         if d < dd:
#             xx, yy, dd = x, y, d
# print(xx, yy)

from random import randrange

seg = [randrange(8 * 8) for i in range(60)]
seg.sort()
dd = float('inf')
for i in range(len(seg) - 1):
    x, y = seg[i], seg[i + 1]
    if x == y: continue
    d = abs(x - y)
    if d < dd:
        xx, yy, dd = x, y, d
print(xx, yy)
