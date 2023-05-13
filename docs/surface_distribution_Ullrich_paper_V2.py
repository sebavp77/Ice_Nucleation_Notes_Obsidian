# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 10:40:42 2023

@author: sebas
"""


import numpy as np
from scipy.special import erfcinv
from scipy.special import erfc
import matplotlib.pyplot as plt
from numpy.random import seed
from numpy.random import normal
#from scipy.stats import shapiro
import time
seed(42)
#%matplotlib qt
# to run GUI event loop

#################### Defining functions #######################################
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
    #print('sigma: ', sigma)
    #print('nume: ', nume)
    xmin= nume/deno
    return(xmin)

def surfacearea(xminsa,sa0):
    arg = -xminsa/(np.sqrt(2))
    
    sa= sa0*(1- (1/2)*erfc(arg))
    sa0=(1/2)*erfc(arg)
    return(sa,sa0)

def Ndistribution (mu,sigma):
    #Creates the lognormal distribution for the particle concentration
    data = normal(mu, sigma, size=5000)
    return(data)
    
def compute(fd,mu,sigmac,mu_sa,sa0):
    #Computes the values:
        #xmin for size distribution
        #minimun diameter
        #xmin for surface area
        #activated and nonactivated surface area
        #fd: frozen fraction
        #mu: mean of the number size distribution
        #sigmac: std for number size and surface area distribution
        #mu_sa: mean for the surface area distribution
        #sa0: initial amount of surface area particles at time step i
        
    x_min_v = x_min(fd) #xmin for size distribution
    dmin = d_min(x_min_v,mu,sigmac) #minimun diameter
    dminv.append(dmin)
    xminsa = x_min_sa(dmin,mu_sa, sigmac) #xmin for surface area
    #print('fd decreciente',x_min_v)
    sd,sa0d = surfacearea(xminsa,sa0)
    
    sa.append(sd) #area activated
    sa0_v.append(sa0) #area no activated
    sa0=sa0*sa0d
    return(sa,sa0_v,sa0,dminv)

def fd_dec(N):
    #Decreasing frozen fraction
    x=np.linspace(0.1,2,N)
    fd_inv  = np.exp(-x) #Let's suppose that the frozen fraction has a #exponential 
    fd_inv = fd_inv[::-1]
    return(fd_inv)

def fd_cre(N):
    #Increasing frozen fraction
    x=np.linspace(0.1,2,N)
    fd = np.linspace(0.1,2,N) #linear behavior
    fd = np.exp(-x) #Let's suppose that the frozen fraction has a #exponential
    return(fd)

def fd_var(N):
    #Varying frozen fraction
    x=np.linspace(0.1,2,N)
    fd_c = np.exp(-x)
    fd_c_aux = fd_c[::-1]
    fd_c[7:14] = 0.4*np.ones(7)# Constant frozen fraction
    fd_c[14:] =fd_c_aux[0:6]
    fd_c = fd_c[::-1]
    return(fd_c)
###############################################################################
######################## Initiali Values#######################################
N= 20 # number of time steps until total freezing
sigmac = np.sqrt(2) #um Initial square geometric standard deviation obtained from icon-art
mu = 5 #um Initial mean obtained from icon-art
N0 = 1 #Initial number concentration 
cases = 3# Number of different fd cases,e.g.increasing,decreasing,varying
labels= ['Decreasing frozen fraction','Increasing frozen fraction','Varying frozen fraction']
fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(12, 8))
fig1, ax1 = plt.subplots()

ax1.set_xlim(0,11)
ax1.set_ylim(0,1)
for j in range(cases):
    sa0 = (((2*np.pi)**(1/2))*(1/4))*N0*np.exp((1/2)*(2*mu - sigmac)) #Initial surface
    dminv=[] #to store minimum diameter
    sa = [] #area activated
    sa0_v = [] #area no activated
    mu_v = np.zeros(N) #vector containing the mean evolution 
    sigmac_v = np.zeros(N)#vector containing the standard deviation evolution 
    fd_check = 0 #to check that fd is computed once in each case and not N time steps times 
    gaussian_numberdis = Ndistribution(mu,sigmac) #Obtaining the distribution
    data = gaussian_numberdis
    for i in range(N): #goes through each time step

        mu_v[i] = np.mean(data) #Obtaining the mean for that time step
        sigmac_v[i] = np.std(data) #Obtaining the std for that time step
        sigmac_v[i] = 1e-18 if sigmac_v[i]== 0 else np.std(data)
        mu_sa = mu_v[i] + sigmac_v[i]**2 
        
        if fd_check < 1: #Only enters if this is the first time
            if j==0: #increasing frozen fraction 
                fd = fd_cre(N)
                fd_check += 1 #the first time add one
            elif j==1: #decreasing frozen fraction
                fd = fd_dec(N)
                fd_check += 1 #the first time add one
            elif j==2: #Varying frozen fraction
                fd = fd_var(N)
                fd_check += 1 #the first time add one
        
        if j==0:    
            count, bins, ignored = ax1.hist(data, 30, density=True)
            ax1.plot(bins, 1/(sigmac_v[i] * np.sqrt(2 * np.pi)) *
                           np.exp( - (bins - mu_v[i])**2 / (2 * sigmac_v[i]**2) ),
                     linewidth=2, color='r',alpha= (i+1)/20)
        
        
            #plt.pause(1)
            
        sa,sa0_v,sa0,dminv = compute(fd[i],mu_v[i],sigmac_v[i],mu_sa,sa0)
            
        data2 = np.sort(data)[::-1] #Sorted data (initial gaussian distribution)
        
        frozen_p = int(fd[i]*len(data))
        data3 = data2[frozen_p:]# [:]#Take the diameters that haven't frozen yet, which will be my new distribution
        data = data3
    ###################### Time to make the plots #############################
    
    axs[0, j].plot(np.arange(len(sa)),sa,label='activated',color='red')
    axs[0, j].plot(np.arange(len(sa0_v)),sa0_v,label='no activated',color='blue')
    axs[0, j].set_ylabel('Surface area')
    axs[0, j].set_title(labels[j])
    
    axs[1, j].plot(np.arange(len(fd)),fd,color='blue')
    axs[1, j].set_ylabel('frozen fraction',color='blue')
    # Create a second y-axis that shares the same x-axis as the first axis 
    ax2 = axs[1, j].twinx()
    ax2.plot(np.arange(len(fd)),dminv,color='green')
    ax2.set_ylabel('minimum diamter',color='green')
    axs[1, j].set_xlabel('time step bin k')

axs[0,0].legend()
axs[0,1].legend()
axs[0,2].legend()


fig.tight_layout()
plt.show()


