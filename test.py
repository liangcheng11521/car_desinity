import tensorflow as tf


tensor = tf.constant([], tf.string)
sess=tf.Session()
with sess.as_default():
    print("result is ", tensor.eval())