import math

D = [
    [25, "Sports", "L"],
    [20, "Vintage", "H"],
    [25, "Sports", "L"],
    [45, "SUV", "H"],
    [20, "Sports", "H"],
    [25, "SUV", "H"]
]

PL=len([d for d in D if d[2]=='L'])/len(D)
PH=len([d for d in D if d[2]=='H'])/len(D)

HD=-PL*math.log2(PL)-PH*math.log2(PH)
print("Entropy:",HD)
ages=sorted(set([d[0]for d in D]))
cars=list(set([d[1]for d in D]))
Dag=[[d for d in D if d[0]==ag]  for ag in ages]
PagesL=[(len([d for d in dag if d[2]=='L'])/len(dag)) if len(dag)>0 else 0 for dag in Dag]
PagesH=[(len([d for d in dag if d[2]=='H'])/len(dag)) if len(dag)>0 else 0 for dag in Dag]
Hages=[(-PagesH[i]*math.log2(PagesH[i]) if PagesH[i]>0 else 0)+(-PagesL[i]*math.log2(PagesL[i]) if PagesL[i]>0 else 0) for i in range(len(ages))]
Hage=sum([Hages[i]*len(Dag[i])/len(D)for i in range(len(ages))])
Dca=[[d for d in D if d[1]==ca]  for ca in cars]
PcarsL=[(len([d for d in dca if d[2]=='L'])/len(dca)) if len(dca)>0 else 0 for dca in Dca]
PcarsH=[(len([d for d in dca if d[2]=='H'])/len(dca)) if len(dca)>0 else 0 for dca in Dca]
Hcars=[(-PcarsH[i]*math.log2(PcarsH[i]) if PcarsH[i]>0 else 0)+(-PcarsL[i]*math.log2(PcarsL[i]) if PcarsL[i]>0 else 0) for i in range(len(cars))]
Hcar=sum([Hcars[i]*len(Dca[i])/len(D)for i in range(len(cars))])
print("Ages entropty",Hage)
print("Cars entropy",Hcar)

maxGain=0
for car in cars:
    DY=[d for d in D if d[1]==car]
    DN=[d for d in D if d[1]!=car]
    DYL=[d for d in DY if d[2]=='L']
    DYH=[d for d in DY if d[2]=='H']
    DNL=[d for d in DN if d[2]=='L']
    DNH=[d for d in DN if d[2]=='H']
    PYL=len(DYL)/len(DY)
    PYH=len(DYH)/len(DY)
    PNL=len(DNL)/len(DN)
    PNH=len(DNH)/len(DN)
    HDY=(-PYL*math.log2(PYL)if PYL>0 else 0)+(-PYH*math.log2(PYH) if PYH>0 else 0)
    HDN=(-PNL*math.log2(PNL)if PNL>0 else 0)+(-PNH*math.log2(PNH)if PNH>0 else 0)
    gain=HD-(len(DY)/len(D))*HDY-(len(DN)/len(D))*HDN
    if gain>maxGain:
        maxGain,bestDivCar=gain,car
        bestHDY,bestHDN=HDY,HDN
        bestDY,bestDN=DY,DN


cars.remove(bestDivCar)
print("First diviston:",[bestDivCar],cars)
print("Entripies after division:",bestHDY,bestHDN)
D=bestDY

maxGain=0
for div in [(ages[i]+ages[i+1])/2 for i in range(len(ages)-1)]:
    DY=[d for d in D if d[0]<=div]
    DN=[d for d in D if d[0]>div]
    DYL=[d for d in DY if d[2]=='L']
    DYH=[d for d in DY if d[2]=='H']
    DNL=[d for d in DN if d[2]=='L']
    DNH=[d for d in DN if d[2]=='H']
    PYL=len(DYL)/len(DY) if len(DY)>0 else 0
    PYH=len(DYH)/len(DY)if len(DY)>0 else 0
    PNL=len(DNL)/len(DN)if len(DN)>0 else 0
    PNH=len(DNH)/len(DN)if len(DN)>0 else 0
    HDY=(-PYL*math.log2(PYL)if PYL>0 else 0)+(-PYH*math.log2(PYH) if PYH>0 else 0)
    HDN=(-PNL*math.log2(PNL)if PNL>0 else 0)+(-PNH*math.log2(PNH)if PNH>0 else 0)
    gain=HD-(len(DY)/len(D))*HDY-(len(DN)/len(D))*HDN
    if gain>maxGain:
        maxGain,bestDivAge=gain,div
        bestHDY,bestHDN=HDY,HDN
        bestDY,bestDN=DY,DN

print("First diviston: <=",bestDivAge)
print("Entripies after division:",bestHDY,bestHDN)

point=[27,"Vintage"]

if point[1]==bestDivCar:
    if point[0]<=bestDivAge:
        cls='H'
    else:
        cls='L'
else:
    cls='H'
print ("Predicted class:",cls)