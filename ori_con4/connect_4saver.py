import tensorflow as tf



Weights1=tf.Variable(tf.random_normal([84,300]),dtype=tf.float32,name="w1")
biases1=tf.Variable(tf.zeros([1,300])+0.1,dtype=tf.float32,name='b1')

Weights2=tf.Variable(tf.random_normal([300,7]),dtype=tf.float32,name='w2')
biases2=tf.Variable(tf.zeros([1,7])+0.1,dtype=tf.float32,name='b2')


saver=tf.train.Saver()

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    save_path=saver.save(sess,'my_con_4_net/save_net.ckpt')
    print(save_path)
  

       
