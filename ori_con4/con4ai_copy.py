import tensorflow as tf
import pickle
# 0,1 user 0,1 opponnent
##x_data=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]]
##y_data=[[0,0,1,0,0,0,0]]

with open("connect_4_xinput.txt","rb") as fp:
    x_data=pickle.load(fp)

with open("connect_4_yinput.txt","rb") as fp:
    y_data=pickle.load(fp)


         
   

xs=tf.placeholder(tf.float32,[None,84],name='x_inputs')
ys=tf.placeholder(tf.float32,[None,7],name="y_inputs")

w1=tf.Variable(tf.zeros([84,300]),dtype=tf.float32,name="w1")
b1=tf.Variable(tf.zeros([1,300])+0.1,dtype=tf.float32,name="b1")
Wx_plus_b1=tf.matmul(xs,w1) +b1
l1=tf.nn.leaky_relu(Wx_plus_b1)

w2=tf.Variable(tf.zeros([300,7]),dtype=tf.float32,name="w2")
b2=tf.Variable(tf.zeros([1,7])+0.1,dtype=tf.float32,name="b2")
Wx_plus_b2=tf.matmul(l1,w2) +b2
pre=tf.nn.softmax(Wx_plus_b2)



cross_entropy=tf.reduce_mean( -tf.reduce_sum(ys*tf.log(tf.clip_by_value(pre,1e-10,1.0))))

train_step=tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

saver=tf.train.Saver()
sess=tf.Session()


#sess.run(tf.global_variables_initializer())
#sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
#print(sess.run(pre,feed_dict={xs:x_data}))

saver.restore(sess,'my_con_4_net/save_net.ckpt')
#sess.run(train_step,feed_dict={xs:x_data,ys:y_data})

for i in range(5000):
    sess.run(train_step,feed_dict={xs:x_data,ys:y_data})

print(sess.run(pre,feed_dict={xs:[[0]*84]}))

print(saver.save(sess,'my_con_4_net/save_net.ckpt'))






