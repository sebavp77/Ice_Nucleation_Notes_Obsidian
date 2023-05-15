# Particle Surface Areatitled

# Reference
@article{hartmann2016immersion,
  title={Immersion freezing of kaolinite: Scaling with particle surface area},
  author={Hartmann, Susan and Wex, Heike and Clauss, Tina and Augustin-Bauditz, Stefanie and Niedermeier, Dennis and R{\"o}sch, Michael and Stratmann, Frank},
  journal={Journal of the Atmospheric Sciences},
  volume={73},
  number={1},
  pages={263--278},
  year={2016},
  publisher={American Meteorological Society}
}

# Abstract
* The #freezing_probability ing_probability of #kaolinite particles from fluka scales exponentially with particle #surface_area for different atmospherically  relevant particle sizes
* #kaolinite  particles with #mobile_diameter of 300, 700, and 1000 nm were analyzed with one particle per droplet
* the mobility analyzer technique they used for size selection involves the presence of multiple charged particles. When accounting for these charged particles both a #time_dependent and #time_independent description of the freezing process can reproduce the measurements over the range of examined particle sizes
* from comparison with earlier studies of #kaolinite , it is concluded that the neglection of <mark class='blue'>mutiple charged particles</mark> can cause a **significant** <mark class="yellow">overestimation of the ice nucleation site density</mark> of one order of magnitud, which translates into a temperature bias of **5-6 K**

# Introduction
* From laboratory studies, #kaolinite can be considered as a well-known proxy for mineral dust and has been analyzed quite often since the 1960s
* Other experiments examined the immersion freezing of droplets with varying #particle_size s or particle loads: Archuleta et al. (2005), Marcolli et al. (2007), Welti et al. (2009), Lüönd et al. (2010), Welti et al. (2012), and Pinti et al. (2012) reported an increasing #freezing_probability with increased available particle #surface_area 
* For the <mark class='yellow'>quantification of the particle #surface_area  dependence</mark>  often quantities are used <mark class='yellow'> that are independent of particle sizes or particle loads immersed in the droplets</mark>. Such quantities are, for example, ==the ice nucleation surface site density (**inas**)== or the heterogeneous ice nucleation rate coefficient following the singular or stochastic approach, respectively
* <mark class='red'>To prove the freezing probability with the particle surface area dependence in the immersion freezing mode</mark> they used the following experimental conditions:
			*  quasi-monodisperse particles
			* separate examination of different particle sizes 
			*  air-suspended droplets in which only a single particle is immersed
* Freezing activity as function of #temperature  and #particle_size 

# Material and experiment setup
* #kaolinite  can be originated from chemical weathering  for example #feldspar 
* #ice_detection was done by a **Thermo-stabilized Optical Particle Spectrometer**. It is done through the distintion of the polarization of the scattered ligh 

# Time-independent description

* to describe the freezing activity they use the well know expression
			                                            $f_{ice}(T) = 1 - exp[n_s(T)s_p]$     (3)
	Where $n_s(T)$ is the ice nucleation active site ( #inas ) density, $s_p$ is the particle surface area
* In this study, particles have different #surface_area , referred as #external_mixture 
* To derive $n_s$ multiply charged particles for 300 and 700 nm had to be considered
* The ice fraction of the droplet population with externally mixed INPs can be described by the superposition of the ice fraction of the subpopulation weighted by their fraction of occurrence $a_i$
							                    $f_{ice}(T) = \sum_{i=1}^n a_if_{ice,i}(T)$           (4)
where $a_i$ is the fraction of particles with double or triple charge, this particles will have a different size even for the same mobility size
* <mark class="mark-border red">The particle surface area was calculated assuming a spherical shape of the particles </mark> 
* Then $n_s$ was obtained separately for each selected size: 300, 700 and 1000 nm and temperature by using Equation 3
* To do so, at each selected size, it had to be a priori assumed that $n_s$ for the differently sized particles was identical.
* we found strong indications for the a priori assumption that all particle sizes have identical ns values. This implies that kaolinite particles of different sizes feature similar ice nucleation properties. All of this was for the case for single charged particles
### Effect of multply charged particles
* However, the decrease of ice fractions when comparing uncorrected and multiply charge-corrected data is strongly pronounced for 300 nm, where the difference between the two datasets clearly exceeds the measurement uncertainty. This is not a surprising result as 300-nm kaolinite particles have a higher proportion of multiply charged particles than larger ones and the surface area increases quadratic with diameter, leading to much larger surface areas for multiply charged particles

# Time-dependency description
* They used the #soccer_ball_model (SBM)
* In the SBM, the surface of particles is thought to carry sites, where a specific contact angle $\theta$  is assigned to each of these surface sites
* In the present study, we follow the approach of a statistical distribution of #ice_nucleation efficiencies by using a #contact_angle distribution
* <mark class='yellow'>All particles of the same size have the same number of sites $n_{site}$</mark>
* More surface area, more number of sites ($n_{site}$) 
>> In my opinion, the afore mentioned assumptions, i.e., larger sizes will have more active sites are already ensuring that particles with higher surfaces areas will be more active
* The fact that a single SBM parameter set of $\mu_{\theta}$  and $\sigma_{\theta}$  reproduces the experimental results is highly suggestive for the assumption made that the number of sites scales with particle surface area and hence the statement that kaolinite particles feature similar ice nucleation properties at different sizes
>> When they evaluated the time dependency, they used a paper as reference. Nevertheless, in order to obtain the same #ice_fraction with 800 nm, they had to change the number of active sites found it, from $n_{site}$ = 5.7 to $n_{site}$ = 32.4 which corresponds to a #particle_size  of 1900 nm
>> They mentioned that the reason for this was that the multiply charged particles were not consider and an understimation of the real #particle_size  happened

# Summarizing
**i.** Kaolinite particles have very similar #ice_nucleation properties at different #particle_size s : #inas density and #freezing_rate
**ii.** The result from **i** is necessary to derive:
																					> the same temperature-dependent ice nucleation surface site density or alternatively the same contact angle distribution for different particle sizes.
**iii.** Consequence of the above observations is that the #freezing_probability scales <mark class='yellow'>exponentially</mark> with #surface_area  $f_{ice} \propto  e^{s_p}$ 

# Discussion
* This is rooted in the above described effect, that an increase in residence time by one order of magnitude corresponds to an increase of the observed freezing by 1 K
* Studying the immersion freezing behavior of another mineral dust (ATD) using the same particle generation method, in Niedermeier et al. (2010) and Niedermeier et al. (2011b), it was found that multiply charged particles played a negligible role. So during aerosol generation, the occurrence of multiply charged particles strongly depends on the properties of the sample and on the generation method

# Summary and conclusions
* The immersion freezing capability of quasi-monodisperse size-selected kaolinite particles was investigated as a function of temperature and particle size at a known ice nucleation time.
	--> <mark class='blue'> This is exactly the main goal of my thesis</mark>
* Something important here, I have been questioning what was the instrument they used when they made reference to **mobility diameter**, in this section the say that #mobile_diameter was obtained with #DMA ( differential mobility analyzer) which uses an electric field to obtain the different sizes
* In other words, the probability of freezing scales exponentially with particle surface area. To our knowledge, this is shown for the first time for monodisperse particles where only one INP is immersed in each droplet
* This clearly indicates how important is to account for the fraction of multiply charged particles when using the DMA for size selection (not every particle will present the same behavior for this multply charges)

# In my own words
They analyzed #kaolinite to test the #ice_fraction  or #ice_activity with #particle_size , for this purpose they implemented a method to obtain monodisperse particles and be able to use just **one** #INP inside the cloud droplet. In doing so, they foung that the method they implemented to select the particle size, the #DMA presented mobility diameter for particles with one charge, two or even three charges. The two and three charged particles have a stoke diameter greater than the one charge and hence, the #particle_surface greater as well. In order to account for just one size, they evaluate the #CCN activity of each particles and obtained the fraction of particles for each stoke size.
They also notice, that #ice_properties like #inas or #heterogeneous_rate are independent of size and they only depend of temperature.
This property made possible the analysis and the obtention of the relationships they used.
One important finding was the #ice_activity  with  #particle_size, this was proved using the #deterministic_approach (inas density) and the #Stochasti_behaviour  (soccer ball model, SBM).
Nevertheless, I observed big discrepancy between observations and results from equations or simulations (SBM).
I also noticed they used a lot of assumptions and the explenation for the observed discrepancies where just speculations , for example, the presence of kfeldspar, the presence of larger particles.
**Note:** In this paper the use the #soccer_ball_model and mentioned some papers about how the parameters and implementation was done. Good for reference if I want to use this model


