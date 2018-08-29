#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess


class Tree(object):
    def __init__(self, kids, next=None):
        self.kids = self.val = kids
        self.next = next


t =Tree(Tree('a', Tree('b', Tree('c', Tree('d')))))
print(t.kids.next.next.val)

