import scipy.stats
import numpy as np
D = [
    ['T', 'T', 5.0, 'Y'],
    ['T', 'T', 7.0, 'Y'],
    ['T', 'F', 8.0, 'N'],
    ['F', 'F', 3.0, 'Y'],
    ['F', 'T', 7.0, 'N'],
    ['F', 'T', 4.0, 'N'],
    ['F', 'F', 5.0, 'N'],
    ['T', 'F', 6.0, 'Y'],
    ['F', 'T', 1.0, 'N']
]
point=['T','F',1.0]
DY=[d[:-1]  for d in D if d[3]=='Y']
DN=[d[:-1]  for d in D if d[3]=='N']
PY=len(DY)/len(D)
PN=len(DN)/len(D)
PYT0=len([dy for dy in DY if dy[0]=='T'])/len(DY)
PYF0=len([dy for dy in DY if dy[0]=='F'])/len(DY)
PYT1=len([dy for dy in DY if dy[1]=='T'])/len(DY)
PYF1=len([dy for dy in DY if dy[1]=='F'])/len(DY)
FY2=scipy.stats.norm(np.mean([dy[2] for dy in DY]),np.std([dy[2] for dy in DY],ddof=1))
PNT0=len([dn for dn in DN if dn[0]=='T'])/len(DN)
PNF0=len([dn for dn in DN if dn[0]=='F'])/len(DN)
PNT1=len([dn for dn in DN if dn[1]=='T'])/len(DN)
PNF1=len([dn for dn in DN if dn[1]=='F'])/len(DN)
FN2=scipy.stats.norm(np.mean([dn[2] for dn in DN]),np.std([dn[2] for dn in DN],ddof=1))
PpointInY=(PYT0 if point[0]=='T'else PYF0)*(PYT1 if point[1]=='T'else PYF1)*FY2.pdf(point[2])*PY
PpointInN=(PNT0 if point[0]=='T'else PNF0)*(PNT1 if point[1]=='T'else PNF1)*FN2.pdf(point[2])*PN
print(PpointInY,PpointInN)
if(PpointInY>PpointInN):
    print("Класс Y")
else:
    print("Класс N")