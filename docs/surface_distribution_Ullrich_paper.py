# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 09:53:32 2023

@author: sebas
"""
%matplotlib qt
import numpy as np
from scipy.special import erfcinv
from scipy.special import erfc
import matplotlib.pyplot as plt
from numpy.random import seed
from numpy.random import normal
from scipy.stats import shapiro

def x_min(fd):
	argument = 2*(1-fd)
	x = -(np.sqrt(2))*erfcinv(argument)
	return(x)
	
def d_min(x,mu,sigmac):
# x is x min, mu and sigmac are the mean 
# and square geometric standard deviation of the lognormaldistribution
# respectively

	expo = sigmac*x
	
	dmin = np.exp(mu)*np.exp(expo)
	return(dmin)
	
def x_min_sa(dmin,mu,sigma):
	nume = np.log(dmin)-mu
	deno = sigma
	xmin= nume/deno
	return(xmin)

def surfacearea(xminsa,sa0):
    arg = -xminsa/(np.sqrt(2))
    
    sa= sa0*(1- (1/2)*erfc(arg))
    sa0=(1/2)*erfc(arg)
    return(sa,sa0)
	
sigmac = 0.1700 # square geometric standard deviation obtained from icon-art
mu = 0.017 # mean obtained from icon-art
N= 20 # number of time steps until total freezing
mu_sa = mu + sigmac**2 # mean for surface area
N0 = 1 #Initial number concentration
sa0 = (((2*np.pi)**(1/2))*(1/4))*N0*np.exp((1/2)*(2*mu - sigmac)) #Initial surface
dminv=[]
#area concentration
x=np.linspace(0.1,2,N)
fd = np.linspace(0.1,2,N) #linear behavior
fd = np.exp(-x) #Let's suppose that the frozen fraction has a #exponential 
#fd = fd/np.sum(fd) #to normalize
fd_inv = np.exp(-x)# Invert the positions of the elements in the array inverted_arr  
fd_inv = fd_inv[::-1]
#fd will increase until unit
#fd = np.linspace(0.1,1,N)
#behavior with a final efficiency close to 92%
sa = []
sa0_v = []
#fd = (1/N)*np.ones(N)#Constant frozen fraction

##Let's consider that sigma and mu vary in each iteration
sigmac = np.array([0.1700-(0.0085*i) for i in range(N)]) # square geometric standard deviation obtained from icon-art
mu = np.array([0.017-(0.00085*i) for i in range(N)]) # mean obtained from icon-art
mu_sa = mu + sigmac **2  # mean for surface area
sa0 = (((2*np.pi)**(1/2))*(1/4))*N0*np.exp((1/2)*(2*mu[0] - sigmac[0])) #Initial surface

for i in range(N):
    x_min_v = x_min(fd[i])
    dmin = d_min(x_min_v,mu[i],sigmac[i])
    dminv.append(dmin)
    xminsa = x_min_sa(dmin,mu_sa[i], sigmac[i])
    #print('fd decreciente',x_min_v)
    sd,sa0d = surfacearea(xminsa,sa0)
    
    sa.append(sd) #area activated
    sa0_v.append(sa0) #area no activated
    sa0=sa0*sa0d

fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(12, 8))

axs[0, 0].plot(np.arange(len(sa)),sa,label='activated',color='red')
axs[0, 0].plot(np.arange(len(sa0_v)),sa0_v,label='no activated',color='blue')


axs[0, 0].set_ylabel('Surface area')
axs[0, 0].set_title('Decreasing frozen fraction')
axs[1, 0].plot(np.arange(len(fd)),fd,color='blue')
axs[1, 0].set_ylabel('frozen fraction',color='blue')
# Create a second y-axis that shares the same x-axis as the first axis 
ax2 = axs[1, 0].twinx()
ax2.plot(np.arange(len(fd)),dminv,color='green')
ax2.set_ylabel('minimum diamter',color='green')
axs[1, 0].set_xlabel('time step bin k')
#######################################################################
sa = []
sa0_v = []
dminv=[]
x_min_v = 0
dmin = 0
xminsa = 0
sd = 0
sa0d = 0
sa0 = (((2*np.pi)**(1/2))*(1/4))*N0*np.exp((1/2)*(2*mu[0] - sigmac[0])) #Initial surface

for i in range(N):
    x_min_v = x_min(fd_inv[i])
    
    dmin = d_min(x_min_v,mu[i],sigmac[i])
    dminv.append(dmin)
    #print(dmin)
    xminsa = x_min_sa(dmin,mu_sa[i], sigmac[i])
    print('fd creciente',x_min_v)
    sd,sa0d = surfacearea(xminsa,sa0)
    sa.append(sd) #area activated
    sa0_v.append(sa0) #area no activated
    sa0=sa0*sa0d
	
axs[0, 1].plot(np.arange(len(sa)),sa,label='activated',color='red')
axs[0, 1].plot(np.arange(len(sa0_v)),sa0_v,label='no activated',color='blue')


axs[0, 1].set_ylabel('Surface area')
axs[0, 1].set_title('Increasing frozen fraction')
axs[1, 1].plot(np.arange(len(fd)),fd_inv,color='blue')
axs[1, 1].set_ylabel('frozen fraction',color='blue')
# Create a second y-axis that shares the same x-axis as the first axis 
ax3 = axs[1, 1].twinx()
ax3.plot(np.arange(len(fd)),dminv,color='green')
ax3.set_ylabel('minimum diamter',color='green')
axs[1, 1].set_xlabel('time step bin k')
#######################################################################
sa = []
sa0_v = []
dminv=[]
fd_c = np.exp(-x)
x_min_v = 0
dmin = 0
xminsa = 0
sd = 0
sa0d = 0
sa0 = (((2*np.pi)**(1/2))*(1/4))*N0*np.exp((1/2)*(2*mu[0] - sigmac[0])) #Initial surface
fd_c_aux = fd_c[::-1]
fd_c[7:14] = 0.4*np.ones(7)# Constant frozen fraction
fd_c[14:] =fd_c_aux[0:6]
fd_c = fd_c[::-1]
for i in range(N):
    x_min_v = x_min(fd_c[i])
    dmin = d_min(x_min_v,mu[i],sigmac[i])
    dminv.append(dmin)
    xminsa = x_min_sa(dmin,mu_sa[i], sigmac[i])
    sd,sa0d = surfacearea(xminsa,sa0)
    sa.append(sd) #area activated
    sa0_v.append(sa0) #area no activated
    sa0=sa0*sa0d


	
axs[0, 2].plot(np.arange(len(sa)),sa,label='activated',color='red')
axs[0, 2].plot(np.arange(len(sa0_v)),sa0_v,label='no activated',color='blue')


axs[0, 2].set_ylabel('Surface area')
axs[0, 2].set_title('Variable frozen fraction')
axs[1, 2].plot(np.arange(len(fd)),fd_c ,color='blue')
axs[1, 2].set_ylabel('frozen fraction',color='blue')
# Create a second y-axis that shares the same x-axis as the first axis 
ax3 = axs[1, 2].twinx()
ax3.plot(np.arange(len(fd)),dminv,color='green')
ax3.set_ylabel('minimum diamter',color='green')
axs[1, 2].set_xlabel('time step bin k')

axs[0,0].legend()
axs[0,1].legend()
axs[0,2].legend()
fig.tight_layout()
plt.show()


#print(fd)
#print(np.cumsum(fd))
#print(sa)
#print(dminv)


#mu, sigma = 0, 0.1
#data = normal(mu, sigma, size=5000)
##plt.plot(data)

#shapiro(data)
#count, bins, ignored = plt.hist(data, 30, density=True)
#plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
#               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
#         linewidth=2, color='r')
#plt.show()
#data2 = np.sort(data)[::-1] #Sorted data
##Lest's suppose that 10% of the particles froze in k=0
#frozen_p = int(0.95*len(data))
#data3 = data2[frozen_p:]
#shapiro(data3)
#meandata3 = np.mean(data3)
#stddata3 = np.std(data3)
count, bins, ignored = plt.hist(data3, 30, density=True)
plt.plot(bins, 1/(stddata3 * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - meandata3)**2 / (2 * stddata3**2) ),
         linewidth=2, color='r')
plt.show()



