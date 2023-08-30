import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
dimentions = np.arange(51)
radiuses = np.arange(1,2.05,0.05)
def volume(r, n):
    return np.pi**(n/2)*r**n/gamma(1+n/2)
volumes = []
for ind, n in enumerate(dimentions):
    volumes.append([])
    for r in radiuses:
        volumes[ind].append(volume(r,n))
from matplotlib.ticker import LinearLocator
X = dimentions
xlen = len(X)
Y = radiuses
ylen = len(Y)
X, Y = np.meshgrid(X, Y)
Z = np.transpose(np.array(volumes))
plt.figure()
CS = plt.contour(X, Y, Z,levels=[0.1,1,10,100,1000,10000])
plt.clabel(CS, fontsize=10)
plt.title('Counter plot of N-Sphere HyperVolume')
plt.ylabel('radius')
plt.xlabel('n')
labels = ['0.1', '1','10','100',
           '1000', '10000']
for i in range(len(labels)):
    CS.collections[i].set_label(labels[i])

plt.legend()
plt.savefig('N_sphere_vol_py')
