import tensorflow as tf
# 0,1 user 0,1 opponnent
x_data=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]]
y_data=[[0,0,1,0,0,0,0]]



def add_layer(nlayer,inputs,in_size,out_size,activation_function=None):
    layer_name="layer "+str(nlayer)
    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
            Weights=tf.Variable(tf.random_normal([in_size,out_size]),name="w"+str(nlayer))
            tf.summary.histogram(layer_name +"/weights",Weights)
        with tf.name_scope('biases'):
            biases=tf.Variable(tf.zeros([1,out_size])+0.1,name="b" +str(nlayer))
            tf.summary.histogram(layer_name+"/biases",biases)
        with tf.name_scope('inputs'):
            Wx_plus_b=tf.matmul(inputs,Weights) +biases
        if activation_function==None:
            outputs=Wx_plus_b
        else:
            outputs=activation_function(Wx_plus_b)
            tf.summary.histogram(layer_name+'/outputs',outputs)
    return outputs       

with tf.name_scope('inputs'):
 xs=tf.placeholder(tf.float32,[None,84],name='x_inputs')
 ys=tf.placeholder(tf.float32,[None,7],name="y_inputs")

l1=add_layer(1,xs,84,300,tf.nn.leaky_relu)
pre=add_layer(2,l1,300,7,tf.nn.softmax)

with tf.name_scope('loss'):
 cross_entropy=tf.reduce_mean(-tf.reduce_sum(ys*tf.log(pre),reduction_indices=[1]))
 tf.summary.scalar('loss',cross_entropy)
with tf.name_scope("train"):
 train_step=tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

#saver=tf.train.Saver()
sess=tf.Session()

merged=tf.summary.merge_all()
write=tf.summary.FileWriter("logsc/",sess.graph)
sess.run(tf.global_variables_initializer())
#sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
#print(sess.run(pre,feed_dict={xs:x_data}))

#saver.restore(sess,'my_net/save_net.ckpt')
for i in range(1000):
    sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
    '''
    if i%50==0:
        result=sess.run(merged,feed_dict={xs:x_data,ys:y_data})
        write.add_summary(result,i)
    '''    
print(sess.run(pre,feed_dict={xs:x_data}))


