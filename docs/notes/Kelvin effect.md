It is related to the curvature of a surface on which water molecules form a drop. Consider the forces that are holding a water drop together for a #flat and #curve #surface, there is a net holding force in the boundary between the liquid and the vapor.

#SurfaceTension($\sigma$): the net inward force divided by the distance along the surface.

_For curve surfaces_: The amount of bonding between one molecule and the other neighbor is reduced, which results that it is highly likely that one water molecule escapes and enter the vapor phase. ---> *The evaporation rate increases* 

_Great Curvature_ ---> Greate chance to molecules to escape:
    ----> <mark class="purple">It takes less energy to remove a molecule from cruved surfaces than flat surfaces</mark>

* Mathematically, the Kelvin equation can be expressed as:
$e_{sc}= e_s(T)*e^{\frac{2\sigma }{n_{L}RTr_d}}$

Where $e_{sc}$  is the equilibrium vapor pressure over a curved surface of pure water
$e_s$  is the equilibrium vapor pressure over a flat surface of pure water
$\sigma$  is the #SurfaceTension 
$n_L$  is the number of moles of liquid water unit per unit volume
R is the universal gas constant 
$r_d$  is the radius of the drop



```run-python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

rd = np.arange(1*1e-9,100*1e-9,1*1e-9) #Radius in m
sigma = 75.64*1e-3 #at 0.01 celcius in units of N/m
T = 273.15 #temperature in degrees
R = 8.31446261815324 #Gas constant in J K-1 mol-1
nl = 55509 #moles in cubic meter of water
inter = (2*sigma)/(nl*R*T)
y = np.exp(inter/rd)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(rd,y)
ax.set_xlabel(r'$R_p (nm)$', fontsize = 12)
ax.set_ylabel(r'$e_{sc}/e_s$', fontsize = 12)
ax.set_title(r'$e_{sc}/e_s$ as function of particle radius')
plt.show()
```

You can see, as the particle radius increases $e_{sc}$  is more similar to $e_s$ and the particle resembles more like a flat surface.
You can also notice that for smaller values of $R_d$  the value of $e_{sc}$  is greather which mean that more water vapor pressure is needed to reach the equilibrium in comparison with a flat surface. In other words, is more difficult to form a droplet over a curved surface than over a flat surface
