from re import X
import matplotlib.pyplot as plt
import numpy as np


with open('NQ.txt', 'r') as f:
    Tiempos = [line.strip() for line in f]

with open('NQN.txt') as s:
    tiempos = [line.strip() for line in s]



tn = np.array(Tiempos)
YN = tn.astype('float')
N_reinas = np.arange(0, len(YN),1)
plt.plot(N_reinas,YN)

tnn = np.array(tiempos)
YNN = tnn.astype('float')
NN_reinas = np.arange(0,len(YNN),1)
plt.plot(NN_reinas,YNN)


plt.xlabel('Número de reinas')
plt.ylabel('Tiempo de compiación en segundos')
plt.title('Módelo N casillas')
plt.legend(["Modelo N", "Modelo NN"], loc='upper left')
plt.show()
