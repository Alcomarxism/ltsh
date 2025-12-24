import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as scst

X=np.array([69, 74, 68, 70, 72, 67, 66, 70, 76, 68, 72, 79, 74, 67, 66, 71, 74, 75, 75, 76])
Y=np.array([153, 175, 155, 135, 172, 150, 115, 137, 200, 130, 140, 265, 185, 112, 140,  150, 165, 185, 210, 220])

#A
print("Mean X: %.2f" % np.mean(X))
print("Median X: %.2f" % np.median(X))
print("Mode X: %.2f" % scst.mode(X).mode)

#B
print("Variance Y: %.2f" % np.var(Y, ddof=1))

#C
distX=scst.norm(loc=np.mean(X),scale=np.std(X, ddof=1))
minX=distX.mean()-3*distX.std()
maxX=distX.mean()+3*distX.std()
step=0.1
pointsx=[]
pointsf=[]
for x in (minX+i*step for i in range(int((maxX-minX)/step))):
    pointsx.append(x)
    pointsf.append(distX.pdf(x))
plt.plot(pointsx,pointsf)
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

#D
print("The probability that the age is greater than 80: %.2f" % (1-distX.cdf(80)))

#E
print("Covariance matrix:\n",np.cov(X,Y))

#F
print("Correlation: %.2f" % np.corrcoef(X,Y)[0][1])

#G
plt.scatter(X,Y)
plt.xlabel("X (возраст)")
plt.ylabel("Y (вес)")
plt.grid()
plt.show()
