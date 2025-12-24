import re
I={'A','T','G','C'}
D=[
    'AATACAAGAAC',
    'GTATGGTGAT',
    'AACATGGCCAA',
    'AAGCGTGGTCAA'
    ]

def getSup(st,D):
    sup=0
    st="".join([sti+".*" for sti in st])
    for d in D:
        if re.search(st,d):
            sup+=1
    return sup

def getNextC(L,I):
    C=[]
    for l in L:
       for i in I:
            C.append(l+i)
    return C
           
def GSP(D,I,minsup):
    F=[]
    C=[i for i in I]
    while C:
        L=[c for c in C if getSup(c,D)>=minsup]
        F.extend(L)        
        C=getNextC(L,I)
    return F

print(GSP(D,I,4))
