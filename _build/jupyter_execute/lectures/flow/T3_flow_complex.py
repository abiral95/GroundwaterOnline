#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import ipysheet as ips; from ipysheet import sheet, cell, calculation
import panel as pn
from scipy import stats 
pn.extension('katex', 'mathjax') 
import ipywidgets as widgets; from ipywidgets import FloatSlider, interact, interactive, interactive_output, fixed, VBox, HBox
from IPython import display
style = {"description_width" : "initial"} 
#pd.options.display.float_format = "{:,.2f}".format


# # Tutorial 4

# In this chapter:
# 
# + **solutions for homework problems 1 – 4**
# 
# + **tutorial problems on effective conductivity and flow nets**
# 
# + **homework problems on effective conductivity and flow nets**
# 
# 

# # Solutions for homework problems 1 - 4

# ## Homework Problem 1:
# 
# The pressure head in an aquifer extending over $200 km²$ is decreased by $1.60 m$. <br>
# Determine the loss of groundwater in the aquifer for two scenarios:<br>
# 
#     a) The aquifer is unconfined (storage coefficient 0.13)
# 
#     b) The aquifer is confined (storage coefficient 0.0005)
# 
# 
# <img src="images/T03_H1.png" width=350>
# <br>
# <br>
# ```{admonition} Tip
# :class: tip
# Relevant information can be found in Lecture03 - Slides 28 to 30
# ```

# ### Solution Homework Problem 1
# 
# <br><br>
# The relevant equation for this is:<br>
# $$ S = \frac{\Delta V_w}{(A\cdot \Delta H)} $$

# In[2]:


#Given data
print("Provided values are:")
A = FloatSlider(description="A [km²]", min=50, max=400, step=10.5, value="200")
D_h = FloatSlider(description="D_h [m]", min=1, max=10, step=0.5, value="1.6")
S_u = FloatSlider(description="S_u [-]", min=0.1, max=0.9, step=0.01, value="0.13")
S_c = FloatSlider(description="S_c [-]", min=1e-4, max=0.1, step=1e-5, value="5e-4", readout_format=".4f")
#calculations
def calc_DV_wu(A, S_u, D_h):
    DV_wu = (A*S_u*D_h)*10**6
    print("Change in water volume in unconfined aquifer is: {0:1.1e}".format(DV_wu), "m\u00b3")
DV_wu_out = interactive_output(calc_DV_wu, {"A":A, "S_u":S_u, "D_h":D_h})
    
def calc_DV_wc(A, S_c, D_h):
    DV_wc = A*S_c*D_h*10**6
    print("Change in water volume in confined aquifer is: {0:1.1e}".format(DV_wc),"m\u00b3")
DV_wc_out = interactive_output(calc_DV_wc, {"A":A, "S_c":S_c, "D_h":D_h})
#output
left4_1 = VBox([A, D_h, S_u, S_c])
right4_1 = VBox([DV_wu_out, DV_wc_out])
VBox([left4_1, right4_1])


# ## Homework Problem 2
# 
# Conduct a sieve analysis for a dried soil sample (see data in the table below)
# 
#     a) Draw the granulometric curve (cumulative mass distribution) and briefly characterise the sediment with regard to its major constituent(s).
# 
#     b) What is the coefficient of uniformity? 
# 

# In[3]:


#
title = ["mesh   size  [mm] ", "residue in the sieve [g] ", "∑Retained %", "Commulative Passed %"]
Size = [6.3, 2, 0.63, 0.2, 0.063, "< 0.063 /cup"]
passed = [11, 62, 288, 189, 42, 10]
s2 = ips.sheet(rows=6, columns=4, row_headers=False, column_headers=title)
ips.column(0, Size, row_start=0) 
ips.column(1, passed, row_start=0); s2 


# In[4]:


# Solution of problem 2

t_sample = np.sum(passed) # g, add the residue column to get total mass
retained_per = passed/t_sample *100 # %, # retain percentage residue/total mass
retain_per_cumsum =np.cumsum(retained_per) # get the cummulative sum of the reatined
passing_cumper = 100 - retain_per_cumsum # substract 100-cummsum to get passing % - the last column

#Output
s3 = ips.sheet(rows=6, columns=4, row_headers=False, column_headers=title)
ips.column(0, Size, row_start=0) 
ips.column(1, passed, row_start=0); 
ips.column(2, retained_per, row_start=0); 
ips.column(3, passing_cumper, row_start=0); s3 


# In[5]:


# Plotting granulometric curve

plt.rcParams['axes.linewidth']=2
plt.rcParams['grid.linestyle']='--'
plt.rcParams['grid.linewidth']=1
x = np.append([20], Size[:5]) # adding for all left over.
y = np.append([100],passing_cumper[:5])
fig = plt.figure(figsize=(9,6));
plt.plot(x, y, 'x-', color='red', lw=2.5); 
tics=x.tolist()
plt.xscale('log');lw=2.5
plt.grid(which='major', color='k', alpha=0.7) 
plt.grid(which='minor', color='k', alpha=0.3)
plt.xticks(x, tics);  
plt.yticks(np.arange(0,110,10));
#plt.title('grain size distribution (combined wet sieving and sedimentation analysis)');
plt.xlabel('grain size d [mm]');
plt.ylabel('Cummulative Passed fraction %');

plt.annotate('', xy=(0.20, 10),  xycoords='data', xytext=(0.045, 10), arrowprops=dict(arrowstyle='->', color="b", lw=2.5),ha='right', va='top',)
plt.annotate('', xy=(1.1, 60),  xycoords='data', xytext=(0.045, 60), arrowprops=dict(arrowstyle='->', color="b", lw=2.5),ha='right', va='top',)
plt.annotate(r'$d_{60}$', xy=(1, 60),  xycoords="data", xytext=(0.85, -3),color='red',size=12, arrowprops=dict(arrowstyle='<-', color="b", lw=2.5),ha='left', va='bottom',)
plt.annotate(r'$d_{10}$', xy=(0.20, 10),  xycoords='data', xytext=(0.235, 1.5),color='red',size=12, arrowprops=dict(arrowstyle='<-', color="b", lw=2.5),ha='right', va='top',)
plt.rcParams["font.weight"] = "bold"   

plt.savefig("fig6.png")

mpl_pane = pn.pane.Matplotlib(fig, dpi=144)


# In[6]:


# From the figure
d_10 = 0.22 # mm,approx, diameter 10% passing, see the arrow bottom in x-axis
d_60 = 1.0 # mm, approx diameter 10% passing, see the arrow bottom in x-axis

c_u = d_60/d_10 # [], coefficient of uniformity

#Output
print("The coefficient of uniformity is: {0:1.1f}".format(c_u)) 
r2_1 = pn.pane.Markdown("""
**Major constituents: coarse sand/medium sand** """, width=600, style={'font-size': '13pt'} )
pn.Row(r2_1) 


# # Effective conductivity and flow nets

# ## Tutorial Problem 11 - Effective hydraulic conductivity
# 
# A sandy layer withh a thickness of 2.5m is embedded between two gravel layers. Both gravel layers have a thickness <br>
# of 1.5m and a hydraulic conductivity of $3.7 \times 10^{-3}$ $\frac{m}{s}$. <br>
# Steady-state groundwater flow is parallel to the layering. A hydraulic gradient of 0.001 and an overall discharge <br>
# of $1\frac{m^{3}}{d}$ per unit width have been determined.
# <br> <br>
# 
#     a) Determine the effective hydraulic condurctivity!
# 
#     b) What is the hydraulic condurctivity of the sand layer?
# 
#     c) Which effective hydraulic conductivitywould be obtained if flow was assumed perpendicular to the layering?
# 
#     d) Calculate effective hydraulic conductivity if the angle between the flow direction and the layering equals 45\circ!
# 
# ```{admonition} Tip
# :class: tip
# For details check Lecture05 - Slides 8-13 and 22
# ```

# ### Problem 11 - Solution
# <br>
# <img src="images/T03_TP11_a.png" width=400>
# <br><br>
# Known relationships are: <br>
# 
# $$ Q = W \cdot m \cdot K \cdot \frac{\Delta H}{L}$$
# $$K = \frac{Q/W}{m \cdot \Delta H \cdot L}$$
# Weighted arithmetic mean to determine hydraulic conductivity for sand: <br>
# 
# $$ K = \frac{1}{m} \cdot \sum_{i=1}^{n} (m_{i} \cdot K_{i})$$
# 
# Where $i$ is different layers.

# In[7]:


#Given Solution of 11 a, b

Q = 2 # m^3/d, discharge
W = 1 # m, per unit width
K_g = 3.7*1E-3# m/s, conductivity of gravel layer 
m_g = 1.5 # m, thickness of gravel layer
m_s = 2.5 # m, thickness of sand layer
m = 2*m_g + m_s # m. total thickness of aquifer
Dh_L = 0.001 # (-), hydraulic gradient


#Solution of 11a
Keff_h = (Q/W)/(m*Dh_L) # m/d, conductivity
Keff_hs = Keff_h/(24*3600)# m/s, conductivity unit changed

#Solution of 11b
# K_eff = (2*m_g*K_g + m_s*K_g)/m

K_s = ((m*Keff_hs - 2*m_g*K_g))/m_s  

print("Effective horizontal hydraulic conductivity (Keff_h) = {0:1.2f}".format(Keff_h), "m/d\n" ) 
print("Effective horizontal hydraulic conductivity (Keff_hs) = {0:1.3E}".format(Keff_hs), "m/s\n" )
print("Hydraulic conductivity of sand layer (K_s) = {0:1.1E}".format(K_s), "m/s" )     


# ### Problem 11 - Solution for c) and d)
# 
# <img src="images/T03_TP11_b.png" width=200>
# <br><br>
# Vertical effective conductivity is given by weighted harmonic mean:<br>
# 
# $$ K = \frac{m}{2 \cdot \frac{m_{g}}{K_{g}} + \frac{m_{s}}{K_{s}}} $$
# 
# <br>
# <img src="images/T03_TP11_c.png" width=200>
# <br><br>
# For inclined aquifer the effective conductivity is:<br>
# 
# $$ K = \frac{1}{\frac{\cos^{2} \cdot \theta}{K_{h}} + \frac{\sin^{2} \cdot \theta}{K_{v}}} $$
# 

# In[8]:


# Solution of 11c

Keff_v = m/(2*(m_g/K_g)+ (m_s/K_s))

#Given 
theta = 45 # theta 
theta_r = 45*(np.pi)/180 # degree to radian conversion
K_h = Keff_hs # m/s, solution from 11a
K_v = Keff_v # m/s, solution from 11c

# solution from 11d
Keff_i = 1/((np.cos(theta_r)**2/K_h)+(np.sin(theta_r)**2/K_v))


print("Effective vertical hydraulic conductivity (Keff_v) = {0:1.2E}".format(Keff_v), "m/s\n" ) 
print("Effective inclined hydraulic conductivity (Keff_i) = {0:1.2E}".format(Keff_i), "m/s" ) 


# ## Tutorial Problem 12 - Hydrologic Triangle
# 
# The figure below shows the position of four groundwater observation wells with measured hydraulic heads in m a.s.l <br>
# 
#     a) Sketch head isolines for intervals of 1m by applying the hydrologic triangle method!
# 
#     b) Indicate the flow direction!
# 
# <img src="images/T03_TP12_a.png" width=400>

# ### Tutorial Problem 12 - Solution
# 
# Step 1: Connect all the points
# <br><br>
# <img src="images/T03_TP12_b.png" width=400>
# <br><br>
# Step2: Divide the connected lines at equal head-level (here = 1m)
# <br><br>
# <img src="images/T03_TP12_c.png" width=400>
# <br><br>
# Step3: Join all the equal head lines
# <br><br>
# <img src="images/T03_TP12_d.png" width=400>
# <br><br>
# Step4: Mark the flow direction from higher to lower heads
# <br><br>
# <img src="images/T03_TP12_e.png" width=400>

# ## Tutorial Problem 13 - Flow Nets
# 
# Sketch head isolines and streamlines for the two configurations **a)** and **b)** of the well doublette shown below. <br>
# In both cases flow nets should be sketched without and with the uniform flow component.<br>
# <br>
# **a)** withdrawal at both wells:<br><br>
# <img src="images/T03_TP13_a.png" width=200>
# <br>
# **b)** Injection and withdrawal wells:<br><br>
# <img src="images/T03_TP13_b.png" width=200>

# # Homework problems on effective conductivity and flow nets
# <br><br>
# ```{note}
# There is no obligation to solve homework problems!
# ```

# ## Homework problem 5 - Effective hydraulic conductivity
# 
# A gravel layer with a thickness of $2.5m$ is embedded between two sand layers. Both sand layers have a thickness of $1.5 m$ and <br>
# a hydraulic conductivity of $3.7 \times 10^{-4} \frac{m}{s}$. Steady-state groundwater flow is perpendicular to the layering.<br>
# An overall head difference of $5.5 cm$ and a discharge of $500 \frac{L}{d}$ per unit area have determined.<br>
# 
#     a) Determine the effective hydraulic conductivity!
# 
#     b) What is the hydraulic conductivity of the gravel layer?
# 
#     c) Which effective hydraulic conductivity would be obtained if flow was assumed to be in parallel with the layering?
# 
#     d) Calculate effective hydraulic conductivityif the angle between the flow direction and the layering equals 30°!

# ## Homework Problem 6 - Hydraulic Triangle
# 
# The figure below shows the position of groundwater observation wells with measured hydraulic heads in m a.s.l.
# <br>
# 
#     a) Sketch head isolines for intervals of $1 m$ by applying the hydrologic triangle method!
# 
#     b) Indicate the flow direction!
# 
# <br><br><br>
# <img src="images/T03_TH6.png" width=400>

# ## Homework Problem 7 - Flow Nets
# 
# Sketch head isolines and streamlines for the well doublette shown below. <br>
# in this case, injection and withdrawal of groundwater is superimposed to a uniform flow component.
# <br><br><br>
# <img src="images/T03_TH7.png" width=400>

# In[ ]:




