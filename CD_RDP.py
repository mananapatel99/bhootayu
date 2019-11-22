print("Epsilon is represented by !")
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
        if(not((test in NT) or (test in T) or (test=="!")) and (not(test==' '))):
            cntr=cntr+1
            print("Invalid symbol "+ test)
    b=a.split()
    if(cntr==0):
        Dict[non]=b
print(Dict)

key=list(Dict.keys())

for non in key:
    abc=non+"(){"
    print(abc)
    B=Dict[non]
    cntr=0
    a=len(B)
    for prod in B:
        x=list(prod)
        for y in x:
            if(y in T):
                abc="if (input== "+y+" ) \n\t input++"
                print(abc)
            if(y in NT):
                abc="\t"+y+"()"
                print(abc)
            if(y=="!"):
                print("else return")
        cntr=cntr+1
        if(cntr != a):
            print("else")
           
    print("}")

abc="main(){\n"+key[0]+"();\nif(input=='$')\nprintf(Parsing Successful)\n}"
print(abc)
        

##        if(len(B)==0):
##            print("return")
