#!/usr/bin/env python
# coding: utf-8

# # Groundwater Modelling - Some Basics

# A **Model** is a **representation, an image or a description of a real system.** 
# For example, the real system can be a porous medium through whose pores water flow (Darcy experiment). The corresponding model is the Darcy Law (flow rate $\sim$ hydraulic gradient).
# 
# Each model is subject to **simplifications**. It's only an "image" of the real system. Darcy's Law, for example, does not provide an accurate representation of the flow through individual pore channels. Rather, average flow behaviour is represented through many pore channels. 

# ## Process-Based and Empirical Models
# 
# Models can be classified according to various criteria.
# 
# One criterion is based on the consideration of physical principles. 
# A **physical based model (process-based model)** is a model based exclusively on **physical principles.** In most cases these principles represent conservation laws (e.g. for mass, volume, momentum, electric charge or energy).
# 
# On the contrary, an **empirical model** describes the real system by **using data only** (e.g. via regression analysis). 
# The following plot shows an empirical model via regression analysis.
# 
# 
# ![title](image\empirical_model.png)
# 
# Hybrids occur as well (**"semi-empirical models"**) 
# In reality, Darcy's Law is a semi-empirical model: on the one hand, it is based on the conservation of momentum. On the other hand, it is not possible to strictly derive the direct proportionality between flow velocity and hydraulic gradient by averaging the flow behaviour across all pores.

# ## Conceptual Models
# 
# Another criterion for model classification distinguishes the qualitative from the quantitative description of a real system.
# 
# A **conceptual model** provides a **qualitative** representation of the relevant system components, processes and impacts in the area of investigation. This representation is usually **shown graphically**, e.g. as block model (see below), horizontal or vertical cross sections or schematic illustrations.
# 
# ![tile](image\blockmodel.png)
# 
#                             (Middlemis, 2001: Groundwater flow modelling guideline)

# ## Mathematical Models
# 
# A **mathematical model** provides a **quantitative** representation of the relevant system components, resorcesses and impacts in the area of investigation. The quantitative representation is based on **mathematical equations.**
# 
# The most simple mathemtical model in hydrogeology is Darcy's Law for one-dimensional steady-state groundwater flow in confined aquifer:
# $$ v_f = -K \cdot \frac{\Delta h}{L}$$
# 
# Solutions of the mathematical equations can be categorized as **analytical** and **numerical.**

# ### Analytical solution
# 
# There are **exact mathematical expressions solving the model equations.**
# 
# Below you can see an example of an analytical Solution. The situation is represented schematically in the following conceptual model.
# 
# ![title](image\analyticalmodel.png)
# 
# The mathematical model  consisting of an one-dimensional groundwater flow equation and two boundary conditions results in:
# 
# $$\frac {d}{dx}(-h \cdot K \cdot \frac{dh}{dx})=N, \quad h(0) = h_0 \quad \text{and} \quad h(L)=h_L $$
# 
# The analytical solution results in: $$h(x)= \sqrt{h_0^2-(h_0^2-h_L^2) \cdot \frac{x}{L} + \frac{N}{K} \cdot x \cdot (L-x)}$$

# ### Numerical Solution or numerical Method
# 
# There is no exact mathematical expression wich solves the model equations. Rather, it is only possible to obtain **a large set of numbers that approximate the exact solution.**
# 
# An Example for a model without analytical solution is shown below. Parameter heterogenity and irregular model domain boundaries lead to more sophisticated versions of the underlying groundwater flow equition. In this case the analytical solutions are no longer possible. Approximative numerical methods are required.
# 
# ![title](image\numericalmodel.png)
#  
#                              (University of Waterloo, Dept. of Earth Sciences)

# ## From the conceptual Model to the numerical Approach
# 
# ![title](image\concept_to_numeric.png)
# 
#                         (from Anderson and Woessner: Applied Groundwater Modeling, 1992)
#                         
#       
# 

# ## Data Requirements
# 
# Various data are required to create models. Those are:
# 
# - topographical maps (with surface waters and water divides)
# - geological maps, geological profiles (see preceding example) 
# - maps with isolines of aquifer bottoms/ thicknesses, aquitard bottoms/ thicknesses
# - maps indicating vertical extensions of sediments under rivers and lakes 
# - hydrogeological maps (hydraulic head isolines)
# - water level time series in observation wells and rivers
# - time series of spring discharges
# - maps and profiles of storage coefficients 
# - information on spatial and temporal variability of inlow/ outflow due to 
#    - groundwater recharge
#    - evapotranspiration
#    - interaction between groundwater and surface water 
#    - groundwater abstraction 
#    - natural groundwater flow 
# 

# In[ ]:




