import numpy as np 
import matplotlib.pyplot as plt 
import scipy as sp 
import math 

#function na = dun sa binigay na equation
def waveForm (n,L,x):
    k = np.sqrt(2/L)
    psi_func = k*np.sin(n*math.pi*x/L) 

    return psi_func 

#linearly spaced vector para lang mamodel yung x - axis 
#bale from 0 to 1 lang tapos nag insert ako ng 100 points between 0 and 1 
#palitan mo na lang pre pag need para makita mo yung trend 
x = np.linspace(0,1,100)

#ito different values for n = 1,2,3
#same lang sila ng x axis 
y_1 = waveForm(1,1,x)
y_2 = waveForm(2,1,x)
y_3 = waveForm(3,1,x)

#square nila kasi squared lang daw nung floor y yung probability distribution
y_sq1 = np.square(y_1)
y_sq2 = np.square(y_2)
y_sq3 = np.square(y_3)

#plotting lang 
fig,axes = plt.subplots(2) 
axes[0].plot(x,y_1,'r',label= 'n=1')
axes[0].plot(x,y_2,'g',label= 'n=2')
axes[0].plot(x,y_3,'b',label= 'n=3')
axes[0].grid()
leg = axes[0].legend(loc = 'lower left')
axes[0].set_title('Wave Function')


axes[1].plot(x,y_sq1,'r',label= 'n=1')
axes[1].plot(x,y_sq2,'g',label= 'n=2')
axes[1].plot(x,y_sq3,'b',label= 'n=3')
axes[1].grid()
leg = axes[1].legend(loc = 'upper left')
axes[1].set_title('Probability Density')


plt.tight_layout()
plt.show()