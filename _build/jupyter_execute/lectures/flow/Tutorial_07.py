#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import ipysheet as ips
import panel as pn
from scipy import stats 
pn.extension('katex') 


# # Tutorial 7 #
# 
# In this chapter:
# 
# + **solutions of homework problems 5 – 7**
# 
# + **tutorial problems on Flow in natural systems**
# 
#     1. Flow in confined Aquifers
#     
#     2. Flow in unconfined Aquifers
# 

# ## Solution of Homework Problems 5 – 7

# ## Homework Problem 5
# 
# In this problem we consider the roughness of the inner-surface of the facture that can affect the conductivity of water (at $9^\circ C$) in the rock matrix. In this example we consider a composite rock matrix with average fracture aperature of $30 \mu$m and the average spacing between fractures to be $0.5 m$.  Further, we will consider a general relative roughness of the inner surface ($\zeta$) of the fracture to be 0.4 and neglect the influence of non-fractured conductivity ($K_{mat}$).
# We find the effect of surface roughness on conductivity. 
# <br>
# 
# ```{admonition} Tip
# :class: tip
# With surface roughness in consideration, the conductivity of rock matrix can be obtained from:
# 
# $$ K_{t} = \frac{g \cdot \rho \cdot e^{3}}{12 \cdot C \cdot F_{d} \cdot \mu} + K_{mat} $$
# 
# With $C = (1 + 8.8 \cdot \zeta^{1.5})$ describes the fracture roughness for depending on relative roughness $\zeta$
# ```

# In[2]:


# Solution Homework Problem 5
#Given
B_5 = 30 * 10**-6 # m, aperature
F_d5 = 0.5 # m, average spacing between fractures
z_a = 0.4# (), relative roughness
mu_5 = 0.0013465 # N-s/m^2, dynamic visocity of water at 9°C
rho_5 = 999.73 # kg/m^3, density of water at 9°C
g_5 = 9.81 # N/kg, gravitational constant
K_mat5 = 0 # m/s, matrix conductivity neglected in this problem

#interim calculation
C = 1+8.8*z_a**1.5 # (), C calculation

#Solution
K_t5 = g_5*rho_5*B_5**3/(12*C*F_d5) + K_mat5 # m/s, conductivity with inclusion of roughness factor
K_t5b = g_5*rho_5*B_5**3/(12*F_d5) + K_mat5 # m/s, conductivity without roighness consideration
dif_K = K_t5b/K_t5 # m/s, ratio of conductivities without and with roughness

#output
print("The conductivity with inclusion of roughness factor is: {0:1.3e}".format(K_t5), "m/s \n")
print("The conductivity without inclusion of roughness factor is :{0:1.3e}".format(K_t5b), "m/s \n")
print("The ratio of conductivities without and with roughness is:{0:1.2f}".format(dif_K), "\n")
print("Over 3 times higher conductivity is found when roughness is not considered.\n This will also lead to same increase in linear velocity")


# ## Homework Problem 6 - Hydrological Triangle
# 
# The figure below shows the position of five groundwater observation wells with measured hydraulic heads in m a.s.l.
# 
#     a) Sketch head isolines for intervals of $1 m$ by applying the hydrological triangle method.
# 
#     b) Indicate the flow direction.
# 
# <br>
# <img src="images/T05_2a.png" width=300>
# <br>
# 
# ```{admonition} Tip
# :class: tip
# For more information see Lecture06 - Slides 8-10
# ```

# ### Homework Problem 6 - Solution
# 
# <br>Start:<br>
# <img src="images/T05_2a.png" width=300>
# 
# <br>Step 1:<br>
# <img src="images/T05_2b.png" width=300>
# 
# <br>Step 2:<br>
# <img src="images/T05_2c.png" width=300>
# 
# <br>Step 3:<br>
# <img src="images/T05_2d.png" width=300>
# 
# <br>Step 4:<br>
# <img src="images/T05_2e.png" width=521>

# ## Homework Problem 7 - Flow Nets
# 
# Sketch head isolines and streamlines for the well doublette shown below. In this case, injection and withdrawal of groundwater is superimposed to a uniform flow component.
# <br><br>
# <img src="images/T03_TH7.png" width=400>
# <br>
# 
# ```{admonition} Tip
# :class: tip
# For more information see Lecture06 - Slides 17-19
# ```

# ### Homework Problem 7 - Solution
# 
# The flownet is presented in the figure below. The solution provided in quantitative.
# <br><br>
# 
# <img src="images/T07_H7.png" width=700>

# ## Tutorial Problems on flow in natural systems
# 
# 
# ### 1.  Flow in Unconfined Aquifers

# ## Tutorial Problem 20 - Flow in confined aquifer with a uniform thickness
# 
# A confined aquifer is $30 m$ thick and $5 km$ wide. Two observation wells are located $1.5 km$ apart in the direction of flow. The head in well 1 is $h_{1} = 90 m$ and in well 2 it is $h_{2} = 85 m$.<br>
# The hydraulic conductivity is $1.5 \frac{m}{d}$.<br>
# 
#     a) What is the total daily flow of water through tthe aquifer?
# 
#     b) What is the elevation of the potentiometric surface at a point located $0.5 km$ from well 1
# 
# <br>
# <img src="images/T06_Y1.png" width=350>

# ### Tutorial Problem 20 - Solution
# 
# From Darcy Law:
# 
# $$ q' = K \cdot b \cdot \frac{dh}{dL} \qquad\qquad \text{(eq. 1A)} $$
# 
# where,
# $q'$ is flow per unit width $[\frac{L}{T}]$, <br>
# $b$ is aquifer thickness $[L]$, <br>
# $K$ is hydraulic conductivity $[\frac{L}{T}]$ <br>
# and $\frac{dh}{dL}$ is hydraulic gradient $[-]$
# <br><br>
# Since the thickness of the aquifer is uniform, any hydraulic head between two known heads ($h_{1}$ and $h_{2}$) can be obtained by rearranging the above equation, from
# 
# $$ h_{2} = h_{1} - \frac{q'}{K \cdot b} \cdot x \qquad\qquad \text{(eq. 1B)} $$
# 
# where $x$ is the distance from $h_{1}$
# 

# In[3]:


# Given are:
m_1 = 30 # m, uniform thinckness of aquifer 
w_1 = 5 * 1000 # m, width of the aquifer
d_l = 1.5 * 1000 # m, distance between wells
hy1_w1 = 90 # m, head in well 1
hy1_w2 = 85 # m, head in well 2
K_1 = 1.5 # m/d, conductivity in aquifer


#Solution 1
dh_y1 = (hy1_w1 - hy1_w2)/d_l # (-), head gradient
Q_y1 = K_1*m_1*dh_y1*w_1 # m^3/day, discharge using the first eq. above.

#Solution 2 
w_2 = 0.5 *1000 # m, distance from well 1 
q_1 = Q_y1/w_1 # m^2/d, flow per unit width
h_y1 = hy1_w1-(q_1/(K_1*m_1))*w_2 # head at 0.3 Km from Well 1, using the second equation 


#output
print("The daily discharge from the aquifer is: {0:1.2f}".format(Q_y1), "m\u00b3/d")
print("The head at 0.3 Km from well 1 is : {0:1.2f}".format(h_y1), "m")


# ## Tutorial problem 21
# 
# Presented below in the figure is the available information of an aquifer cross-section. The aquifer is confined and of variable thickness across the cross-section.<br>
# It has a uniform conductivity of $5.6 \times 10^{-5} \frac{m}{s}$. The total Discharge from the aquifer of width $500 m$ is required to be obtained.<br>
# <br>
# <img src="images/T06_Y2.png" width=500>

# ### Tutorial Problem 21 - Solution (1)
# 
# The aquifer is confined but of variable thickness, hence $T = Kb$, cannot be used. In this case we need to find a representative aquifer thickness. This is simple if it can be assumed that a slope decreases linearly throughout its length. So, we can write for a representative $m$
# 
# $$ m = \frac{m_3-m_1}{L}x + m_1  \qquad\qquad \text{(eq. 2A)} $$
# 
# where $x$ is a lengthwise distance of $m$ from $m_{1}$. Equation above is simply an equation of straight line $y = ax + c$, in which slope $a = \frac{m_{3}-m_{1}}{L} $ and $c = m_{1}$.
# 
# Now Darcy law can be used to obtain discharge per unit width ($q'$). 
# 
# $$ q' = -bK\frac{dh}{dx} \qquad\qquad \text{(eq. 2B)} $$
# 
# with conductivity $K$ and hydraulic head gradient $dh/dx$. We substitute $b$ from eq. (2A) to eq. (2B)
# $$ q' = -\Bigg(\frac{m_3-m_1}{L}x + m_1\Bigg) \cdot K\frac{dh}{dx}  \qquad\qquad \text{(eq. 2C)} $$
# 
# Rearranging eq. (2C) we get
# $$ -dh = \frac{q'}{K}\cdot \frac{dx}{\frac{m_3 - m_1}{L}x+m_1} \qquad\qquad \text{(eq. 2D)} $$
# 
# Differential equation Eq. (2D) has to be solved to obtain the discharge.

# ### Tutorial Problem 21 - Solution (2)
# 
# Eq. (2D) is a variable separated differential equation, so direct integration can be done with the following hydraulic (boundary) conditions:
# $$ \text{for } x = 0,  \; h = h_1 \qquad \text{and}\qquad \text{for } x = L, \; h = h_3 $$
# 
# i.e.,
# $$ -\int_{h_1}^{h_3} dh = \frac{q'}{K}\cdot\int_0^L \frac{dx}{\frac{m_3-m_1}{L}x + m_1} \qquad \qquad \text{eq. (2E)} $$
# 
# The integral on the right hand side of eq. (2E) is an elementary integral the solution of which is of the form:
# $$ \int\frac{dx}{ax + b} = \frac{1}{a}\ln(ax+b) + C $$
# based on this, the solution of eq. (2E) will be
# $$ h_1 - h_3 = \frac{q'}{K} \frac{1}{\frac{m_3-m_1}{L}}\cdot\Bigg[\ln\Bigg(\frac{m_3-m_1}{L}L + m_1 \Bigg) - \ln\Bigg(\frac{m_3-m_1}{0}0 + m_1 \Bigg)\Bigg] $$
# Simplifying which we get
# $$ h_1 - h_3  = \frac{q'}{K}\cdot \frac{L}{m_3-m_1}\cdot \ln\frac{m_3}{m_1} $$
# Then, $q'$ the unit aquifer width discharge can be obtained from
# $$ q' = K \frac{h_1- h_3}{L}\cdot\frac{m_3 - m_1}{\ln\frac{m_3}{m_1}} \qquad \qquad \text{eq. (2F)} $$
# 

# In[4]:


#Tutorial Problem Y2 – Continued
# given
h2_1 = 290 # m, head in Well 1
h2_3 = 275 # m, head in the river end
m2_1 = 6 # m, aquifer thickness at well 1
m2_3 = 20 # m, aquifer thickness near river end
K2 = 5.6 * 10**-6 # m/s, conductivity of aquifer
L2 = 700 # m, length of the river cross-section
W2 = 500 # m, Width of aquifer

# solution 
# Discharge per unit width using eq. 2F
q2 = K2*((h2_1 - h2_3)/L2)*(m2_3 - m2_1)/np.log(m2_3/m2_1) 
Q2 = q2*W2 

#output
print("Discharge per unit width of aquifer is: {0:1.2e}".format(q2), "m\u00b2/s \n")
print("Discharge from the given width of aquifer is: {0:1.2e}".format(Q2), "m\u00b3/s")


# ## Tutorial Problems on Flow in Unconfined Aquifers

# ## Tutorial Problem 22
# 
# Discharge from an unconfined aquifer presented in the figure below in wich $h_{1} = 20m$, $h_{2} = 18 m$ and $L = 50 m$ is to be obtained. Other information available are that the aquifer is $30 m$ wide and has a uniform conductivity $K = 5 \times 10^{-6} \frac{m}{s}$. <br>
# Also known are that the Duipuit assumptions (check here: [Dupuit-Forchheimer-assumption](https://en.wikipedia.org/wiki/Dupuit-Forchheimer_assumption)) applies to this unconfined aquifer.<br>
# <br>
# <img src="images/T06_Y3.png" width=400>

# ### Tutorial Problem 22 - Solution
# 
# As Dupuit assumptions are valid, the discharge per unit width of aquifer ($q'$) 
# can be obtained from
# 
# $$ q' = -K \cdot h \cdot\frac{dh}{dx} \qquad\qquad \text{eq. (3A)} $$
# 
# where $h$ is saturated thickness of aquifer located at $x$ distance from $h_{1}$ end.
# From figure, at $x = 0$, $h = h_{1}$ and at $x = L$, $ h = h_{2}$. Based on this
# differential equation eq. (3A) can be directly integrated after separation of variable to obtain $q'$, i.e.,
# 
# $$ \int_0^L q' \cdot dx = -K \cdot \int_{h_1}^{h_2}h dh $$
# 
# Integration leads to
# 
# $$ q' \cdot x\Big|^L_0 = -K\frac{h^2}{2}\Big|_{h_1}^{h^2} $$
# 
# resulting to 
# 
# $$ q' \cdot L = -K \cdot \Bigg( \frac{h_2^2}{2} - \frac{h_1^2}{2}\Bigg) $$
# 
# and $q'$ is then obtained from
# 
# $$ q' = -\frac{1}{2}K \cdot \Bigg( \frac{h_2^2 -h_1^2 }{L}\Bigg) \qquad\qquad \text{eq. (3B)} $$

# In[5]:


#Solution of Tutorial Problem 22:
# Given

h3_1 = 20 # m, aquifer head at point 1
h3_2 = 10 # m, aquifer head at point 1
K3 = 5 * 10**-6 # m/s uniform conductivity of aquifer
L3 = 50 # m, length of the aquifer
W3 = 30 # m, width of the aquifer

#Calculation
q3 = -1/2*K3*(h3_2**2 - h3_1**2)/L3 # m^2/s, unit width discharge using eq. 3B
Q3 = q3 * W3 # m^3/s, total dischage from given width

#output
print("Discharge per unit width of aquifer is: {0:1.2e}".format(q3), "m\u00b2/s \n")
print("Discharge from the given width of aquifer is: {0:1.2e}".format(Q3), "m\u00b3/s")


# ## Tutorial problem 23
# 
# In a schematic below an unconfined aquifer is found to divide 2 rivers of differnt stages $h_{1} = 30 m$ and $h_{2} = 10 m$. The aquifer of length $L = 50 m$ and with uniform conductivity $K = 5\times 10^{-6} \frac{m}{s}$ is found to receive recharge at the rate ($w$) of $0.01 \frac{m}{d}$. <br>
# 
#     a) What will be the hydraulic head and discharge per unit width ($q'$) in the aquifer at $5 m$ from the left river.
# 
#     b) What will the head at the same location when aquifer receives no recharge.
# 
# <br><br>
# <img src="images/T06_Y4.png" width=500>

# ### Tutorial Problem 23 - Solution
# 
# For an unconfined aquifer, the case here, the water table = hydraulic head. For a condition as in this problem the height 
# of the water table $h$ as a function of position $x$ can be obtained from the following expression provided in Fetter (2014):
# $$ h = \sqrt{h_1^2 - \frac{(h_1^2- h_2^2)x}{L} + \frac{w}{K}(L-x)x} \quad\quad \text{eq. (4A)} $$
# 
# From whhich discharge per unit width $(q')$ can be obtained by differentiating eq. (4A) with respect to $x$, 
# as from Darcy Law $q' = -Kh (dh/dx)$ for unconfined aquifer. Thus we get (from Fetter (2014), 
# $$ q'(x) = \frac{K (h_1^2 - h_2^2)}{2L}- w\Bigg(\frac{L}{2}-x\Bigg) \quad\quad \text{eq. (4B)} $$
# 
# For the case when $w= 0$, the last term under the square root in eq. (4A) becomes 0, and then $h$ is 
# $$ h = \sqrt{h_1^2 - \frac{(h_1^2- h_2^2)x}{L}} \quad\quad \text{eq. (4C)} $$

# In[6]:


#Solution of Tutorial Problem 23:
# Given

h4_1 = 30 # m, River 1 stage 
h4_2 = 10 # m, River 2 stage
K4 = 5 * 10**-4 # m/s uniform conductivity of aquifer
L4 = 50 # m, length of the aquifer
w4 = 0.01/(24*3600) # m/s recharge rate in the aquifer
x4 = 5 # m, loaction at which water table is to be found 

#Calculation part a
h4_w = np.sqrt(h4_1**2 - ((h4_1**2 - h4_2**2)*x4)/L4 + (w4/K4)*(L4-x4)*x4) # head at x = 5 m from eq. 4A
q4 = K4*((h4_1**2- h4_2**2)/2*L4) - w4*((L4/2)-x4)     # m^2/s, total dischage from given width

#Calculation part b
h4_nw = np.sqrt(h4_1**2 - ((h4_1**2 - h4_2**2)*x4)/L4)


#output
print("The water table at the required  location (x) with recharge is: {0:1.5f}".format(h4_w), "m \n")
print("Discharge per unit width from the aquifer is: {0:1.2f}".format(q4), "m\u00b2/s \n")
print("The water table at the required  location (x) without recharge is: {0:1.5f}".format(h4_nw), "m ")


# In[ ]:




