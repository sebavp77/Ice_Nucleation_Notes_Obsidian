## Single-$\alpha$ 

One parameter, based on #CNT. It is a stochastic process and can happen with equal probability in any part over the surface of the particle. $\alpha$ is the contact angle

## pdf-$\alpha$ scheme

Modification of single-$\alpha$, it has a distribution of contact angles. The nucleation rate( #nucleation_rate, **j** ) is constant, and the nucleation probability per surface area differs from particle to particle

## Active site scheme

Nucleation happens in preferred sites, active sites. There is no contact angle implicit dependency. Additionally, it is deterministic, meaning that freezing happens instantaneously once certain temperature is reached 

#### INAS density ( #inas)
 It is the number of ice crystals per surface area ( # ice crystals / $m^2$). It is useful to asses how important (in terms of ice activity) is a particle and to compare it with other species.
 The value of $n_s$ at each temperature is calculated according to:
 $$
 n_s(T) = \frac{\sum_{i=1}^m -ln(\frac{N_{i,f}(T)}{N_{i,0}})N_{i,0}}{\sum_{i=1}^m N_{i,0}A_{i}}
$$

Where i is each of of the size bins, $N_{i,f}$ is th number of frozen droplets at temperature T, $N_{i,0}$ is the number of initial droplets and $A_i$ is the surface are for the bin size i