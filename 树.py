#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess


G = ['G', []]
H = ['H', []]
I = ['I', []]
K = ['K', []]
E = ['E', [G, H, I, K]]  # E节点
D = ['D', []]
F = ['F', []]
A = ['A', [D, E]]  # A节点
B = ['B', []]
C = ['C', [F]]  # C节点
Root = ['root', [A, B, C]]  # 构造树根
print(Root)