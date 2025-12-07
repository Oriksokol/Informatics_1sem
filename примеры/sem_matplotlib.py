import matplotlib
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-10.,10.,0.5)
y=np.tanh(x)
derivative=(y[1:]-y[:-1])/0.5
plt.figure(figsize=(4,4))
plt.plot(x,y,label='что-то')
plt.plot(x[:-1],derivative, label='производная')
plt.grid(True)
plt.title('График 0,7')
plt.xlabel('иксы')
plt.ylabel('игреки')
plt.legend(loc='lower right')
#plt.savefig('название') -- сохранить график в ту же папку
plt.show()