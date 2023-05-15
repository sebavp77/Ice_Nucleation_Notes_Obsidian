
## Reference
Ullrich, R., and Coauthors, 2017: A New Ice Nucleation Active Site Parameterization for Desert Dust and Soot. _J. Atmos. Sci._, **74**, 699–717, [https://doi.org/10.1175/JAS-D-16-0074.1](https://doi.org/10.1175/JAS-D-16-0074.1).

## Abstract
- 11 years measured data in AIDA ( #AIDA)
- The framework includes: Desert dust, and soot aerosols
- Ice nucleation was obtained using inas density ( #inas )
- ==Immersion freezing== inas has an exponential dependency with temperature
- ==deposition nucleation==, considering the plot of ice saturation Vs temperature:
	- Negative slope on isolines toward lower temperatures -> explained by **CNT**
	- Behaviour toward higher temperatures --> explained by a pore condensation and freezing mechanism 

* Comparison with a **CNT-based** ( #CNT) empirical parameterization and an empirical framework showed ==large differences== in shape and magnitude of the $n_s$ isolines especially for **deposition nucleation**

# Introduction

Inas density ( #inas) for a polydisperse aerosol sample is given by:
$$\sum_{j=1}^{p}N_{i,j} = \sum_{j=1}^{p}N_{tot,j}(1-e^{-S_{ae,j}n_s(T)})$$

## Data and Methods

Assuming that $S_{ae,j}n_s << 1$ :
$$n_s(T,s_i) \approx \frac{n_i(T,s_i)}{n_{ae,tot}S_{ae}} = \frac{n_i(T,s_i)}{s_{ae}}$$
Where $n_i(T,s_i)$ is the number of frozen droplets at temperature $T$ and super saturation with respect to ice $S_i$, $n_{ae,tot}(T,s_i)$ is the total number of particles, $S_{ae}$ is the aerosol surface area per particle, and $s_{ae}$ is the total aerosol surface area of all particles

- ==Relative error for the inas density of about 40%==
- Large particles were removed
- most of the samples passed a cyclone impactor with a cutoff value between 1 and 5 $\mu m$ to further remove larger particles

# Results

The inas density values derived from the measurements for ==immersion freezing on desert dust== can be approximated by an **exponential function**
$$n_s(T,desert dust) = e^{150.577 - 0,517T}$$
where $T\epsilon[243 , 459]$

* Nevertheless, the scaled parameterization  for illite NX does agree very well with the parameterization for desert dust. Therefore, illite seems to be a good proxy for ice nucleation of desert dus
![[Ulrrich_paper_parameterization_comparison.png]]

# Some technical aspects
* This ice nucleation time interval is further split into  smaller time bins for the analysis. To obtain representative statistics, each bin k is required to have a minimum length of 10 s and to include at least five ice particle   counts. For each bin, the ice number concentration n i,k, the  mean temperature Tk, and the mean ice saturation ratio  $S_{i,k} = RH_{i,k}/100\%$  are determined
* The total aerosol number and  ==surface area concentrations== are obtained from a lognormal  
fit to the size distribution
* The pumping during the experiment leads to a ==reduction== of the ==aerosol concentration==.  
Therefore, the total number and surface area concentrations as measured prior to the pumping and are ==corrected  time-bin-wise== by the ==pressure fraction== $p_k/p_0$ , where $p_k$ is the mean pressure in bin k and $p_0$ the pressure at start of  the expansion
* For **immersion freezing** ( #immersion_freezing ), only the aerosol  activated to droplets will contribute to ice formation. If the **CCN activated fraction is less than 50% the total aerosol surface area concentration is reduced to this fraction**

#### How to obtain the total surface area for each time bin K taking into account the dilution effect

**The aerosol surface area concentration** $s_{ae,k}$ in each time bin $k$ is the fraction of the total   aerosol surface area concentration $s_{ae,0}$ , which, until this time, was activated to ice crystals. ==This fraction is obtained by== integrating the lognormal distribution from a threshold particle diameter $d_{act,k-1}$ to infinity and corrected for the dilution effect

$$
s_{ae,k} = s_{ae,0}\frac{P_k}{P_0}\Phi(\frac{logd_{act,k-1} - logd_{m,s}}{log\sigma_{g,s}})
$$
**By using this equation it is being assumed that the large particle activate first**
$\Phi(x)$ is the standar normal distribution with the cutoff  value x, $d_{m,s}$ is the median diameter, and $\sigma_{g,s}$ the geometric  standard deviation of the aerosol surface area size distribution function, and $d_{act,k-1}$ is the aerosol diameter above  which the aerosols were activated in the previous time bin  calculated from the ice number concentration

### Observation

One of the new things that this study implemented was the consideration of the surface area variation with time and pumping as it was explained in the previous section. Nevertheless, they used samples from old experiments that were analyzed and fitted before. In the case of mineral dust, the previous fit has a small difference with this one on the amount of predicted ice crystals. 

# Appendix

### Reduction due to incomplete CCN activation
For some immersion freezing experiment in the AIDA cloud chamber not all aerosol is activated to droplets. Therefore, the total aerosol surface area concentration available for freezing is not equal to the total concentration obtained from the lognormal distribution function.
So, only certain particle diameter are now *CCN*, we can define the fraction of activated particles as:
$$f_d = \frac{S_{ae}}{S_{ae,0}} \tag{1}$$
Where $S_{ae}$ is the total surface area of all particles that activated to CCN and $S_{ae,0}$ is the total surface area of particles available for activation. Total activation will imply $S_{ae}=S_{ae,0}=1$

**In the following part I am going to derive the equations presented in ==Appendix c==**

Now, knowing that the particle number concentration follows a *==lognormal distribution==* we can obtain the total surface area concentration for the particles that activated to *CCN*. Parting from the lognormal distribution
$$n(l) = \frac{dN(l)}{dl}=\frac{N_0}{ \sigma \sqrt{2\pi}}e^{-\frac{1}{2}(\frac{l - \mu}{\sigma})^2} \tag{2}$$

with $l=ln(x)$, in this case x is either the radius or diameter, $\sigma$ and $\mu$ are the variance and mean of the particle number concentration distribution. If we want to express Equation 2 as function of diamter, consider that
$$n(d) = \frac{dN(l)}{dl}\frac{dl}{dd'}= \frac{N_{0}}{\sqrt{2 \pi}}\frac{1}{d}\frac{1}{\sigma_{l}}exp(-\frac{(ln(d)-\mu_{l})^2}{2 \sigma_{l^{2}}})\tag{3}$$

If we want to obtain the total surface area, we can obtain it from the second moment
$$S(d')=\pi/2\int_{} d'^2n(d')dd' = \pi/2\int_{} d'^{2}\frac{1}{d'}\frac{N_0}{ \sigma_l \sqrt{2\pi}}e^{-\frac{1}{2}(\frac{ln(d') - \mu_l}{\sigma_l})^{2}}dln(d')\tag{4}$$
making some simplifications
$$S(d')=\frac{\sqrt{2\pi}}{4}\frac{N_0}{\sigma_l}\int_{} d'e^{-\frac{1}{2}(\frac{ln(d') - \mu_l}{\sigma_l})^{2}}dln(d')\tag{5}$$

Now, in order to obtain the limits of our integral we need to do, as it is said in the paper, "The  
aerosol surface area concentration available for immersion freezing $s_{ae}$ is obtained by integrating the lognormal distribution from zero to the minimum diameter  dmin"

$d=0 \rightarrow,  ln(d) \rightarrow -\infty$ and $d=d_{min}\rightarrow  ln(d_{min})$ 

**So here is the first difference with the paper**

$$S(d')=\frac{\sqrt{2\pi}}{4}\frac{N_0}{\sigma_l}\int_{-\infty}^{ln(d_{min})} d'e^{-\frac{1}{2}(\frac{ln(d') - \mu_l}{\sigma_l})^{2}}dln(d')\tag{6}$$
Now, we are going to focus in obtaining the variance and geometric mean for our lognormal distribution:
*geometric mean* : the mean is a monotonic variable so the natural logarithm of the mean is the mean of the lognormal distribution
$$\mu_{l}= ln(\mu_s)\tag{7}$$

*Variance:* It is defined according to:

$$\sigma_{s}^{2}=\frac{\int_{0}^{\infty}\left(r-\mu_{s}\right)^{2} n(r)}{N_{0}} dr \tag{8}$$
Obtaining it for the log-space:

$$\begin{aligned}& \ln^2 \left(\sigma_{0}\right)=\frac{\int_{0}^{\infty}\left(\ln (r)-\ln \left(\mu_{s}\right)\right)^{2} n(r) d r}{N_{0}} \\& \ln ^{2}\left(\sigma_{0}\right)= \int_{0}^{\infty}\left(\ln (r)-\ln \left(\mu_{s}\right)\right)^{2} \frac{1}{\sqrt{2 \pi}} \frac{1}{\sigma_{1}} \frac{1}{r} e^{-\frac{-\left(\ln (r)-\ln \left(\mu_{s}\right)\right)^{2}}{2 \sigma_{1}^{2}}} d r \\ & =\frac{1}{\sigma_{l} \sqrt{2 \pi}} \int_{0}^{\infty} \frac{\left[\ln (r)-\ln \left(\mu_{s}\right)\right]^{2}}{r} e^{-\frac{\left(\ln (r)-\ln \left(\mu_{s}\right)\right)^{2}}{2 \sigma_{1}^{2}}}dr\end{aligned}\tag{9}$$
If we define
$$\begin{aligned}&  x = \frac{ln(r)-ln(\mu_s)}{\sqrt{2}\sigma_{l  }} \\& \frac{dx} {dr} = \frac{1}{\sqrt{2}r\sigma_{l}}\rightarrow dr = \sqrt{2}\sigma_lrdx\end{aligned}\tag{10}$$
Using Equation (10) in (9), and considering that $r=0 \rightarrow  x \rightarrow -\infty$ and $r\rightarrow \infty,  x\rightarrow \infty$
$$\begin{aligned}\ln^2 \left(\sigma_{s}\right)=\frac{1}{\sqrt{\pi}}  \int_{-\infty}^{\infty}2\sigma_l^2x^2 e^{-x^{2}}dx\\\ln^2 \left(\sigma_{s}\right)=\frac{2\sigma_l^2}{\sqrt{\pi}}  \int_{-\infty}^{\infty}x^2 e^{-x^{2}}dx\end{aligned} \tag{11}$$
that integral is equal to $\sqrt{\pi}/ 2$ . Finally, we obtain that
$$ln^2(\sigma_{s})=\sigma_l^2\tag{12}$$
and we can conclude that the geometric standard deviation of the lognormal distribution is equal to the natural logarithm of the geometric standard deviation of the distribution

**W**ith this new information we can rewrite our Equation (6) using Equation (7) and (12)
$$S(d')=\frac{\sqrt{2\pi}}{4}\frac{N_0}{ln(\sigma_s)}\int_{-\infty}^{ln(d_{min})} d'exp(-\frac{1}{2}(\frac{ln(d') - ln(\mu_s)}{ln(\sigma_s)})^{2})dln(d')\tag{13}$$
Where the subindex $s$ in $\mu_s$ and $\sigma_s$ makes reference that this is a **Size** distribution.
Let's consider that $d=e^{ln(d)}$ , we can rewrite the integral of Equation (13) as
$$\int_{-\infty}^{ln(d_{min})} e^{ln(d')}exp(-\frac{1}{2}(\frac{ln(d') -ln(\mu_s)}{ln(\sigma_s)})^{2})dln(d')\tag{14}$$
Expanding the binomial
$$\int_{-\infty}^{ln(d_{min})} exp(-(\frac{ln^2(d')-2ln(d')ln(\mu_s) + ln^2(\mu_s)-2ln^2(\sigma_s)ln(d')}{2ln^2(\sigma_s)}))dln(d')\tag{15}$$

We can rearrange terms that share $ln(d')$ 
$$\int_{-\infty}^{ln(d_{min})} exp(-(\frac{ln^2(d')-2ln(d')(ln(\mu_s)+ln^2(\sigma_s)) + ln^2(\mu_s)}{2ln^2(\sigma_s)}))dln(d')\tag{15}$$

$$\begin{aligned}& \text { adding and substracting: }\left(ln(\mu_{s})+\ln ^{2}(\sigma_s)\right)^{2}\end{aligned}$$

Writing down only the therm of the exponential we have
$$\begin{aligned}&-(\frac{{\color{Blue} ln^2(d')-2ln(d')(ln(\mu_s)+ ln^2(\sigma_s))} + ln^2(\mu_s)+{\color{Blue} (ln(\mu_s)+ln^2(\sigma_s))^2}-{\color{green} (ln(\mu_s)+ln^2(\sigma_s))^2}}{2ln^2(\sigma_s)})dln(d')\end{aligned} \tag{16}$$
Where the part highlited in blue is a binomial of the form $(a-b)^2$ with $a=ln^2(d')$ and $b=(ln(\mu_s)+ln^2(\sigma_s))$ . Making this change and expanding the term in green we obtain
$$-(\frac{[ln(d')- (ln(\mu_s)+ln^2(\sigma_s))]^2{\color{Blue}-2ln(\mu_s)ln^2(\sigma_s)-ln^4(\sigma_s)}}{2ln^{2}(\sigma_s)})dln(d')\tag{17}$$
We can break this fraction into two parts: the black part depending on $d'$ and the blue part which does not depend on $d'$ 
$$e^\frac{2ln(\mu_s)+ln^2(\sigma_s)}{2}\int_{-\infty}^{ln(d_{min})} e^-{\frac{[ln(d')- (ln(\mu_s)+ln^2(\sigma_s))]^2}{2ln^2(\sigma_s)}}dln(d')
\tag{18}$$
Considering the exponential part of the integral we can compare it with a normal distribution
$$e^-\frac{(ln(x)-ln(\mu))^2}{2ln^2(\sigma)} = e^-{\frac{[ln(d')- (ln(\mu_s)+ln^2(\sigma_s))]^2}{2ln^2(\sigma_s)}} \tag{19}$$
comparing term by term

$$\begin{aligned}ln(x) = ln(d') \\ln(\mu_{sa}) = ln(\mu_s) + ln^2(\sigma_s)\\ln^2(\sigma_{sa}) = ln^2(\sigma_s)\end{aligned} \tag{20}$$
What the set of equations in 20 says is that the geometric standard deviation for the size distribution and surface area is the same but the geometric mean is different. Using Equations (20), in (19) and writing  the whole expression for surface area density, we obtain

$$S(d')=\frac{\sqrt{2\pi}}{4}\frac{N_0}{ln(\sigma_s)}e^\frac{2ln(\mu_s)+ln^2(\sigma_s)}{2}\int_{-\infty}^{ln(d_{min})} e^-{\frac{[ln(d')- ln(\mu_{sa})]^2}{2ln^2(\sigma_s)}}dln(d')\tag{21}$$
If we call $S_0$ the constant before the integral
$$\boxed{S(d')=\frac{S_0}{ln(\sigma_s)}\int_{-\infty}^{ln(d_{min})} e^-{\frac{[ln(d')- ln(\mu_{sa})]^2}{2ln^2(\sigma_s)}}dln(d')}\tag{22}$$
With $S_0$ being
$$S_0 = \frac{\sqrt{2\pi}}{4}N_0e^{\frac{2ln(\mu_s)+ln^2(\sigma_s)}{2}}$$
Let's now consider the equation provided by the paper
$$s_{ae}= \frac{1}{\sqrt{2\pi}}\int_{log(d_{min})}^\infty dlogd\frac{S_{ae,0}}{log\sigma_{g,s}}exp[-\frac{(logd-logd_{m,s})^2}{2log^2\sigma_{g,s}}] \tag{23}$$
Reorganizing the terms in a similar way to Equation (22) and moving the constant before the integral inside $S_0$ (here log means natural logarithm) we obtain

$$s_{ae}(d)= \frac{S_{ae,0}}{log\sigma_{g,s}}\int_{log(d_{min})}^\infty e^{- \frac{[log(d)-log(d_{m,s})]^2}{2log^2\sigma_{g,s}}}dlogd \tag{24}$$
Where, according to the paper
>"where $s_{ae,0}$ is the total aerosol surface area concentration  obtained from the fit to the measured size distribution  and $d_{m,s}$ and $\sigma_{g,s}$ the appropriate median diameter and  geometric standard deviation, respectively."

==Observation== We can see that both equations ( 22 and 24) are almost identical with the difference of the integration limits 
==Observation 2== It is possible to obtain the same limits as Equation 24 if we consider instead of the **the  aerosol surface area concentration available for immersion freezing** the *already frozen aerosol surface area concentration*, under the supposition that *==large size freezes first==*
$d \rightarrow \infty, ln(d) \rightarrow \infty$ and $d = d_{min}, ln(d)=ln(d_{min})$ 

### Pretty good, but we know that not all particles will activated to CCN and only the activated particles will contribute to immersion freezing

So now, we need to find the amount of particles that activated to CNN ( #CNN), $f_d$. 
Considering the fraction of **nonactivated** particles as:
$1-f_d$ , and with the assumption that large particles activate first, we can consider the nonactivated fraction as the small particles: $d=0, ln(d=0) \rightarrow -\infty$ and $d = d_{min} \rightarrow ln(d_{min})$
$$1 - f_d = \frac{1}{\sqrt{2 \pi}}\frac{1}{ln(\sigma_s)}\int_{- \infty}^{ln(d_{min})}exp(-\frac{1}{2}(\frac{ln(d') - ln(\mu_s)}{ln(\sigma_s)})^{2})dln(d') \tag{25}$$
Focusing on the integral and defining $x=(\frac{ln(|d'|) - ln(\mu_s)}{ln(\sigma_s)})$ , $dln(d') = ln(\sigma_s)dx$ 
**Note** the addition of absolute value doesn't change the result given that the diameter can only have positive values
$$\begin{aligned}& 1 - f_d = \frac{1}{\sqrt{2 \pi}}\frac{1}{ln(\sigma_s)}\int_{- \infty}^{x_{min}}exp(-\frac{1}{2}x^{2})ln(\sigma_s)dx \\& 1 - f_d = \frac{1}{\sqrt{2 \pi}}\int_{- \infty}^{x_{min}}exp(-\frac{1}{2}x^{2})dx\end{aligned}\tag{26}$$
The integral can be solved in the standard way, extending the integration to an additional dimension and the performing the integral in polar coordinates
$$\begin{aligned}& (1 - f_d )^2= \frac{2\pi}{\sqrt{2 \pi}}\int_{0}^{r_{min}}rexp(-\frac{1}{2}r^{2})dr \\& (1 - f_d )^2 = \frac{\pi}{\sqrt{2 \pi}}\int_{0}^{r_{min}}exp(-\frac{1}{2}r^{2})dr^2 \\& (1 - f_d )^2 = \frac{\pi}{\sqrt{2 \pi}}[-\frac{1}{a}e^{-ar^2}]|_{0}^{r_{min}} \\& (1 - f_d )^2 =-\frac{2\pi}{\sqrt{2 \pi}}[e^{-\frac{1}{2}r^2_{min}}-1] \\& (1 - f_d )^2 = -\sqrt{2\pi}[e^{-\frac{1}{2}r^2_{min}}-1]\end{aligned}\tag{27}$$
If the fraction of activated particles is know, we can obtain $x_{min}$
**An alternative, may be better** is using the error function
$$\begin{aligned}& 1 - f_d = \frac{1}{\sqrt{2 \pi}}\int_{- \infty}^{x_{min}}exp(-\frac{1}{2}x^{2})dx \\& 1 - f_d = \frac{1}{2}(1 + erf(\frac{x_{min}}{\sqrt{2}})) \\& 1 - f_d = \frac{1}{2}erfc(-\frac{x_{min}}{\sqrt{2}})\end{aligned}\tag{28}$$
Solving for $x_{min}$
$$-\sqrt{2}ercf^{-1}(2(1-f_d)) = x_{min} \tag{29}$$
With Equation (29) we can obtain the minimum diameter 
$$\begin{aligned}& x_{min}=(\frac{ln(|d'_{min}|) - ln(\mu_s)}{ln(\sigma_s)}) \\\end{aligned}$$
$$
\begin{aligned}
& x_{m i n} = \frac{\ln \left( d_{m \ln }^{\prime}\right)-\ln \left(\mu_s\right)}{\ln \left(\sigma_s\right)} \\
& \ln \left(\sigma_s\right) x_{m in } =\ln (d_{m i n}^{\prime})-\ln \left(\mu_s\right) \\
&\boxed{\mu_s e^{\ln \left(\sigma_s\right) x_{m i n}}  =d_{\text {min }}^{\prime}}
\end{aligned}\tag{30}
$$
With Equation 30 it is possible to obtain the minimum diameter at which CCN ( #CCN) happened.
**In an analogous way we can obtain the surface area concentration available for immersion freezing**
$$\begin{aligned}
& 1=f_F+f_{u n} \\
& 1-f_F=f_{u n} \\
& 1-f_F=\frac{1}{2} \operatorname{erfc}\left(-\frac{x_{\text {min }}}{\sqrt{2}}\right) \\
& f_F=1-\frac{1}{2} e r fc\left(\frac{-x_{\text {min }}}{\sqrt{2}}\right) \\
& \frac{S_{a e}}{S_{a e, 0}}=f_F \\
& \boxed{S_{a e}=S_{a e, 0}[1-\frac{1}{2} e r fc\left(\frac{-x_{\text {min }}}{\sqrt{2}}\right)]}
\end{aligned} \tag{31}$$
Where $f_F$ and $f_{un}$ are the activated and nonactivated frozen fraction, respectively

**Conclusion:**
Despite the intial difference with the paper, it seems like they use the correct equations later and the calculations agree with the physics. 
* We can think this process as splited into two regions:
	*1.* The amount of particles that activate to CCN and will count in the normalization, given by Equations 28, 30 and 31. Then obtain the amount of frozen particles using the initial surface area distribution from the CCN.
	*2.* In the next time step, the before amount of particles won't be taken into account and now we need to consider the amount of particles that didn't freeze in the previous time step, this amount is obtained by using Equation 22. This value will be the new $S_{ae,0}$ and now we can use again Equation 28,30, and 31 to obtain the fraction of particles that activated (if CCN is not 100% efficient)
	*3.* We continue doing step 1 and 2 until all particles activate. 

The following Table presents the relevant equations for the obtention of number concentration and surface area activated and nonactivated due to CCN and which will contribute to immersion freezing. In a similar way the surface area activated to ice can be calculated, where the equations are the same and it is only necessary to change $f_d$ for $f_i$, which is the frozen fraction of particles, particles that activate to CCN and then freeze.

| |Number concentration|Surface area|
|:-:|:------------------------------:|:----------------:|
|activated| $f_d = 1-\frac{1}{2}erfc(-\frac{x_{min,s}}{\sqrt{2}})$| $S_{a e}=S_{a e, 0}[1-\frac{1}{2} e r fc\left(\frac{-x_{\text {min,sa }}}{\sqrt{2}}\right)]$|
|nonactivated| $1-f_d = \frac{1}{2}erfc(-\frac{x_{min,s}}{\sqrt{2}})$|$\frac{1}{2} e r fc\left(\frac{-x_{\text {min,sa }}}{\sqrt{2}}\right)$|
|geometric mean | $\mu_{l}= ln(\mu_s)\tag{7}$  |$ln(\mu_{sa}) = ln(\mu_s) + ln^2(\sigma_s)$ |  
|geometric standard deviation | $ln^2(\sigma_{s})=\sigma_l^2\tag{12}$   |$ln^2(\sigma_{sa}) = ln^2(\sigma_s)$  |
|$x_{min}$|$-\sqrt{2}erfc^{-1}(2(1-f_d)) = x_{min,s} \tag{29}$|$x_{min,sa}=(\frac{ln(d'_{min}) -ln(\mu_{sa})}{ln(\sigma_{sa})})$|
|$d_{min}$|$\mu_s e^{\ln \left(\sigma_s\right) x_{m i n}}  =d_{\text {min }}^{\prime}$|-|

In the following flow diagram is depicted how the surface area concentration is calculated for each time bin. The same procedure (only until 5.a) is valid to calculate the initial concentration of particles activated to CNN, where the stepe (5.a) will be the concentration of activated particles.
![[workflow_Ullrich_normalization.png]]

**The following script and plots consider that the number of particles activated to CCN are already calculated, either being equal to the number of initial particles or to a different value. What we want to see here is how the surface area distribution evolves under different conditions of frozen fraction**

```python
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
```
![[surface_area_Ullrich_paper.png]]
**OBSERVATIONS:** If the frozen fraction ($f_d$) is constant the minimum diameter will be the same all the time. Hence, $f_d$ has to decrease in each time step in order that the minimum diameter drecreases as well. $\rightarrow$ This means that the whole procedure is based on the assumption that larges particles freeze before and that $f_d$ will decrease over time 
* The $erfc^{-^1}$ when is evaluated in 0 goes to $- \infty$ , this means that it is not possible to obtain an efficiency of 100% ?
* $f_d$ cannot be constant?
* (Hannah): the frozen fraction ($f_d$) is considere as a cummulative distribution. e.g., let's suppose we start with 10 particles and 2 frozen in bin k=0, the $f_d = 2/10$. In bin k=1 another 2 particles frozen and now $f_d = (2 + 2) /10$, and so on. This will fix the issue with constant and decreasing $f_d$ but my concern is that this is a cumulative frozen fraction and we are considering differential freezing.
* All CCN activation happens in a first stage and then IN can happen, the alternative where CCN can occur in parallel with IN in later time steps is not contemplated..

*==proposition==*: One way in which $f_d$ can be constant and obtain a different cutoff diameter is if we recalculated $\mu$ and $\sigma$ each time. Some particles will freeze and they won't make part of the distribution anymore, hence the distribution will have different values for the mean and standard deviation. You can see the result of this in the following Figure, where the mean and standard deviation was calculated at each time step. It is possible to observe how the issue with the size of the diameter is solved and now the frozen fraction can increase, decrease or being constant.
![[surface_area_Ullrich_paper_variable_mean_std.png]]

### In the following I will trying to show the justification of my proposition


![[surface_area_distribution_evolution.png]]