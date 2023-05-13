# A Particle-Surface-Area-Based Parameterization of Immersion Freezing on Desert Dust Particles

# Reference
Niemand, M., and Coauthors, 2012: A Particle-Surface-Area-Based Parameterization of Immersion Freezing on Desert Dust Particles. _J. Atmos. Sci._, **69**, 3077–3092, [https://doi.org/10.1175/JAS-D-11-0249.1](https://doi.org/10.1175/JAS-D-11-0249.1).

# Abstract

The parameterization is valid in the temperature range -12°c to -36°c, at or above water saturation. 
The ice nucleation number concentration calculated from te new surface area based parameterization was about of 13 less than IN measurements during the same event.



# Results

They used a Scaning Mobility Particle Sizer ( #SMPS ) andan Aerodynamic Particle Sizer ( #APS ). To compare both measurements the sizes were converted into a voolume equivalent sphere diameter

### Parameterization of immersion freezing
They used inas dentisity ( #inas ) 

$$N_{i,j} = N_{tot,j}(1-e^{-S_{ae,j}n_s(T)})$$

Where $N_{i,j}$ is the number of frozen particles at temperature T, $N_{tot,j}$ is the total number of particles, $S_{ae,j}$ is the surface area, $n_s(T)$ is the inas density, $j$ is the size bin and $i$ is the specie.

<mark>Assumption:</mark> **inas** is considered constant during the whole size distribution, this means that the aerosol composition and surface properties **do not vary with size**.

For a polydisperse aerosol sample, we sum over all p size bins

$$\sum_{j=1}^{p}N_{i,j} = \sum_{j=1}^{p}N_{tot,j}(1-e^{-S_{ae,j}n_s(T)})$$


