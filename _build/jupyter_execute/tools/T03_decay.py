#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
import pandas as pd 


# In[2]:


# Input 
n_simulation = 21 # choose the number of simulation
A_0 = 1000.0 # g, mass of A at t=0
B_0 = 50.0 # g, mass of B at t=0
C_0 = 10.0 # g, mass of C at t=0
R_A = 0.1 # g/a, decay rate for A
R_B = 0.2 # g/a, decay rate for B
time  = np.arange(n_simulation) # simulation time = number of simulation at 1 (time unit) interval

#initialization
A = np.zeros(n_simulation)
B = np.zeros(n_simulation)
C = np.zeros(n_simulation) 
A[0] = A_0 
B[0] = B_0
C[0] = C_0

# computation
for i in range(0,n_simulation-1):
    A[i+1] = A[i]-R_A*A[i]
    B[i+1] = B[i]+R_A*A[i]-R_B*B[i] 
    C[i+1] = C[i]+R_B*B[i]
    summ = A[i]+B[i]+C[i]  

# Output

d = {"Mass_A": A, "Mass_B": B, "Mass_C": C, "Total Mass": summ}
df = pd.DataFrame(d) # Generating result table
label = ["Mass A (g)", "Mass B (g)", "Mass C (g)"]
fig = plt.figure(figsize=(9,6))
plt.plot(time, A, time, B, time, C, linewidth=3);  # plotting the results
plt.xlabel("Time [Time Unit]"); plt.ylabel("Mass [g]") # placing axis labels
plt.legend(label, loc=0);plt.grid(); plt.xlim([0,20]); plt.ylim(bottom=0) # legends, grids, x,y limits
plt.show() # display plot
df.round(2) #display result table with 2 decimal places 


# In[3]:


def mass_bal(n_simulation, MA, MB, MC, R_A, R_B):
    
    A = np.zeros(n_simulation)
    B = np.zeros(n_simulation)
    C = np.zeros(n_simulation) 
    
    for i in range(0,n_simulation-1):
        A[0] = MA
        B[0] = MB
        C[0] = MC
        A[i+1] = A[i]-R_A*A[i]
        B[i+1] = B[i]+R_A*A[i]-R_B*B[i] 
        C[i+1] = C[i]+R_B*B[i]
        summ = A[i]+B[i]+C[i]
        
    d = {"Mass_A": A, "Mass_B": B, "Mass_C": C, "Total Mass": summ}
    df = pd.DataFrame(d) # Generating result table
    label = ["Mass A (g)", "Mass B (g)", "Mass C (g)"]
    fig = plt.figure(figsize=(6,4))
    plt.plot(time, A, time, B, time, C, linewidth=3);  # plotting the results
    plt.xlabel("Time [Time Unit]"); plt.ylabel("Mass [g]") # placing axis labels
    plt.legend(label, loc=0);plt.grid(); plt.xlim([0,20]); plt.ylim(bottom=0) # legends, grids, x,y limits
    plt.show() # display plot
    
    return df.round(2) 


# In[4]:


mass_bal(21,1000, 20, 20, 0.3, 0.2)


# In[ ]:




