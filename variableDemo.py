# coding=utf-8
import tensorflow as tf

sess = tf.Session()
a = tf.Variable(10, name='a')
b = tf.constant(10)
op = tf.add(a, b)
update = tf.assign(a, op)

# 初始化变量
sess.run(tf.global_variables_initializer())

print sess.run(a)
print sess.run(op)

print '--------' * 10

for i in range(0, 10, 1):
    sess.run(update)
    # 取单个节点的值
    print i, sess.run(a)

print '--------' * 10

input1 = tf.constant(728)
input2 = tf.constant(1214)
res1 = tf.add(input1, input2)
res2 = tf.multiply(input1, input2)

# 取多个节点的值
print sess.run([res1, res2])

print '--------' * 10

# feed机制，该机制可以临时替代图中任意操作的tensor

m = tf.placeholder(tf.int32)
n = tf.placeholder(tf.int32)
output = tf.multiply(m, n)
res = tf.assign(a, output)

print sess.run([output], feed_dict={m: 7, n: 10})
print sess.run([res, output], feed_dict={m: 728, n: 1214})
print sess.run([output], feed_dict={m: [7, 728], n: [10, 1214]})

result = sess.run([output], feed_dict={m: [7, 728], n: [10, 1214]})
print result[0]
