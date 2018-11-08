import connect_4
import random
import pickle as pk
import tensorflow as tf
import numpy as np
from time import sleep

data_xa=[]
data_ya=[]

data_xb=[]
data_yb=[]


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

train_step=tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)
saver=tf.train.Saver()
sess=tf.Session()


table=connect_4.tab()

def show(msg):
    for i in range(len(msg)):
        if msg[i]=='a':
            msg[i]=crayons.red('a')
        elif msg[i]=='b':
            msg[i]=crayons.yellow('b')
    print(msg)        
def ran(x_data,forc,oppo):
    lp= sess.run(pre,feed_dict={xs:[x_data]})
    lp=lp[0]
    l=np.argsort(lp)
    '''
    if table.space_avail(l[-1]) and lp[l[-1]] >=0.9 and random.randrange(0,4)!=2:
        return l[-1]
    else:
            print("EXECUTION HAMPERRED>>>>>>")
            #for m in range(2,8):
            if table.space_avail(l[-2]) and lp[l[-2]] >=0.3 and random.randrange(0,4)!=2:
                return l[-2]
            elif table.avail_list!=[]:
                return random.choice(table.avail_list())
            else:
                return "spacen"
    '''
    if table.space_avail(l[-1]) and lp[l[-1]] >=0.9 and random.randrange(0,4)!=2:
        return l[-1]
    elif max(sess.run(pre,feed_dict={xs:[table.x_return(oppo,forc)]})[0])>=0.92 and np.argsort(sess.run(pre,feed_dict={xs:[table.x_return(oppo,forc)]})[0])[-1] in table.avail_list():
            print("EXECUTION HAMPERRED>>>>>>")
            return np.argsort(sess.run(pre,feed_dict={xs:[table.x_return(oppo,forc)]})[0])[-1]
    else:
            print("EXECUTION HAMPERRED>>>>>>")
            #for m in range(2,8):
            if table.space_avail(l[-2]) and lp[l[-2]] >=0.3 and random.randrange(0,4)!=2:
                return l[-2]
            elif table.avail_list!=[]:
                return random.choice(table.avail_list())
            else:
                return "spacen"
    input("PLACES FILLED>>>>>>>>>")
    exit()
        
def convert(s):
    return [1 if x==s else 0 for x in range(0,7)]

with open("connect_4_pos.txt", "rb") as fp:
                      connect_4_pos=pk.load(fp)
with open("connect_4_xinput.txt", "rb") as fp:
                       connect_4_xinput=pk.load(fp)
with open("connect_4_yinput.txt", "rb") as fp:
                       connect_4_yinput=pk.load(fp)
rag=0
saver.restore(sess,'my_con_4_net/save_net.ckpt')
while True:
    rag+=1
    if rag%70==0:
        with open("connect_4_pos.txt", "wb") as fp:
                  pk.dump([1],fp)
        with open("connect_4_xinput.txt", "wb") as fp:
                pk.dump([[0]*84],fp)
        with open("connect_4_yinput.txt", "wb") as fp:
                   pk.dump([[0,0,0,1,0,0,0]],fp)
        connect_4_pos=[1]
        connect_4_xinput=[[0]*84]
        connect_4_yinput=[[0,0,0,1,0,0,0]]
        print("resseting")

    #saver.restore(sess,'my_con_4_net/save_net.ckpt')
    table.fresh()
    data_xa=[]
    data_ya=[]

    data_xb=[]
    data_yb=[]

    while table.winner()==None:
        data_xa.append(table.x_return())
        ss=ran(table.x_return(),'a','b')
        if ss=='spacen':
            print('draw')
            break
        data_ya.append(convert(ss))
        table('a',ss)
        print(table)
        print('---------------------')
        if table.winner()!=None:
            break
        #sleep(3)
        data_xb.append(table.x_return('b','a'))
        ss=ran(table.x_return('b','a'),'b','a')
        if ss=='spacen':
            print('draw')
            break
        data_yb.append(convert(ss))
        #data_xb.append(table.x_return('b','a'))
        #ss=int(input())
        #data_yb.append(convert(ss))
        table('b',ss)
        #table('b',int(input()))
        print(table)
        print("---------------------")

    print("{} is the winner....".format(table.winner()))
    print(rag)
##    with open("connect_4_pos.txt", "rb") as fp:
##                      connect_4_pos=pk.load(fp)
##    with open("connect_4_xinput.txt", "rb") as fp:
##                       connect_4_xinput=pk.load(fp)
##    with open("connect_4_yinput.txt", "rb") as fp:
##                       connect_4_yinput=pk.load(fp)

    if 'a' in table.winner():
               k = len(data_xa)-1
               for ev in data_xa:
                   if ev in connect_4_xinput:
                              if data_xa.index(ev)/k >= connect_4_pos[connect_4_xinput.index(ev)]:
                                  ma=connect_4_xinput.index(ev)
                                  del connect_4_pos[ma]
                                  del connect_4_xinput[ma]
                                  del connect_4_yinput[ma]
                                  connect_4_xinput.append(ev)
                                  connect_4_yinput.append(data_ya[data_xa.index(ev)])
                                  connect_4_pos.append(data_xa.index(ev)/k)
                   else:
                            connect_4_xinput.append(ev)
                            connect_4_yinput.append(data_ya[data_xa.index(ev)])
                            connect_4_pos.append(data_xa.index(ev)/k)
    if 'b' in table.winner():
               k = len(data_xb)-1
               for ev in data_xb:
                        if ev in connect_4_xinput:
                               if data_xb.index(ev)/k > connect_4_pos[connect_4_xinput.index(ev)]:
                                   ma=connect_4_xinput.index(ev)
                                   del connect_4_pos[ma]
                                   del connect_4_xinput[ma]
                                   del connect_4_yinput[ma]
                                   connect_4_xinput.append(ev)
                                   connect_4_yinput.append(data_ya[data_xb.index(ev)])
                                   connect_4_pos.append(data_xb.index(ev)/k)
                        else:
                         connect_4_xinput.append(ev)
                         connect_4_yinput.append(data_ya[data_xb.index(ev)])
                         connect_4_pos.append(data_xb.index(ev)/k)

    with open("connect_4_pos.txt", "wb") as fp:
                      pk.dump(connect_4_pos,fp)
    with open("connect_4_xinput.txt", "wb") as fp:
                    pk.dump(connect_4_xinput,fp)
    with open("connect_4_yinput.txt", "wb") as fp:
                       pk.dump(connect_4_yinput,fp)


    x_data=connect_4_xinput
    y_data=connect_4_yinput


             
       
    '''
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
    '''


    

    #saver=tf.train.Saver()
    #sess=tf.Session()


    #sess.run(tf.global_variables_initializer())
    #sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
    #print(sess.run(pre,feed_dict={xs:x_data}))

    #saver.restore(sess,'my_con_4_net/save_net.ckpt')
    #sess.run(train_step,feed_dict={xs:x_data,ys:y_data})

    for i in range(5000):
        sess.run(train_step,feed_dict={xs:x_data,ys:y_data})

    print(sess.run(pre,feed_dict={xs:[[0]*84]}))

    print(saver.save(sess,'my_con_4_net/save_net.ckpt'))
                   
