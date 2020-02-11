import numpy as np
import matplotlib.pyplot as plt


def genXY(n):
	X = np.random.normal(loc=0.0, scale=1.0, size=n)
	E = np.random.normal(loc=0.0, scale=1.0, size=n)
	Y = -3. + X * 0. + E
	return X, Y


def augX(X):
	o = np.ones(X.shape[0])
	return np.vstack((o, X)).transpose()
def estimateB(X, Y):
	return np.linalg.inv(X.transpose() @ X) @ X.transpose() @ Y

n = 150
N = 100

ss = []
ns = range(10, 1000, 10)
for n in ns:
	Bhs = []
	for i in range(N):
		X, Y = genXY(n)
		X = augX(X)

		Bh = estimateB(X, Y)

		Bhs.append(Bh)

	Bhs = np.array(Bhs)

	s = np.std(Bhs[:, 1])
	ss.append(s)


t = 1/np.sqrt(ns)


plt.scatter(ns, ss)
plt.scatter(ns, t)
plt.show()
