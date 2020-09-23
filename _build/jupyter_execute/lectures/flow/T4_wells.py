#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import ipysheet as ips
import panel as pn
from scipy import stats 
import ipywidgets as widgets
from ipywidgets import IntSlider, interact, interactive, interactive_output, HBox, VBox, Button
pn.extension('katex', 'mathjax') 


# # Tutorial 6 #
# 
# 
# <br>
# In this chapter:
# 
# + **Homework Problems on Permeameters**
# 
# + **Tutorial Problems on Wells**
# 
# + **Homework Problems on Wells**
# 
# 

# ## Homework Problem on Permeameters

# ## Homework Problem 3
# 
#     a) Derive an expression for hydraulic conductivity K for the constant-head permeameter shown in the figure below.
# 
#     b) The hydraulic conductivity of a sample (length $L = 10cm$, diameter: $d = 4cm$) is to be determined. The water depths $a_{1}$ and $a_{2}$ equal $6cm$ and $3cm$. A water volume of $250ml$ passed the sample during an experimental period of $36s$.
# 
#     c) Which material could be contained in the sample?
# 
# <br>
# <img src="images/T02_TH3.png" width=500>
# <br><br>
# 
# ```{admonition} Tip
# :class: tip
# For more information chechk Lecture04 - Slides 14 and 15
# ```

# ### Homework Problem 3 - Solution a)
# 
# General formula for constant-head permeameter:
# 
# $$ K = \frac{Q \cdot L}{h_{in} - h_{out}} $$
# 
# The column outlet is chosen as the reference level $z = 0$ with the $z-$axis pointing up-ward. As a consequence, we have $z = L$ at the inlet.<br>
# 
# **at the outlet:**<br>
# pressure head = $a_{2}$ ; elevation head = 0 ; $h_{out} = a_{2}$<br>
# <br>
# **at the inlet:**<br>
# pressure head = $a_{1}$ ; elevation head = $L$ ; $h_{in} = a_{1}+L$<br>
# <br>
# **head difference:** $h_{in} - h_{out} = a_{1} + L - a_{2}$<br>
# <br>
# **hydraulic conductivity:** $$K = \frac{Q \cdot L}{A \cdot (a_{1} + L - a_{2})}$$
# 

# In[2]:


# Problem 3b and c, Given are:
L = 10# cm, length of column 
a1 = 6# cm, pressure head at 1 
a2 = 3# cm, pressure head at 2 
d = 4 # cm, diameter of the column
V = 250 # ml, volume of water passed 
t = 36 # s, time required


#interim calculation
A = np.pi*(d/2)**2 # cm^2 Area of the column
Q = V/t # mL/s, discharge 


#calculation
K = Q*L/(A*(a1+L-a2))# cm/s, Conductivity (note: 1cm³ = 1 mL)

#output
print("The conductivity of the column is:{0:1.3f}".format(K), "cm/s")
print("The conductivity of the column is:{0:1.3E}".format(K/100), "m/s")

r1_8 = pn.pane.Markdown("""
**The sample in the column is: _Coarse sand - Fine gravel_**
""", width=400)  

pn.Row(r1_8) 


# In[3]:


#Creating Input
L = IntSlider(description="L [cm]", min=2, max=100, step=1, value="10")
a1 = IntSlider(description="a1 [cm]", value="6", disabled=True)
a2 = IntSlider(description="a2 [cm]", value="3", disabled=True)
d = IntSlider(description="d [cm]", min=2, max=20, step=1, value="4")
V = IntSlider(description="V [mL]", min=50, max=500, step=10, value="250")
t = IntSlider(description="t [s]", min=10, max=120, step=1, value="36")
#Define calculations
def calc_A(d):
    A = np.pi * (d/2)**2

def calc_Q(V,t):
    Q = V / t

def calc_K(V,t,d,L):
    K = (V/t) / ((np.pi * d/2) * (6 + 3))
    print("The conductivity of the column is: {0:1.3f}".format(K), "cm/s")
def calc_K_100(V,t,d,L):
    K_100 =  ((V/t) / ((np.pi * d/2) * (6 + 3))) / 100
    print("The conductivity of the column is: {0:1.3E}".format(K_100), "m/s")
#Create Output of K
K_out = interactive_output(calc_K, {"V":V, "t":t, "d":d, "L":L})
K_100_out = interactive_output(calc_K_100, {"V":V, "t":t, "d":d, "L":L})
#Create Button to specify soiltype
button = widgets.Button(description="Specify sample soil type")
out = widgets.Output()
@out.capture()
def on_button_clicked(button, K_100):
    with out:
        if(K_100 > 0.03 and K_100 > 0.0003):
            if(K_100 < 6*10**-3 and K_100 > 3*10**-4):
                print("The sample in the column is: _Fine gravel - Coarse sand_")
            else : print("The sample in the column is: _Gravel_")
        elif(K_100 < 6*10**-3 and K_100 > 9*10**-7):
            if(K_100 < 5*10**-4 and K_100 > 9*10**-7):
                print("The sample in the column is: _Medium sand - Coarse sand_")
            else: print("The sample in the column is: _Coarse sand_")
        elif(K_100 < 5*10**-4 and K_100 > 9*10**-7):
            if(K_100 < 2*10**-4 and K_100 > 2*10**-7):
                print("The sample in the column is: _Medium sand - Fine sand_")
            else: print("The sample in the column is: _Medium sand_")
        elif(K_100 < 2*10**-4 and K_100 > 2*10**-7):
            if(K_100 < 2*10**-5 and K_100 > 2*10**-7):
                print("The sample in the column is: _Fine sand - Silt,loess_")
            else: print("The sample in the column is: _Fine sand_")
        elif(K_100 < 2*10**-5 and K_100 > 1*10**-9):
            if(K_100 < 2*10**-6 and K_100 > 1*10**-9):
                print("The sample in the column is: _Silt,loess - Till_")
            else: print("The sample in the column is: _Silt,loess_")
        elif(K_100 < 2*10**-6 and K_100 > 1*10**-12):
            if(K_100 < 4.7*10**-9 and K_100 > 1*10**-12):
                print("The sample in the column is: _Till - Clay_")
            else: print("The sample in the column is: _Till_")
        elif(K_100 < 4.7*10**-9 and K_100 > 1*10**-11):
            print("The sample in the column is: _Clay_")
button.on_click(on_button_clicked)
#planned was to get the output of the defined function for soiltype-decision from above.on_button_clicked
#something went wrong, so the button does not do anything. maybe yo can find a solution for this problem?
#Create output
display(button)
tleft6_3 = VBox([L, d, V, t])
tright6_3 = VBox([a1, a2])
top6_3 = HBox([tleft6_3, tright6_3])
bleft6_3 = VBox([K_out, K_100_out])
bright6_3 = out
bot6_3 = HBox([bleft6_3, bright6_3])
bot6_3 = bleft6_3
VBox([top6_3, bot6_3])


# ## Homework Problem 4
# 
# A Darcy experiment is perfomed by a falling-head permeameter using water at $\theta = 20°C$. <br>
# Length and diameter of the sample are $L_{sample} = 20cm$ and $d_{sample} = 6cm$, respectively. The inner tube diameter is $d_{inner} = 4cm$.<br>
# The following data are available for the time-dependent hydraulic head difference:<br>
# 
# <img src="images/T02_TH4a.png" width=400>
# 
#     a) Convert times to seconds and plot the logarithm of the ratios of head differences $ln(\frac{\delta h_{0}}{\delta h_{t}})$ vs. time t!
# 
#     b) Determine the slope of the corresponding regression line!
# 
#     c) Determine hydraulic conductivity K!
# 
#     d) Determine intrinsic permeability k!
# 
# ```{admonition} Tip
# :class: tip
# More information on this topic can be found at Lecture04 - Slide 16
# ```

# ### Homework Problem 4 - Solution
# 
# <img src="images/T02_TP10.png" width=350>
# <br><br>
# The formula for variable-head permeameter:
# 
# $$ K = \frac{d_{t}^{2} \cdot L}{d_{t}^{2} \cdot t} \cdot \ln\Bigg(\frac{h_{in,0} - h_{out}}{h_{in,t} - h_{out}}\Bigg) = \frac{d_{t}^{2} \cdot L}{d_{c}^{2} \cdot t} \cdot \ln\Bigg(\frac{\Delta h_{0}}{\Delta h_{t}}\Bigg) $$
# 
# Rearrangement shows that the natural logarithm of $\frac{\Delta h_{0}}{\Delta h_{t}}$ depends lineraly on time $t$:
# 
# $$ \ln\Bigg(\frac{\Delta h_{0}}{\Delta h_{t}}\Bigg) = \frac{K \cdot d_{c}^{2}}{L \cdot d_{t}^{2}} \cdot t $$
# 
# $$\text{slope} = \frac{K \cdot d_{c}^{2}}{L \cdot d_{t}^{2}} $$
# 
# $$ K = L \cdot \frac{d_{t}^{2}}{d_{c}^{2}} \cdot \text{slope} $$
# 
# ```{note}
# t [min] as given time <br>
# $D_{h}$ [cm] as head difference
# ```

# In[4]:


#Given Data
t = np.array([0, 5, 18, 23, 27, 29])
Dh = np.array([36.9, 33.6, 26.3, 23.9, 22.1, 21.3])
#Caclulation
t_s = t*60 # s, time in second
Dh0_Dht = Dh[0]/Dh # (-), Delta h(0)/Delta h(t)
ln_Dhodht = np.log(Dh0_Dht)# (-), ln(Delta h(0)/Delta h(t))
slope, intercept, r_value, p_value, std_err = stats.linregress(t_s, ln_Dhodht) # linear regression
#Plot the results
fig = plt.figure()
plt.plot(t_s, ln_Dhodht, 'x', label=' provided data');
pred = intercept + slope*t_s
plt.plot(t_s, pred, 'r', label='y={:.2E}x+{:.2E}'.format(slope,intercept)) ;
plt.xlabel(r"$t (s)$");
plt.ylabel(r"$\ln\frac{\Delta h (0)}{\Delta h (t)}\;\:(-)$");
plt.grid();
plt.legend(fontsize=11) 
plt.text(150, 0.42,'$R^2 = %0.2f$' % r_value)
plt.close() # otherwise we have 2 figure
r2_2 = pn.pane.Matplotlib(fig, dpi=144)
pn.Row(r2_2)  


# In[5]:


#
#Solution of 4C
# Given 
L = 20 # cm, Length of the column
d_t = 4 # cm, diameter of the tube
d_c = 6# cm, diameter of the column
slope = slope # obtained from the fit equation

K = L*(d_t**2/d_c**2)*slope # cm/s, conductivity calculated using eqn from previous slide

print("The conductivity in the column is: {0:1.2E}".format(K), "cm/s\n")
print("The conductivity in the column is: {0:1.2E}".format(K/100), "m/s\n")

#Solution of 4D
# Given
rho_w = 998.2 # kg/m^3, density of water
eta_w = 1.0087E-3# kg/(m-s), viscocity of water
g = 9.81 # m/s^2, accl. due to gravity

k = K/100*eta_w/(rho_w*g)# m^2, K = k*ρ/n
k_D = k/0.987E-12 # D, 1D = 0.987E10-12 m^2

print("The permeability of the media is: {0:1.2E}".format(k), "m\u00b2 \n")  
print("The permeability of the media in Darcy's unit is: {0:1.2f}".format(k_D), "D")  


# # Tutorial 6 - Problems on Wells

# ## Tutorial Problem 18
# 
# A pumping test was conducted with a constant water withdrawal rate of $9 \frac{m^{3}}{h}.$ The table shows the time-drawdown series recorded at an observation well wich is located $9.85m$ apart from the pumping well. The aquifer thickness is $5m.$<br>
# Determine the storage coefficient, the transmissivity and the hydraulic conductivity by using the Theis method!<br>
# To this end, it is necessary to complete the table below such that data are made available for further steps (see next page).
# <br><br>
# 
# ```{admonition} Tip
# :class: tip
# For more information on this problem see Lecture07 - Slides 29-33
# ```

# In[6]:


#Provided data set
df_t1 =np.array([1, 2,    3,    4,    5,    7,    9,   12,   18,   23,   33, 41,   56,  126,  636, 1896])
df_s1 = np.array([0.01, 0.03, 0.05, 0.06, 0.07, 0.09, 0.12, 0.14, 0.16, 0.17, 0.18, 0.19, 0.2 , 0.22, 0.3 , 0.32])

d = {'time [min]': df_t1, 'drawdown [m]': df_s1}
df = pd.DataFrame(data=d, index=None)
df


# ### Tutorial Problem 18 - Solution
# 
# As a first approach, the graphical solution of the problem  is to be determined, i.e. double-logarithmic data and type curve sheets are compared as follows:<br>
# 
#     1. Plot data for $s$ vs. $\frac{t}{r^{2}}$ in the data sheet.
# 
#     2. Determine coordinates of the match point $A$ on the type curve sheet, e.g. $\frac{1}{u_{A}} = 1$ and $W_{A} = 1.$
# 
#     3. Put the data sheet on top of the type curve sheet and shift it in parallel to the coordinate axes until data points fall on the type curve as close as possible.
# 
#     4. Determine coordinates of the match point $A$ on the data sheet.

# In[7]:


#Given data in this problem
r = 9.85 # m, observation well distance
t_s = df_t1*60 # s, converting time in s
t_r2 = t_s/r**2# s/m^2,  finding t/r^2 

#output
d2= {'time [min]': df_t1, 'drawdown [m]': df_s1, "t/r2 (s/m^2)": t_r2}  
df2 = pd.DataFrame(data=d2, index=None) 
print("With an observation well distance r = 9.85m we get:")
df2


# In[8]:


# Given in this problem

Q = 9 # m^3/h, discharge
i_ua = 1 # (-), 1/U_a
W_a = 1 #, (-), Well function W(u)
t_r2m = 0.6 # s/m^2, t/r^2 obtained from data matching with the typ curve
s = 0.06 # m, drawdown, obtained from data matching with the typ curve
m = 5 # m, aquifer thickness

# Compute
T = Q*W_a/(3600*(4*np.pi*s)) # m^2/s, transmissivity, T= Q.Wa/(4.pi.s). /3600 for hr-s
S = (4*T*t_r2m)/i_ua #(-), Storage coeff.
K = T/m # m/s, conductivity

#output
print("The Transmissivity at the site is: {0:1.2E}".format(T), "m\u00b2/s\n")
print("The Storage coefficient at the site is: {0:1.2E}".format(S),"\n") 
print("The Conductivity at the site is: {0:1.2E}".format(K), "m/s")  


# In[9]:


#
# Typ curve
#code to find W(u) (see L07/S-31) using the infinite series W(u) = -0.5772-log(u)+u-u^2/(2*2!)+u^3/(3*3!)-... (100 terms) 
# It is possible to use: from scipy.special import expi def W(u):  return  -expi(-u)

# W(u) = -0.5772-log(u)+u-u^2/(2*2!)+u^3/(3*3!)-... (100 terms) 

def W(u):  
    w = -0.5772 -np.log(u) + u
    a = u
    for n in range(1, 100):
        a = -a * u * n / (n+1)**2 # new term (next term)
        w += a  # w = w+a
        return w
        
u_1 = np.logspace(10,-1,250, base=10.0) # setting the value of u
w_u =W(1/u_1) # finding W(1/u) : as we use 1/u in the typ curce
        
plt.figure(figsize=(9,6)) 
plt.loglog(u_1, w_u) 
plt.title("The typ curve"); plt.ylim((0.1, 10)); plt.xlim(1, 1e5)
plt.grid(True, which="both",ls="-"); plt.ylabel(r"W(u)");plt.xlabel(r"1/u") ;


# In[10]:


# Solution from typ curve (extra code)

# Data to fit
p_r = 9/3600 # m^3/s, pumping rate /3600 for unit /h- /s
r = 9.85 # m, distance of observation well
m = 5 # m, aquifer thickness
d_s = df_s1 # m, drawdown data

# Obtained from graphical method
S_C = 7.97e-03 # (-), storage coeff.
T = 0.00332 # m^2/s, transmissivity
K_aq = T/m

#Calculations
u_1d = 4*T*t_s/(S_C*r**2)  
w_ud = 4*np.pi*d_s*T/p_r

# plots
u_1 = np.logspace(10,-1,250, base=10.0)
w_u =W(1/u_1) 
        
plt.figure(figsize=(9,6)) 
plt.loglog(u_1, w_u) 
plt.loglog(u_1d, w_ud, "o", color="red"  )
plt.ylim((0.1, 10))
plt.xlim(1, 1e5)
plt.grid(True, which="both",ls="-") 
plt.ylabel(r"W(u)");
plt.xlabel(r"1/u") ;


# In[11]:


# Additional Code  interactive one

from ipywidgets import interact # for interactive plot with slider
from scipy.special import expi # easily obtain well function

def W(u):  
    return  -expi(-u)

def f(T, S_C, r, Q):
    
    #data that can be changed
    d_s = np.array([0.01, 0.03, 0.05, 0.06, 0.07, 0.09, 0.12, 0.14, 0.16, 0.17, 0.18,
       0.19, 0.2 , 0.22, 0.3 , 0.32])
    
    t_s = np.array([60, 120,    180,    240,    300,    420,    540,    720, 
                    1080,   1380,   1980,   2460,   3360,   7560,  38160, 113760])
    
    # calculated function see L07-slide 31
    u_1d = 4*T*t_s/(S_C*r**2) # calculating 1/u
    w_ud = 4*np.pi*d_s*T/Q   # well function

    # plots

    
    u_1 = np.logspace(10,-1,250, base=10.0)
    w_u =W(1/u_1) 
    
    plt.figure(figsize=(9,6));plt.loglog(u_1, w_u); plt.loglog(u_1d, w_ud, "o", color="red"  )
    plt.ylim((0.1, 10));plt.xlim(1, 1e5)
    plt.grid(True, which="both",ls="-") 
    plt.ylabel(r"W(u)");plt.xlabel(r"1/u")


# In[12]:



f(0.0033, 7e-3, 7, 0.003) 
#interactive_plot = interact(f(0.033, 8e-3, 7, 0.003), T=(0.0005, 0.05, 0.002), S_C=(0.00005, 0.05, 0.0001), r= (1.0,15.0, 1 ), Q=(0.0005, 0.05, 0.002))


# ## Tutorial Problem 19
# 
# A pumping test is conducted in a confined aquifer with thickness $m = 14.65m.$<br>
# The pumping rate is kept constant at $Q = 50 \frac{m^{3}}{h}$ and the corresponding drawdown $S$ is recorded in an observation well at<br>
# a distance $r = 251.32m$ from the pumping well (see table).
# 
#     1. Determine storage coefficient $S$, transmissivity $T$ and hydraulic conductivity $K$ by employing the theis method (graphical solution).
# 
#     2. What is the drawdown in the pumping well (radius including gravel pack: $r_{w} = 0.3m$) after $500min$ ?
# 
#     3. How big is the radius of influence acording to Siechardt's equation?
# 
# <br><br>
# 
# ```{admonition} Tip
# :class: tip
# For more information on this problem see Lecture07 - Slides 29-33
# ```
# <br>
# 
# ```{note}
# Use the approximation W(u) = -0.5772 - ln(u) + u ; Which is valid for u << 1
# ``` 

# In[13]:


#Given data
data19 = pd.read_csv("T06_P19_data.csv", sep=",", header=None)
d19_tm = np.array(data19[0])
d19_s = np.array(data19[1])
d19 = {"Time [min]":d19_tm, "Drawdown [m]":d19_s}
df19 = pd.DataFrame(d19)

r = 251.32
t19_s = d19_tm * 60
t19_r2 = t19_s / r**2


# ### Tutorial Problem 19 - Solution (1)
# 
# 1. Determine storage coefficient $S$, transmissivity $T$ and hydraulic conductivity $K$ by employing the Theis method (graphical solution)

# In[ ]:


# Given information
Q_19 = 50 # m^3/h, discharge per hours (change it sec)
m_19 = 14.65 # m , aquifer thickness
r_19  = 251.32 # m, distance to observation well

# Match point obtained from the type curve sheet (Manually done, you could also do by fitting)
i_u19 = 1 # (-), 1/ua
W_19a = 1 # (-), W(u)
t19_r2m = 0.004 # s/m^2, t/r^2
s_19 = 0.8 # m, drawdown

#Calculations
T_19 = (Q_19/3600)*W_19a/(4*np.pi*s_19) # m^2/s, transmissivity
S_19 = (4*T_19*t19_r2m)/i_u19 # (-), storage coefficient
K_19 = T_19/m_19 # m/s, hydraulic conductivity of the aquifer

#output
print("The Transmissivity at the site is: {0:1.2E}".format(T_19), "m\u00b2/s\n")
print("The Storage coefficient at the site is: {0:1.3E}".format(S_19), "\n")  
print("The Conductivity at the site is: {0:1.1e}".format(K_19), "m/s") 


# In[16]:


#Solution 19.  steps
r4_2 = pn.pane.Markdown("""

### Solution Steps 
1. Determine storage coefficient _S_,  transmissivity _T_ and hydraulic conductivity _K_ by employing the 
Theis method (graphical solution).
<br><br>
2. What is the drawdown in the pumping well (radius including gravel pack: _r<sub>w</sub>_ = 0.3 m) after 500 min? 
(Hint: Use the approximation _W(u) ≈ –0.5772 – lnu + u_,  which is valid for _u_ << 1) 
<br><br>
3. How big is the radius of influence according to Siechardt's equation? 

""",width = 600, style={'font-size': '13pt'})

#given
r = 251.32  # m, observation well distance
t19_s = d19_tm*60 # s, converting time in s
t19_r2 = t19_s/r**2# s/m^2,  finding t/r^2 

#output
d19_2= {'time [min]': d19_tm, 'drawdown [m]': d19_s, "t/r2 (s/m^2)": t19_r2}  
df19_2 = pd.DataFrame(data=d19_2, index=None) 

r4_3 = pn.pane.Markdown("""

### Solution of 15-1   
1. Determine storage coefficient _S_,  transmissivity _T_ and hydraulic conductivity _K_ by employing the Theis method (graphical solution).

""",width = 600, style={'font-size': '13pt'})
r4_4= pn.Column(r4_2, r4_3)
pn.Row(r4_4, df19_2)  


# ### Tutorial Problem 19 - Solution (2) 
# 
# 2. What is the drawdown in the pumping well after 500 min? 
# (Hint: Use the approximation formula $W(u) \approx -0.5772 - \ln u + u $, which is valid for $u << 1$)<br><br>
# 
# 3. How big is the raius of influence according to Siechardt's equation?

# In[18]:


# Given 
r_w = 0.3 # m, radius of the weell
t_19_2 = 500*60 # s, given time in min, converted to s.
Q_19s = Q_19/3600 # m^3/s, discharge unit converted

#Calculations
u_19 = (S_19*r_w**2)/(4*T_19*t_19_2)
W_19b = -0.5772 - np.log(u_19)+u_19
s_19b = (Q_19s*W_19b)/(4*np.pi*T_19) # see L07 - slide 32

# Solution of 15C: 
#How big is the radius of influence according to Siechardt‘s equation? (L07, slide 27)
R_19 = 3000*s_19b*np.sqrt(K_19) 

#output
print("u = {0:1.2E}".format(u_19), "\n")
print("W(u)= {0:1.2f}".format(W_19b), "\n")  
print("The drawdonw at the site is: {0:1.2f}".format(s_19b), "m\n")
print("The radius of influence is is: {0:1.2f}".format(R_19), "m")


# # Home Work Problems - Effective Conductivity and Wells
# 
# 
# ```{admonition} Tip
# :class: tip
# There is no obligation to submit the homework, if you wish to please submit within two weeks.
# ```
# 

# ## Homework Problem 8 - Effective Hydraulic Conductivity
# 
# A gravel layer with a thickness of $2.5m$ is embedded between two sand layers. Both sand layers have a thickness of $1.5m$ and a hydraulic conductivity of $3.7 \times 10^{-4} \frac{m}{s}$.<br>
# Steady-state groundwater flow is perpendicular to the layering. An overall head difference of $5.5cm$ and a discharge of $500 \frac{L}{d}$ per unit area have been determined.
# 
#     a) Determine the effective hydraulic conductivity
# 
#     b) What is the hydraulic conductivity of the gravel layer?
# 
#     c) Which effective hydraulic conductivity would be obtained if flow was assumed to be in parallel with the layering?
# 
#     d) Calculate effective hydraulic conductivity if the angle between the flow direction and the layering equals 30°.

# ## Homework Problem 9 - Pumping Test Evaluation
# 
# 
# A pumping test is conducted to determine hydraulic properties (storage coefficient $S$, the transmissivity $T$ and the hydraulic conductivity $K$) of 
# the aquifer. of a confined aquifer. For this purpose, a constant 
# pumping rate of 1219 m<sup>3</sup>/d is established and drawdown is recorded in an observation well. This problem is to be 
# solved with the Theis method implemented in the code below.<br><br>
# 
# The code generates the typ curve based on your date of birth (ddmmyyyy). To use the code, you will provide different value of $T$ and $S$ and make a match of the data with the typ-curve.
# 
# Code (2 cells below)
# 
# 

# In[41]:


# Functions to generate well-function (this is another method based on scipy library)

from scipy.special import expi
def W(u): 
    return -expi(-u)

#Generate your data and function required to solve

def data(Q, DOB, S, T):

    '''
    Q = pumping rate in m^3/s, 
    DOB- date of birth (ddmmyyyy), 
    S = Storage Coeff. and 
    T = Transmissivity (m^2/s)
    '''
    S_dob = sum(int(DOB) for DOB in str(DOB)) # add numbers in your DOB
    d_t = np.array([3.5, 5, 6.2, 8, 9.2, 12.4, 16.5, 20, 30, 60, 100, 200, 320, 380, 500])
    d_d = np.array([0.12, 0.23, 0.31, 0.41, 0.47, 0.64, 0.82, 0.92, 1.2, 1.74, 2.14, 2.57, 3, 3.1, 3.34])
    data_t = d_t/(S_dob/22)**3 # min, time based on DOB
    data_d = d_d/(S_dob/22) # m, drawdown data based on DOB
    dist = 251/(S_dob/22) # m, distance to observation well based on DOB
    Aq_t = 15/(S_dob/22) # m, aquifer thickness based on DOB
    
    i_u = (4*T*data_t*60)/(S*dist**2) 
    W_u = (4*np.pi*data_d*T)/(Q)
    return i_u, W_u


# In[42]:


#Solution 
#Q = pumping rate in m^3/s, DOB- date of birth (ddmmyyyy), S = Storage Coeff. and T = Transmissivity (m^2/s)
# Change the value in the bracket to find the fit

i_u, W_u = data(Q=2.41E-02, DOB=11071920, S=3.53e-05, T = 2.70e-03)

#interim calculation to get typ-curve
u_1 = np.logspace(10,-1,250, base=10.0) # setting the value of u
w_u =W(1/u_1) # finding W(1/u) : as we use 1/u in the typ curce

# Output
dx_1 = {"1/u":i_u, "W(u)":W_u}; dfx_a = pd.DataFrame(dx_1); figs = plt.figure(figsize=(9,6)) 
plt.loglog(u_1, w_u) # typ curve
plt.loglog(i_u, W_u, "ro" ) # your data
plt.title("The typ curve"); plt.ylim((0.1, 10)); plt.xlim(1, 1e5)
plt.grid(True, which="both",ls="-"); plt.ylabel(r"W(u)");plt.xlabel(r"1/u"); plt.close()
rx_2 = pn.pane.Matplotlib(figs, dpi=300); pn.Row(dfx_a, rx_2) 


# In[ ]:




