#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess


'''
# 构建图的第一步,
# 是创建源 op (source op). 源 op 不需要任何输入,
# 例如 常量 (Constant) .
# 源 op 的输出
# 被传递给其它  op 做运算.
'''


'''
# Python 库中, op 构造器的返回值代表被构造出的 op 的输出, 这些返回值可以传递给其它 op 构造器作为输入.
'''

'''
# TensorFlow Python 库有一个默认图 (default graph),
# op 构造器可以为其增加节点.
# 这个默认图对
# 许多程序
# 来说已经足够用了.
'''

import tensorflow as tf


'''
# 创建一个常量 op, 产生一个 1x2 矩阵. 这个 op 被作为一个节点
# 加到默认图中. #
# 构造器的返回值代表该常量 op 的返回值.
'''
matrix1 = tf.constant([[3., 3.]])
# 创建另外一个常量 op, 产生一个 2x1 矩阵.
matrix2 = tf.constant([[2.], [2.]])
# 创建一个矩阵乘法 matmul op , 把 'matrix1' 和 'matrix2' 作为输入. # 返回值 'product' 代表矩阵乘法的结果.
product = tf.matmul(matrix1, matrix2)

'''
# 默认图现在有三个节点,
# 两个 constant() op,
# 和一个 matmul() op.
# 为了真正进行矩阵相乘运算,
# 并得到矩阵 乘法的 结果,
# 你必须在会话里启动这个图.
'''
print(matrix1, matrix2)
'''
# Tensor("Const:0", shape=(1, 2), dtype=float32) 
# Tensor("Const_1:0", shape=(2, 1), dtype=float32)
'''

'''
# 构造阶段完成后, 才能启动图. 启动图的第一步是创建一个 Session 对象, 如果无任何创建参数, 会话构造器 将启动默认图.
'''

# 启动默认图.
sess = tf.Session()
'''
# 调用 sess 的 'run()' 方法来执行矩阵乘法 op, 传入 'product' 作为该方法的参数.
# 上面提到, 'product' 代表了矩阵乘法 op 的输出, 传入它是向方法表明, 我们希望取回
矩阵乘法 op 的输出. #
# 整个执行过程是自动化的, 会话负责传递 op 所需的全部输入. op 通常是并发执行的. #
# 函数调用 'run(product)' 触发了图中三个 op (两个常量 op 和一个矩阵乘法 op) 的执行. #
# 返回值 'result' 是一个 numpy `ndarray` 对象.
'''
result = sess.run(product)
print(result)
# ==> [[ 12.]]
# 任务完成, 关闭会话.
sess.close()

'''
也可以使用 "with" 代码块 来自动完 成关闭动作.
with tf.Session() as sess:
  result = sess.run([product])
  print result
'''

'''
---------------------------------------
如果机器上有超过一个可用的 GPU, 除第一个外的其它 GPU 默认是不参与计算的. 
为了让 TensorFlow 使用这些 GPU, 你必须将 op 明确指派给它们执行. 
with...Device 语句用来指派特定的 CPU 或 GPU 执行操作:
'''
with tf.Session() as sess:
    with tf.device("/gpu:1"):
        matrix1 = tf.constant([[3., 3.]])
        matrix2 = tf.constant([[2.], [2.]])
        product = tf.matmul(matrix1, matrix2)

'''
/cpu:0" : 机器的 CPU.

• "/gpu:0" : 机器的第一个 GPU, 如果有的话.
• "/gpu:1" : 机器的第二个 GPU, 以此类推.
'''