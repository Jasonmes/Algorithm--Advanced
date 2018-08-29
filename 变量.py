#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess
"""
Variables for more details. 变量维护图执行过程中的状态信息. 下面的例子演示了如何使用变量实现一个简 单的计数器. 参见 变量 章节了解更多细节.
"""


import tensorflow as tf

# 创建一个变量, 初始化为标量 0.
state = tf.Variable(0, name="counter")  # 创建一个 op, 其作用是使 state 增加 1
one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)


