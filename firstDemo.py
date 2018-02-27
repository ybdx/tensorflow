import tensorflow as tf
sess = tf.Session()
a = tf.constant(1)
b = tf.constant(29)
c = tf.add(a, b)
print(sess.run(a + b))
print(sess.run(a + c))
