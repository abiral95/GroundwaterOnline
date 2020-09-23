#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import ipysheet as ips
import panel as pn
from scipy import stats 
pn.extension('katex', 'mathjax') 


# # Tutorial 5 #
# 
# + **Tutorial Problem on Hydraulic Conductivities in Complex Systems**
# 
#     1. **Unsaturated Zone**
# 
#     2. **Consolidated Media**
# 
#     3. **Flow nets**
# 
# 
# + **homework problems on   Hydraulic Conductivities and flow nets**
# 
# 

# ## Tutorial Problem on Hydraulic Conductivity in Unsaturated Zone 

# ## Tutorial Problem 12
# 
# From the laboratory test the degree of saturation($\theta$) of the unsaturated core (temperature = $9^{\circ} C$) sample was <br>
# found to be 30% and relative permeability ($k_{r}$) is assumed to be $0.1$.  From the grain analysis the sample was determined to be predominantly <br>
# medium sand (intrinsic permeability, $k = 1.61 \times 10^{-7}$ cm$^2$). Provided that density ($\rho$) and dynamic <br>
# viscosity of water ($\mu$) at $9^\circ C$ is $999.73 \frac{kg}{m^{3}}$ and $0.0013465 \frac{N \cdot s}{m^{2}}$ respectively, find the conductivity of the sample. <br>
# What will be the conductivity of the same sample when the moisture content is $1\%$ ($k_r \approx 0.001$) and $80\%$ ($k_r \approx 0.4$). <br>
# Explain the effect of moisture content on the sample.
# 
# ```{admonition} Tip
# :class: tip
# Lecture contents on the topic in Lecture02 - Slides 02, 22 & 26
# ```

# ### Tutorial Problem 12 - Solution ###
# 
# Hydraulic conductivity of the unsaturated sample ($\theta < 100\%$) can be obtained from the following expression:
# 
# $$
# K(\theta) = \bigg(\frac{k \cdot \rho \cdot g}{\mu}\bigg) \cdot k_r(\theta)
# $$
# 
# 

# In[2]:


# Given 
kr_30  = 0.1 # (-), relative permeability for moist. cont. 30%
i_p = 1.61 * 10**-7 # cm^2, intrinsic permeability
rho = 999.73 # kg/m^3, Sample density
mu = 0.0013467 #  N-s/m^2, dynamic visc.
g_c = 9.81 # N/kg, force unit used for gravitational constant

# Solutions 1
i_pm = i_p/10000 # m^2 unit conversion for int. permeab.
K_30 = (i_p*rho*g_c/mu)*kr_30

# Solution 2  when moisture content is 1% and 80%
kr_1 = 0.001 # (-), relative permeability for moist. cont. 1%
kr_80 = 0.4 # (-), relative permeability for moist. cont. 80%
K_1 = (i_p*rho*g_c/mu)*kr_1
K_80 = (i_p*rho*g_c/mu)*kr_80

# output

print("The conductivity of water when moisture content is 30%  is: {0:1.1e}".format(K_30),"m/s \n")
print("The conductivity of water when moisture content is 1%  is: {0:1.1e}".format(K_1),"m/s \n")
print("The conductivity of water when moisture content is 80%  is: {0:1.1e}".format(K_80),"m/s \n")
print("The conductivity of media increases very rapidly with increase of moisture content")


# ## Tutorial Problem 13
# 
# From the analysis of laboratory results the unsaturated hydraulic conductivity fits the following exponential 
# model as a function of pressure head ($\psi$): $K(\psi) = K_s \exp(\alpha\cdot \psi)$, 
# with $K_s$ $[\frac{L}{T}]$ the saturated hydraulic conductivity and $\alpha$ $[\frac{1}{L}]$ a fit parameter. 
# For the pressure head measurements and the data provided in the figure below, find $K(\psi)$. 
# Also, find the Darcy velocity for this case.
# 

# ### Tutorial Problem 13 - Solution ###
# 
# 
# <img src="images/T04_a_1.png" width=400>

# In[3]:


# Given

K_s = 2 # cm/d # saturated conductivity
al_a = 0.04 # 1/cm, fit constant
Ph_a = -100 # cm, pressure head at A
Ph_b = -90 # cm, pressure head at B
Z_a = 300 # cm, elevation head at A from datum
Z_b = 200 # cm, elevation head at B from datum

# Solution 1 
Ph_m = (Ph_a+Ph_b)/2 # mean pressure head
K_psi = K_s*np.exp(al_a*Ph_m)

#Solution 2
H_A = Ph_a+Z_a # cm, hydraulic head at A
H_B = Ph_b+Z_b # cm, hydraulic head at B
dh_dz = (H_B - H_A)/(Z_b - Z_a) # (-), hydraulic head gradient
q_z = -K_psi*dh_dz # cm/d, Darcy velocity 

print("The unsaturated conductiviy of the sample is: {0:1.3f}".format(K_psi), "cm/d")
print("The Darcy velocity is: {0:1.3f}".format(q_z), "cm/d") 
print("The negative sign indicates the direction opposite to increase in z.") 


# ## 2. Tutorial Problem on Hydraulic Conductivities in Consolidated Media 
# 

# ## Tutorial Problem 14
# 
# Discharge of water at $9° C$ through the fractured rock with a uniform fracture aperature $e=0.1cm$ and width $1m$ is to be obtained. For simplicity, only a single fracture is<br>
# considered (as seen in the figure below) and a hydraulic gradient $i = 0.001$ is assumed. Additionally, the flow in the fracture is assumed to be laminar r Darcy conditions are valid.<br>
# Available watre properties at $9°C$ are:<br>
# dynamic viscosity $\mu_{w}$ = $0.0013465 \frac{N \cdot s}{m^{2}}$ and density $\rho_{w}$ = $999.73 \frac{kg}{m^{3}}$.
# <br><br>
# <img src="images/T04_a_2.png" width=300>
# <br>
# ```{admonition} Tip
# :class: tip
# For more information check Lecture02 - Slide 7
# ```

# ### Tutorial Problem 14 - Solution
# 
# <br>
# The conductivity $(K_s)$ in the single fracture can be obtained from:
# 
# $$
# K_s = \frac{g \cdot \rho \cdot e^2}{12 \mu}
# $$
# 
# where, $g =$ gravitational constant, $\rho =$ density of fluid, $e =$ fracture aperature and $\mu =$ dynamic viscosity

# In[5]:


# Solution Problem 14

# Given
e_p = 0.1 # cm, Fracture aperature 
W = 1 # m, fracture width
mu_3 = 0.0013465 # N-s/m^2, dynamic visocity of water at 9°C
rho_3 = 999.73 # kg/m^3, density of water at 9°C
g_3 = 9.81 # N/kg, gravitational constant
i_3 = 0.001 # (), hydraulic head

#Solution 1
e_pm = e_p/100# m, unit conversion for B
K_3 = e_pm**2*rho_3*g_3/(12*mu_3) # m/s, Conductivity of rock media
Q_3 = W*e_pm*K_3*i_3 # Q = KiA - as Darcy's law is valid

print("The conductiviy of the fracture is: {0:1.3f}".format(K_3), "m/s")
print("The discharge from the rock is: {0:1.3f}".format(Q_3), "m\u00b3/s") 


# ## Tutorial Problem 15 
# 
# The effective porosity of individual matrix blocks within a fractured aquifer is $1.5 \%$ and the hydraulic conductivity $K_{matrix}$ is $1 \times 10^{-8} \frac{m}{s}$. The average aperture of fractures is $35 \mu m$ with an average distance between fractures of $0.8 m$. Water temperature is $9^\circ C$.
# 
#     a) Calculate the hydraulic conductivity of an individual fracture.
# 
#     b) How much is the total hydraulic conductivity?
# 
#     c) Calculate the average linear velocity (in m/a) within fractures and matrix blocks respectively under consideration of a hydraulic gradient $i = 0.001$
# 
# <br>

# ### Solution of Tutorial Problem 15
# 
# For the composite (fracture + matrix), the conductivity ($K_t$) is obtained from:
# $$
# K_t = \frac{e}{F_d}K_s + K_{mat}
# $$
# which is equivalent to
# $$
# K_t = \frac{g \cdot \rho \cdot e^3}{12 F_d \cdot \mu} + K_{mat}
# $$
# 
# where, $K_{mat}$ = matrix conductivity, and $F_d$ = average fracture distance

# In[6]:


# Solution 15, 

#Given are:
e_4 = 35*10**-6 # m, aperature  
F_d = 0.8 # m, average fracture distance  
K_mat = 10**-8# m/s, Hyd. Conductivity
n_e = 1.5/100# (), effective porosity in number
g_4 = 9.81 # N/kg, gravitational constant (known)
i_4 = 0.001

#Water properties at 9°C
mu_4 = 0.0013465 # N-s/m^2, dynamic visocity of water 
rho_4 = 999.73 # kg/m^3, density of water

#Solution (a), (b) and (c)
K_f = e_4**2*rho_4*g_4/(12*mu_4) # m/s, individual hydraulic conductivity see problem 14
K_o = e_4/F_d*K_f+ K_mat # m/s, total Hydraulic conductivity of mass
q_mat = K_mat*i_4 # m/s Darcy velocity in total matrix
v_mat = q_mat/n_e # m/s, linear velocity in total matrix
q_f = K_f*i_4 # Darcy's velocity in single fracture
v_f = q_f/F_d # Linear velocity in single fracture


#output
print("The conductivity of the single fracture is: {0:1.3e}".format(K_f), "m/s")
print("The conductivity of the total rock matrix is: {0:1.3e}".format(K_o), "m/s")
print("Linear velocity in total rock matrix is: {0:1.3e}".format(v_mat), "m/s")
print("Linear velocity in single fracture system is: {0:1.3e}".format(v_f), "m/s")


# ## 3. Tutorial Problem on Flow-nets

# ## Tutorial Problem 16 - Hydrologic Triangle
# 
# The figure below shows the position of four groundwater observation wells with measured hydraulic heads in m a.s.l.
# 
#     a) Sketch head isolines for intervals of $1 m$ by applying the hydrologic triangle method.
#     
#     b) Indicate the flow direction.
# 
# <br><br><img src="images/T03_TP12_a.png" width=400>

# ### Tutorial Problem 16 - Solution
# 
# 1. Connects all the points
# 
# <img src="images/T03_TP12_b.png" width=400>
# 
# 2. Divide the connected lines at equal head-level (here = 1 m)
# 
# <img src="images/T03_TP12_c.png" width=400>
# 
# 3. Join all the equal head lines
# 
# <img src="images/T03_TP12_d.png" width=400>
# 
# 4. Mark the flow direction from higher head towards lower head
# 
# <img src="images/T03_TP12_e.png" width=400>
# 
# 

# ## Tutorial Problem 17 - Flow Nets
# 
# Sketch isolines and streamlines for the two configurations a) and b) of a well doublette shown below. In both cases flow nets should be sketched without and with the uniform flow component.
# 
# a) withdrawal at both wells:
# 
# <img src="images/T03_TP13_a.png" width=200>
# 
# b) Injection at both wells:
# 
# <img src="images/T03_TP13_b.png" width=200>

# # Homework Problems
# 
# ```{admonition} Tip
# :class: tip
# There is no obligation to submit the homework, but if you wish to please submit within two weeks as .ipynb file to my email.
# ```

# ## Homework Problem 5
# 
# In this problem we consider the roughness of the inner-surface of the facture
# that can affect the conductivity of water (at $9^{\circ} C$) in the rock matrix. In this example we consider
# a composite rock matrix with average fracture aperature of $30 \mu m$ and the average 
# spacing between fractures to be $0.5 m$.  Further, we will consider a general relative roughness
# of the inner surface ($\zeta$) of the fracture to be 0.4 and neglect the influence of non-fractured conductivity ($K_{mat}$). 
# We find the effect of surface roughness on conductivity. 
# 
# 
# ```{note}
# With surface roughness in consideration, the conductivity of rock matrix can be obtained from: <br>
# 
# $$ K_{t} = \frac{g \cdot \rho \cdot e^{3}}{12 \cdot C \cdot F_{d} \cdot \mu} + K_{mat} $$
# 
# With $C = (1 + 8.8 \zeta^{1.5})$ describes the fracture roughness for depending on relative roughness $\zeta$
# ```

# ## Homework Problem 6 - Hydraulic Triangle
# 
# The figure below shows the position of five groundwater observation wells with measured hydraulic heads in m a.s.l. 
# 
# 
#     a) Sketch head isolines for intervals of 1 m by applying the hydrologic triangle method.
# 
#     b) Indicate the flow direction.
# 
# <img src="images/T03_TH6.png" width=400>

# ## Homework Problem 7 - Flow Nets
# 
# Sketch head isolines and streamlines for the well doublette shown below. 
# In this case, injection and withdrawal of groundwater is superimposed to a uniform flow component.
# <br><br>
# <img src="images/T03_TH7.png" width=400>
