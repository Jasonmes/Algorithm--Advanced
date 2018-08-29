#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

# class node(object):
#     def __init__(self, value, next=None): #不用空格
#         self.value = value
#         self.next = next
# L = node("a", node("b", node("c", node("d"))))
#
# print(L.next.next.value)

# 传统列表--通常是由一系列节点来实现的，其每一个节点都都持有下一个节点的引用。


class node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


no = node("a", node("b", node("c", node("d"))))
print(no.next.next.next.next)
