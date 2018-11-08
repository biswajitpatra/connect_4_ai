import connect_4
import random
import pickle as pk
import tensorflow as tf
import numpy as np
from time import sleep
import colorama
import crayons

colorama.init()

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
saver=tf.train.Saver()
sess=tf.Session()
saver.restore(sess,'my_con_4_net/save_net.ckpt')

table=connect_4.tab()

def show(msgt):
    msg=msgt.printing()
    msg=list(msg)
    for i in range(len(msg)):
        if msg[i]=='a':
            msg[i]=crayons.magenta('a',bold=True)
        elif msg[i]=='b':
            msg[i]=crayons.yellow('b',bold=True)
    for i in msg:
        print(i,end='')
def ran(x_data,forc,oppo):
    lp= sess.run(pre,feed_dict={xs:[x_data]})
    lp=lp[0]
    l=np.argsort(lp)
    if table.space_avail(l[-1]) and lp[l[-1]] >=0.9:
        return l[-1]
    elif max(sess.run(pre,feed_dict={xs:[table.x_return(oppo,forc)]})[0])>=0.92 and np.argsort(sess.run(pre,feed_dict={xs:[table.x_return(oppo,forc)]})[0])[-1] in table.avail_list():
            print("EXECUTION HAMPERRED>>>>>>")
            return np.argsort(sess.run(pre,feed_dict={xs:[table.x_return(oppo,forc)]})[0])[-1]
    else:
       print("EXECUTION HAMPERRED>>>>>>")
       for m in range(2,8):
         if table.space_avail(l[-m]):
                return l[-m]
    input("PLACES FILLED>>>>>>>>>")
    exit()
        
def convert(s):
    return [1 if x==s else 0 for x in range(0,7)]

while table.winner()==None:
    data_xa.append(table.x_return())
    ss=ran(table.x_return(),'a','b')
    data_ya.append(convert(ss))
    table('a',ss)
    show(table)
    print('---------------------')
    if table.winner()!=None:
        break
    #sleep(3)
    #data_xb.append(table.x_return('b','a'))
    #ss=ran(table.x_return('b','a'),'b','a')
    #data_yb.append(convert(ss))
    data_xb.append(table.x_return('b','a'))
    ss=int(input())
    data_yb.append(convert(ss))
    table('b',ss)
    #table('b',int(input()))
    show(table)
    print("---------------------")

print("{} is the winner....".format(table.winner()))

with open("connect_4_pos.txt", "rb") as fp:
                  connect_4_pos=pk.load(fp)
with open("connect_4_xinput.txt", "rb") as fp:
                   connect_4_xinput=pk.load(fp)
with open("connect_4_yinput.txt", "rb") as fp:
                   connect_4_yinput=pk.load(fp)

if table.winner()=='a':
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
if table.winner()=='b':
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

input("DONE...")
