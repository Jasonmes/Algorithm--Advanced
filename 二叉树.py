#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

# 二叉树类


class Tree(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right


t = Tree(Tree('a', 'b'), Tree('c', 'd'))
