#!/usr/bin/env python
# coding: utf-8

# # Effective hydraulic conductivity excel sheet by Dr. Liedl

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual


# In[2]:


print("Please provide the information below:  ")
def Plot_Function(L1, L2, L3, K1, K2, K3):
    TL=(L1+L2+L3)
    R1=1/(K1)
    R2=1/(K2)
    R3=1/(K3)
    W_K1=K1*(L1/(TL))
    W_K2=K2*(L2/(TL))
    W_K3=K3*(L3/(TL))
    W_R1=(L1/(TL))/K1
    W_R2=(L2/(TL))/K2
    W_R3=(L3/(TL))/K3
    R_prependicular=((R1)+(R2)+(R3))/3
    K_prependicular=(TL)/((L1/K1)+(L2/K2)+(L3/K3))
    K_parallel=float((L1*K1)+(L2*K2)+(L3*K3))/float(TL)
    R_parallel=1/K_parallel
    rel_h4=0
    rel_h3=((float(TL)/(float(L1/K1)+float(L2/K2)+float(L3/K3)))*float(1/K3))
    rel_h2=((float(TL)/(float(L1/K1)+float(L2/K2)+float(L3/K3)))*float(1/K2))+ float(rel_h3)
    rel_h1=1
    c1=0
    c2=(L1/(L1+L2+L3))+0
    c3=(L2/(L1+L2+L3))+(L1/(L1+L2+L3))
    c4=1
    rel_Q1= float(W_K1)/(float(W_K1)+float(W_K2)+float(W_K3))
    rel_Q2= float(W_K2)/(float(W_K1)+float(W_K2)+float(W_K3))
    rel_Q3= float(W_K3)/(float(W_K1)+float(W_K2)+float(W_K3))
    Head=(rel_h1, rel_h2, rel_h3, rel_h4)
    Thickness=(c1, c2, c3, c4)
    Relative_discharge=(rel_Q1, rel_Q2, rel_Q3)
    Layers=("Layer 1", "Layer 2", "Layer 3")
    dat1=([rel_h1, c1], [rel_h2, c2], [rel_h3, c3],[rel_h4, c4])
    dat2=([rel_Q1,"1"],[rel_Q2,"2"], [rel_Q3, "3"])
    # Plotting prependicular data
    plt.plot(Head,Thickness)
    plt.title("Flow Prependicular to the Layers")
    plt.xlabel("Relative thickness (-)")
    plt.ylabel("Relative head (-)")
    # Plotting lines for prependicular
    plt.axhline(y=0, color='r', linestyle=':')
    plt.axhline(y=(L1/(L1+L2+L3))+0, color='r', linestyle=':')
    plt.axhline(y=(L2/(L1+L2+L3))+(L1/(L1+L2+L3)), color='r', linestyle=':')
    plt.axhline(y=1, color='r', linestyle=':')
    # Table for prependicular
    Table1=pd.DataFrame(dat1, columns= ["Relative Head", "     Relative Thickness"])
    # Plotting for parallel flow  
    fig = plt.figure()
    ay = fig.add_axes([0,0,1,1])
    ay.bar(Layers, Relative_discharge )
    plt.title("Flow Parallel to the Layers")
    plt.ylabel("Relative discharge(-)")
    plt.xlabel("No. of layers")
    #Table for parallel
    Table2= pd.DataFrame(dat2, columns= ["Relative discharge", "   No. of Layer"])
    print("\n", "   Flow prependicular to the layers","\n","\n",  Table1,"\n","\n")  
    print("\n", "   Flow parallel to the layers","\n","\n", Table2, "\n", "\n")

style = {'description_width': 'initial'}    
Inter=widgets.interact_manual(Plot_Function, 
                       L1= widgets.FloatText(description="Layer Thickness", style=style),
                       K1= widgets.FloatText(description="Hydraulic Conductivity",style=style),
                       L2= widgets.FloatText(description="Layer Thickness", style=style),
                       K2= widgets.FloatText(description="Hydraulic Conductivity", style=style),
                       L3= widgets.FloatText(description="Layer Thickness", style=style),
                       K3= widgets.FloatText(description="Hydraulic Conductivity", style=style))


# In[ ]:




