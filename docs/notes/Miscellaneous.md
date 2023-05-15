### #Supersaturation : $s = S -1 = \frac{e}{e_s}-1$
	* s < 0 : Subsaturated environment
	* s = 0 : Saturated environment
	* s > 0 : Supersaturated environment 
	
### #EpitaxialGrowth :
Condensation of gas precursors to from a film on a substrate

### #Epitaxy :
It is where the crytalline orientation of the deposited film is influenced by the crytalline orientation of the substrate material

### #SurfaceEnergy :
Measurement of the excess of energy at the surface of a material. It is used to describe wetting and adhesion between materials.
Surface atoms will have an incomplete unbalanced set of interactions. Therefore, they have unrealised bunding energy
                                                                  ---> Bulk interactions are stronger
Surface energy will be higher if --
                                                                 --> Surface exposure is greater
* The tendency of a solution to spread out ('wet') on a solid surface depends on several factors
<mark class="mark-border blue">low surface energy</mark> --> <mark class="mark-border blue">poor wetting</mark> --> <mark class="mark-border blue">high contact angle</mark> 


![[contact_angle.jpg]]

### #DupresEquation :
Used to relate the interfacial tension ($\sigma_{sl}$) and the interactions between the solid and the liquids

$\sigma_{sl} = \sigma_{l} + \sigma_{s} -W{sl}$ 

Where $W{sl}$ is the work of adhesion --> the work that must be done to separate the two faces

### #OswaldsRuleofStages :
In the course of transformation of an unstable or metastable system into a stable one, the #system does not go directly to the most #stable conformation, but prefers to reach #intermediate stages having closest #freeEnergy to the initial state
    !
    !----> <mark class="mark-border blue">The phase that emerges is the one that separates from the parent phase by the smallest free energy barrier</mark>

### #Wegener-Bergeron-Findeisen-Process : #CloudRain process
It is a process of crystal growth that occurs in mixed phase clouds. It occurs in regions where:

<mark class="mark-border blue">saturation vapor pressure over water</mark> > <mark class="mark-border black"> ambient vapor pressure</mark> > <mark class="mark-border green"> lower saturation vapor pressure over ice</mark> 
--> It is a subsaturated environment for liquid water but supersaturated environment for ice
	--> <mark class='red'>Result</mark> : Rapid evaporation of liquid water and rapid ice crystal growth through <mark class='purple'> vapor deposition</mark>
<mark class='red'>**Required conditions**</mark>
i. Number of droplets >> Number of crystals
ii. Fast adiabatic updraft

### #Critical_Ice_embryo_surface_area :
It is approximately 10 $nm^{2}} at -29°C

### #Stochasti_behaviour:
If I plot $ln(\frac{N_{unf}}{N_0})$ and I obtain a straight line --> <mark class="mark-border blue">Stochastic behavior </mark> 

### #Water_activity: ($a_w$)
It is defined as the #PartialVaporPressure of water in a solution divided by the standard state partial vapor pressure of water
		!
		!--> It is the <mark class="yellow">thermodynamic activity of water as solvent</mark>  and the relative humidity of the surrounding air after equilibrium 
					!
					!--> Generally increases with temperature
				<mark class="yellow">the solute absorbs water from the air</mark>

### #Clausius-Clapeyron relation:
Specifies the #temperature_dependence of #watervaporpressure  at a discontinous phase transition between two #phases of matter of a <mark class="red">single constituent</mark> 
		!
		!--> The increase of the water-holding capacity of the atmosphere by about 7% for every 1°C rise in temperature
The equation applies to vaporization of liquids where vapor follows #ideal_gas_law and liquid volume is neglected as being much smalles than vapor volume V

	$\frac{dP}{dT} = \frac{PL}{T^{2}R}$
	
Where $P$ is the pressure, $L$ is the latent heat, $T$ the temperature and $R$ the ideal gas constant


![[phase_diagram_clausius_clapeyron.png|right]]



### #differential_scanning_calorimetry 
It is a thermoanalytical technique in wich the difference in the amount of heat required to increase the temperature of a sample and reference is measured as a function of temperature. The samples are keep at the same temperature increase rate. **Principle** when the sample undergoes a physical transformation such as #phase_transition, more or less heat will need to flow to it than the reference to maintain both at the same temperature increase rate

### #DVS

### Brunauer-Emmett-Teller #BET
It is used to determine the #specific_surface_area and #pore_size distribution of solid materials. It is based on the physical absorption of inert gas, such as nitrogen, on the solid surface of the sample. Some characteristics:
	* It is determined at isothermal conditions 
	* The properties of the sample define the suitable inert gas for the analysis 
	* The gas forms a monolayer over the surface of the sample

How the surface area is determined? Once the monolayer is formed the sample is placed into a non-nitrogen atmosphere and heated. This allows the release of the adsorbed nitrogen gas molecules from the surface of the sample. The released gas molecules can then be quantified and the surface area and porosity of the sample calculated.
**needed amount** around 500 mg of sample material is needed to obtain reliable results

### #TEM 
Useful to estimate qualitative assessment of the structural integrity of the particles

# Gumbel distribution
It is used to model the distribution of the maximum or minimum of a number of samples of various distributions.
**For example** To represent the maximum level of a river in a particular year if there was a list of maximum values for the past 10 years.
<mark class='yellow'> useful to predict the chance that an extreme flood will occur</mark>

# Features revelant for ice nucleation

These are some of the features that are thoguth to be relevant in ice nucleation process 
* Chemical composition
* Minearology (lattice matching)
* Coatings
* Particle surface area (roughness)
* time (second order importance)

# k-köhler activation theory
(research about this theory)

# Papers that considered time dependency but I didn't consider in this note

* Analysis of isothermal and cooling rate dependent immersion freezing by an unifying stochastic ice nucleation model
* Time-dependent freezing rate parcel model 

# Log-normal distribution ( #lognormal_distribution)

$$
f(x) = \frac{1}{x \sigma \sqrt{2\pi}}e^{-\frac{1}{2}(\frac{ln(x) - \mu}{\sigma})^2}
$$
where $\mu$ is the location parameter and $\sigma$ is the [scale parameter](https://en.wikipedia.org/wiki/Scale_parameter) (the larger the scale parameter, the more spread out the distribution) (**_Caution here!_ These two parameters should not be mistaken for the more familiar mean or standard deviation from a normal distribution.**)
When our log-normal data is transformed using logarithms our μ can then be viewed as the mean _(of the transformed data)_ and σ as the standard deviation _(of the transformed data)_.

==Let’s say your data fits a log-normal distribution. If you then take the logarithm of all your data points, the newly transformed points will now fit a normal distribution==

If you have a normal distribution you can turn it into a log-normal distribution taking the exponential of the x component. On the other way around, if you have a log-normal distribution you can turn it into a normal distribution taking the log.

>“The most efficient way to analyse log-normally distributed data consists of applying the well-known methods based on the normal distribution to logarithmically transformed data and then to back-transform results if appropriate.”

Using the maximum likelihood estimators we can obtain $\mu$ and $\sigma$ 

$$
\mu = \frac{\sum_k^n ln(x_k)}{n}
$$
and 
$$
	\sigma = \frac{\sum_k(ln(x_k) -\mu)^2}{n-1}
$$
**_Note_** The integral of the normal (log-normal) distribution represents the probability that an aleatory variable normally distributed has values between 0 and x

# Size distribution ( #size_distribution)

For a **mono disperse** aerosol the particle diameter describes the size of the particles. This distribution defines the relative amount of particles, sorted by size. it splits the size range into intervals and finds the number of particles in each interval. __Usually normalised by dividing the number of particles in a bin by the width of the interval__.

the area under the frequency curve between two sizes _a_ and _b_ represents the total fraction of the particles in that size range
$$
f_{ab} = \int_a^bf(d_p)dd_p
$$
Where $f_{ab}$ is the frequency function
It can also be formulated in terms of the total number density _N_
$$
dN = N(d_p)dd_p
$$
N is the density of particles.
If we consider the first moment of the size distribution, according to the definition:
$$
\mu_n = \int_{-\infty}^{\infty}(x)^nf(x)dx
$$
with $n$ beign the moment number. For the second moment, n=2 and $f(x) = N(d_p)$ with $x=d_p$. We obtain
$$
\mu_2 = \int_{-\infty}^{\infty}(d_x)^2N(d_p)dd_p
$$
==assuming spherical particles==: as $r=d/2$ and $A=\pi *r^2 = \pi d^2/4$, in order to obtain area in the right side of the equation we need to mutiply by $\pi /4$ , then the aerosol surface area per unit volume (_S_) is given by
$$
S = \pi/2 \int_o ^\infty N(d_p) d_p^2 dd_p
$$
![[Synthetic_aerosol_distribution_in_number_area_and_volume_space.png |550]]

## Enthalpy
( #enthalpy)
It is defined as
$$
H = U + pV
$$
Where $U$ is the internal energy, $p$ is pressure and $V$ is volume. So enthalpy is the energy of certain system and determined moment (neglecting other types of energy as kinetic energy)
**The specifiy enthalpy** is the enthalpy devided by the mass of the system 

# Latent heat
( #latent_heat)

It is defined as the difference in specific enthalpy between two phases of a substance at the same temperature 

# heat capacity
( #heat_capacity)
It is defined as the ratio of energy (or enthalpy) absorbed or released by a system to the corresponding *temperature* rise or fall
For a **constant pressure process**, it is defined as:
$$
C_p = \frac{\partial  H}{\partial T}
$$
