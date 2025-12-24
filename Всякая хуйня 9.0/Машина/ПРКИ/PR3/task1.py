I={'A','B','C','D','E','F','G'}
D=[
    {'A','B','C','D'},
    {'A','C','D','F'},
    {'A','C','D','E','G'},
    {'A','B','D','F'},
    {'B','C','G'},
    {'D','F','G'},
    {'A','B','G'},
    {'C','D','F','G'}
    ]

def getSup(st,D):
    sup=0
    for d in D:
        if (st & d)==st:
            sup+=1
    return sup
def getNextC(L,I):
    C=set()
    for l in L:
       for i in I:
            if not(i in l):
                C=C|{(tuple(sorted(l|{i})))}
    C=[set(s) for s in C]
    return C
           
def apriori(D,I,minsup):
    F=[]
    C=[{i}for i in I]
    while C:
        L=[c for c in C if getSup(c,D)>=minsup]
        F.extend(L)        
        C=getNextC(L,I)
    return F

def updateTree(R,d,mx):
    if not d: return
    for r in R:
        if r[0]==d[0]:
            r[1]+=mx
            updateTree(r[2],d[1:],mx)
            break
    else:
        R.append([d[0],mx,[]])
        updateTree(R[-1][2],d[1:],mx)    

def inspectTreeDwn(R,elm):
    L=[]
    r2r=[]
    for r in R:            
        if r[2]:
            for i in inspectTreeDwn(r[2],elm):
                i[0]=[r[0]]+i[0]
                L.append(i)
        else:
            if r[0]==elm:
                L.append([[],r[1]])
                r2r.append(r)       
    for r in r2r:
        R.remove(r)
    return L
     

def FPGPrepareData(D,I,minsup):
    Idic={i:sum(1 for d in D if i in d) for i in I}
    Idic={i:Idic[i] for i in Idic if Idic[i]>=minsup}
    Idic=sorted(Idic,reverse=True,key=lambda a:Idic[a])
    Dord=[sorted([elm for elm in d if elm in Idic],key=lambda a:Idic.index(a))for d in D]
    return Dord,Idic
              
def makeCPB(FP,I):
    CPB=[]
    while I:
        curr,I=I[-1],I[:-1]
        L=inspectTreeDwn(FP,curr)
        L=[l for l in L if l[0]]
        CPB.append([curr,L])
    return CPB

def makeCFP(CBP):
    CFT=[]
    for cpb in CBP:
        cft=[]
        for i in cpb[1]:
            updateTree(cft,i[0],i[1])
        CFT.append([cpb[0],cft])
    return CFT

def countTree(tree,minsup):
    if not tree: return {},set()
    dic,ptrns={},set()
    for t in tree:
        dwnptrns=set()
        dic[t[0]]= (dic[t[0]]+t[1]) if (t[0] in dic) else t[1]           
        if t[2]:
            dwndic,dwnptrns=countTree(t[2],minsup)
            for elm in dwndic:
                dic[elm]=(dic[elm]+dwndic[elm]) if (elm in dic) else dwndic[elm]  
            ptrns|=dwnptrns|{tuple(elm) for elm in dic if dic[elm]>=minsup}
        if t[1]>=minsup:
            ptrns|={tuple(t[0])}
            if dwnptrns:
                for elm in dwnptrns:
                    ptrns|={tuple(sorted(set(elm)|{t[0]}))}
    ptrns|={tuple(elm) for elm in dic if dic[elm]>=minsup}
    return dic,ptrns


def FPGrowth(D,I,minsup):
    D,I=FPGPrepareData(D,I,minsup)
    FP=[]
    for d in D:
        updateTree(FP,d,1)
    CPB=makeCPB(FP,I)
    CFT=makeCFP(CPB)
    F=set()
    for cft in CFT:
        dic,ptrns=countTree(cft[1],minsup)
        ptrns=[tuple(sorted(set(p)|{cft[0]}))for p in ptrns]
        ptrns.append(tuple(cft[0]))
        ptrns={tuple(sorted(p))for p in ptrns}
        F|=ptrns
    return [set(f)for f in F]

print(apriori(D,I,3))
print(FPGrowth(D,I,2))
