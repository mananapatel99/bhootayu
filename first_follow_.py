#Parsing table, First, Follow, Input string accepted or not
class FirstFollow:
    def __init__(self):#need to pass the grammar here..
        self.gram={'E':['TB'],'B':['+TB','n'], 'T':['FC'],'C':['*FC','n'],'F':['(E)','d']}
        self.term=['+','*','(',')','d','n','$']
        self.nonterm=['E','T','B','C','F']
        
        ''' def findset(self):
        for i in self.nonterm:
            self.firstfind(i)
            #self.follow(i)
        for i in self.term:
            print(firstset[i])
    
    def firstfind(self,ip):
        self.first(ip)'''    
    def first(self,ip):#ip is a string; first() returns first setn
        #print('in First')
        #length=len(ip)
        fir=[]
        ctr=0
        length=0
        if(ip in self.term):
            fir.extend(ip)
        else:
            for i in self.gram[ip]:
               # print('1')
                #print(i[0],":",i,"::")
                if(i[0] in self.term):
                     #print('2')
                     #print(i[0])
                     #print(ctr)
                     fir.extend(i[0])
                else:
                     #print('3')
                     length=len(i)
                     while(ctr<length):
                          #print('4')
                          if('n' in self.gram[i[ctr]]):   # 'n' is for null symbol
                                #print('5')
                                #print(ctr)
                                fir.extend(self.first(i[ctr]))
                                #print(fir)
                                ctr+=1
                                #print(ctr)
                          else:
                                #print('6')
                                
                                fir.extend(self.first(i[ctr]))
                                #print(fir)
                                #print(ctr)
                                break
        firstset[ip]=fir
        return fir

    def follow(self,ip):
        foll=[]
        if(ip=='E'):
            foll.extend('$')
        for key in self.gram.keys():#iterating thorugh the keys of the grammar
            vals=self.gram[key]
            #print('1')
            #print('key',key)
            #print('vals',vals)
            for each in vals:
                #print('2')
                #print('each',each)
                ctr=0
                length=len(each)
                #print('len',length)
                for j in each:
                    #print('3')
                    #print('j',j)
                    if(j==ip):
                        #print('4')
                        if(ctr<length-1):
                            #print('5')
                            if((ip != key)and('n'in self.first(each[ctr+1]))):
                                #print('6')
                                for x in self.first(each[ctr+1]):
                                    if((x not in foll)and(x!='n')):
                                        foll.extend(x)
                                for x in self.follow(key):
                                    if((x not in foll)and(x!='n')):
                                        foll.extend(x)
                                #print('foll',foll)
                            else:
                                #print('7')
                                for x in self.first(each[ctr+1]):
                                    if((x not in foll)and(x!='n')):
                                        foll.extend(x)
                                #print('foll',foll)
                        if((ip != key)and(ctr==length-1)):
                            #print('8')
                            for x in self.follow(key):
                                if((x not in foll)and(x!='n')):
                                    foll.extend(x)
                            #print('foll',foll)
                    ctr+=1
                ctr=0
        followset[ip]=foll
        return foll
      
    def parsingtable(self,ip):
        #print(self.gram)
        
        for i in self.gram[ip]:
            #print("+++",i)
            #print(i[0],":",i,"::",ip)   
            if ip not in parsingtable: 
                parsingtable[ip]={}
                #for j in firstset[ip]:
                    #if j not in parsingtable[ip]: 
                        #parsingtable[ip][j]=[]
                #print("pppp",i,type(i))
            #print(i[0],":",i,"::######",ip)    
            if i[0] in self.term and i[0]!='n':
                    #print(i)
                if i[0] not in parsingtable[ip]:
                    parsingtable[ip][i[0]]=[]
                parsingtable[ip][i[0]].append(str(ip +" -> "+ i))
            elif i == 'n':
                #print("2")
                for k in followset[ip]:
                    if k not in parsingtable[ip]: 
                        parsingtable[ip][k]=[]
                    parsingtable[ip][k].append(str(ip +" -> "+ i))
            else:
                #print("3")
                for k in firstset[ip]:
                    if k not in parsingtable[ip]: 
                        parsingtable[ip][k]=[]
                    parsingtable[ip][k].append(str(ip + " -> "+i))
                
    def printparser(self):
        for i in parsingtable:
            for j in parsingtable[i]:
                for k in parsingtable[i][j]:
                    print(i,":",j,":",k)

    def stringcheck(self):
        inp=['d','+','d','*','$']           #input string
        stack=['$','E']
        a=inp[0]
        b=stack[-1]
        while a!='$' and b!='$':
            if b in self.term and a==b:
                stack.remove(a)
                inp.remove(a)
                print(stack)
                print(inp)
                a=inp[0]
                b=stack[-1]
                
            if b in self.nonterm:
                for i in parsingtable:
                    if i==b:
                        for j in parsingtable[i]:
                            if j==a:
                                c=parsingtable[i][j]
                d=[]
                cntr=0
                for letter in c[0]:
                    if cntr >= 5:
                        d.append(letter)
                    cntr=cntr+1
                f=len(d)
                if d[f-1]=='n':
                    stack.pop()
                    d.pop()
                else:
                    stack[-1]=d[f-1]
                    e=d[f-1]
                    d.remove(e)
                    if len(d)>0:
                        for letter in d[::-1]:         ##Reverse loop
                            stack.append(letter)
                a=inp[0]
                b=stack[-1]
                print(stack)
                print(inp)
                
            if b in self.term and a!=b:
                break

        if a=='$' and b== '$':
            print("String accepted")
        else:
            print("String not accepted")                        
                                                        
firstset={}
followset={}
parsingtable={}
a=FirstFollow()
#a.findset()
nont=['E','T','B','C','F']
# print('FOLLOW :',"e " ,a.first('E'))
for i in nont:
    fi=a.first(i)
    fo=a.follow(i)
    #print('FOLLOW :',i," " ,a.first(i))
    #print('FIRST  :',i," ",a.follow(i))
    firstset[i]=fi
    followset[i]=fo
    

print(firstset)
print(followset)
for i in nont:
    a.parsingtable(i)

a.printparser()
a.stringcheck()
