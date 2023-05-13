# : exploring the transition from stochastic to singular freezing behavior

# Reference
@article{niedermeier2011heterogeneous,
  title={Heterogeneous ice nucleation: exploring the transition from stochastic to singular freezing behavior},
  author={Niedermeier, D and Shaw, RA and Hartmann, S and Wex, H and Clauss, T and Voigtl{\"a}nder, J and Stratmann, F},
  journal={Atmospheric Chemistry and Physics},
  volume={11},
  number={16},
  pages={8767--8775},
  year={2011},
  publisher={Copernicus GmbH}
}

# Abstract

**Soccer ball model** ( #soccer_ball_model ): Treats particles as being covered with surface sites (particles of finit area) characterized by different nucleation barriers, but with each surface site following the stochastic nature of ice embryo formation 

![[soccer_ball_model.png]]

**Description of the soccer ball model:** The model serves to illustrate how a smooth transition between purely **stochastic** and **singular** behavior occurs as IN surfaces properties are changed

# Essential features in the model

***1.*** Large number of identical and spherical ice nucleus particles (<mark>same size</mark>), each particle immersed in a water droplet
![[soccer_ball_model_illustration.png]]
So they will have: 
									* Uniform thermodynamic conditions
									* Fraction of frozen droplets at a given temperature and time
***2.*** The properties of the particles are not necessarily identical, but are drown from a **probability distribution**
![[gaussian_distribution.jpg|400]]
To that purpose the **surface of each particle** is imagine to be divided into $n_{site}$ surface sites.
Each one having well defined properties. <mark>Ice formation on any given site can be considered to be described by CNT</mark> ( #CNT)
![[soccer_model_eachparticle.png]]

***3.*** Each surface site is characterized by a fixed but randomly chosen water contact angle ( #contact_angle ) ( $\theta_i$)

**Choosen** $n_{site}$**purely stochastic view**

# Freezing probability

It is derived from #CNT 

$$
P_{freeze}(T,\theta, t) = 1 - \prod_{i=1}^{n_{site}}e^{-j_{het}(T,\theta_i(\mu_{\theta_i},\sigma_{\theta_i}))S_{site}t}
$$
Where $\mu$ and $\sigma$ are the mean and standard deviation of the $\theta$ contact angle distribution, $S_{site}$ is the surface area of each active site, and the nucleation rate is defined by
$$
J_{het}(T, \theta_i) = \frac{\kappa T n_s}{h}e^{-(\frac{-\Delta F(T) + \Delta G(T) f(\theta_i)}{\kappa T})}
$$
Where h is the planck constant, $n_s$ is the number density of water molecules at the ice nucleus/water interface , $\kappa$ is the boltzmann constant, F is the kinetic term, G the thermodynamic term ( Gibbs free energy) and f is the contact term (lower the energy required to phase transition due to the contact between the solute and water molecules).

And finally, the **frozen fraction** is
$$
f_{ice}(T,t) = \frac{N_f (T,t)}{N_0} = 1 - \frac{N_U(T,t)}{N_0} = \frac{1}{N_0}\sum_{k=1}^{N_0}P_{freeze,k}(T,t)
$$

