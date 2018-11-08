import pickle as pk

with open("connect_4_pos.txt", "wb") as fp:
                  pk.dump([1],fp)
with open("connect_4_xinput.txt", "wb") as fp:
                pk.dump([[0]*84],fp)
with open("connect_4_yinput.txt", "wb") as fp:
                   pk.dump([[0,0,0,1,0,0,0]],fp)
