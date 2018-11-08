#  a- user b- opponent o-null
#->7
#↓ 6

class tab:
    def __init__(self):
        self.table=[list('ooooooo') for x in range(6)]
    def __setitem__(self,tup,value):
        self.table[tup[0]][tup[1]] =value
    def fresh(self):
        self.table=[list('ooooooo') for x in range(6)]
    def __getitem__(self,tup):
        return self.table[tup[0]][tup[1]]
    def __str__(self):
        return ('\n').join([(' ').join([t for t in self.table[x]]) for x in range(6)]) + "\n"
    def __call__(self,us,num):
      for x in range(6):
        try:
            if self.table[x+1][num]=='a' or  self.table[x+1][num]=='b':
                self.table[x][num]=us
                return    
        except:
            pass
      self.table[5][num]=us
    def space_avail(self,num):
        if self.table[0][num]=='o':
            return True
        else:
            return False
    def avail_list(self):
        return [num for num in range(7) if self.table[0][num]=='o']
    def printing(self):
        return ('\n').join([(' ').join([t for t in self.table[x]]) for x in range(6)]) + "\n"
    def x_return(self,comp='a',oppo='b'):
        self.xtable=[]
        for x in range(6):
            for y in range(7):
                if self.table[x][y]==comp:
                    self.xtable+=[1,0]
                elif self.table[x][y]== oppo:
                    self.xtable+=[0,1]
                else:
                    self.xtable+=[0,0]
        return self.xtable   
    def winner(self):
        if all(x != 'o' for x in self.table[0]):
            return 'ab'
        for x in range(6):
            for y in range(7):
                if self.table[x][y]=='a':
                   try:
                       if self.table[x][y+1]==self.table[x][y+2]==self.table[x][y+3]=='a':
                           return 'a'
                   except:
                       pass
                   try:
                       if self.table[x+1][y]==self.table[x+2][y]==self.table[x+3][y]=='a':
                           return 'a'
                   except:
                       pass
                   try:
                       if self.table[x+1][y+1]==self.table[x+2][y+2]==self.table[x+3][y+3]=='a':
                           return 'a'
                   except:
                       pass
                   try:
                       if self.table[x+1][y-1]==self.table[x+2][y-2]==self.table[x+3][y-3]=='a' and y-3 >= 0:
                           return 'a'
                   except:
                       pass
                elif self.table[x][y]=='b':
                   try:
                       if self.table[x][y+1]==self.table[x][y+2]==self.table[x][y+3]=='b':
                           return 'b'
                   except:
                       pass
                   try:
                       if self.table[x+1][y]==self.table[x+2][y]==self.table[x+3][y]=='b':
                           return 'b'
                   except:
                       pass
                   try:
                       if self.table[x+1][y+1]==self.table[x+2][y+2]==self.table[x+3][y+3]=='b':
                           return 'b'
                   except:
                       pass
                   try:
                       if self.table[x+1][y-1]==self.table[x+2][y-2]==self.table[x+3][y-3]=='b' and y-3 >= 0:
                           return 'b'
                   except:
                       pass

        return None


            
        
'''
table=tab()
table.table=[list('oaoooba'),list('aboooab'),list('aboooaa'),list('bbbooab'),list('baaoobb'),list('abbaoaa')]
print(table)
print(table.winner())
'''   

'''
table=tab()
print(table)



table('a',2)
print(table)
print("--------")
table('a',3)
table('a',4)
table('a',5)
table('a',4)
table('b',2)
print(table)
print(table.x_return())
print(table.space_avail(3))
print(table.winner())

'''
