#!/usr/bin/env python
# coding: utf-8

# # Example of a Groundwater Model

# ## Some information about the Modelarea
# 
# ### Spartial Extension 
# 
# ```{sidebar}Please note:
# Please note, that all this corresponds to a highly simplified setup!
# ```
# 
# As you can see below the horizontal extensions in **x-direction is 4000m** and in **y-direction 2500m.** The aquifer bottom is at **z = 250 m. a.s.l.** and the aquifer itself is **15m thick.**
# The corrosponding groundwater model is horizontally two-dimensional (2D). Vertical flow components are neglected.
# 
# ![title](image\spartialextension.png)
# 
# ### Hydraulic Properties 
# 
# The effective porosity $(n_e)$ in the model domain is $0.2$ or $20\text{%}$
# 
# There are two zone with different hydraulic conductivities $(K)$ and two zones with different groundwater recharge.
# 
# A section of a river ("river reach") is in hydraulic contact with the aquifer. I.e. there may be water transfer from the river to the aquifer ("influent conditions") or vice versa ("effluent conditions").
# 
# Furthermore there exists an inflow boundary with **prescribed hydraulic heads** and a outflow boundary with prescribed hydraulic heads, too. 
# 
# In addition there are two **impermeable boundaries.** 

# ## 2D Scenario and Model Purpose
# 
# An Abstraction of groundwater through wells is planned. In this area there should be an overall pumping rate of $7000 m^3/d$.
# 
# Water extraction is to be distributed between two wells located at (x,y) = (3050m, 1550m) and (x,y) = (3050m, 1450m).
# 
# ![title](image\2dscenario.png)
# 
# The model purpose is to **outline the 50-day isochrone for both wells.**

# ## Modeling 
