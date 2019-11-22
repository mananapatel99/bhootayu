def left_rec(prod,a,**Dict):
    i=0;
    alpha=''
    for a in prod:
        if(not(i==0)):
            alpha=alpha+a
        i=i+1
    print("alpha = "+alpha)
    key=Dict.keys()
    B=[]
    b=''
    for prod in B:
        if prod[0]==non:
            b=Dict[non]
    beta=''
    if len(b)>1:
        for a in b:
            if not(a==prod):
                beta=a
                break
    i='1';
    Dict[non]=beta+i
    Dict[i]=alpha+i,'eps'
    print(Dict)
        

nt=int(input("Enter number of non terminals"))
t=int(input("Enter the number of terminals"))
NT=[]
Dict={}
a=input("Enter the non terminals seperated by space").split()
for i in range(nt):
    NT.append(a[i])
print(NT)

T=[]
a=input("Enter the terminals seperated by space").split()
for i in range(t):
    T.append(a[i])
print(T)

cntr=0
for non in NT:
    a=input("Enter the productions from "+non)
    for test in a:
        if(not((test in NT) or (test in T)) and (not(test==' '))):
            cntr=cntr+1
            print("Invalid symbol "+ test)
    b=a.split()
    if(cntr==0):
        Dict[non]=b
print(Dict)

key=Dict.keys()
B=[]
cntr=0

for non in key:
    B=Dict[non]
    if len(B)>1:
        print("Grammar is ambiguous because it is non deterministic")
        cntr=cntr+1
    for prod in B:
        if prod[0]==non:
            print("Grammar is ambiguous because it is left recursive")
            cntr=cntr+1
            left_rec(prod,non,**Dict)
            
if cntr==0:
    print("Grammar is unambiguous")
