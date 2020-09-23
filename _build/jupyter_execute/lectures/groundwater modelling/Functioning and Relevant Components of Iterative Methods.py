#!/usr/bin/env python
# coding: utf-8

# # Functioning and Relevant Components of Iterative Methods #
# 
# ---

# ## Motivation
# 
# In order to be capable of simulating groundwater flow with the help of computer models, a **system of equations** must be solved. As a result head values are calculated for each model cell.
# 
# Each equation is based on the **conservation of volume** (for each cell) and **Darcy‘s Law** (for flow between adjacent cells).
# 
# In most cases, Gauß elimination is not useful due to the large number of equations and the associated large memory requirements of the computer. Therefore **iterative solution** methods are used.
# 
# These require special input parameters to control the iterative procedure. An "optimal" parameter selection leads to an acceptable approximate solution within a few iteration steps. However, there is no guarantee that this will always be achieved.
# 

# ## Schematic Represantation of an Iterative Method
# 
# ![title](image\schematic_iterative_Method.png)
# 
# The solving of systems of finite difference equations is done by a **sequence of similar iterative steps**.
# 
# In each iteration step it is assumed that the approximate solution for the current time level is improved. This “update“ is **based on the intermediate result of the pre-vious iterative step**.
# The fourth index v counts the iteration steps, which is usually written in superscript.

# ## Componentes of an Iterative Method

# ### Starting Value
# 
# The start value corresponds to the value for the iteration step **v = 0**.
# 
# For **transient problems**, the initial values are usually identical with the results of the previous time level (or with the initial values). The exception are cells with a fixed head boundary condition, since the heads are known at time level k and thus make an update unnecessary.
# 
# For **stationary problems**, the initial values must be estimated in advance. This can be done by using the initial values provided by the software, by transient modelling which approximates the steady state, or by estimating the values based on previous experience.

# ### Error Criterion 
# 
# There are two ways to end the iteration. Either the iteration is stopped when the **maximum number of iteration steps $v_{max}$** is reached, or it is terminated if the differences in the results of two successive iteration steps are below a predefined **error tolerance $\varepsilon$**.
# Groundwater software tools include both options. 

# ### Convergence
# 
# ![title](image\Convergence.PNG)
# 
# An iterative method is convergent, if
# 
# $$ \max\limits_{i,j}|h_{ij}^{k,(v)}-h_{ij}^{k,(v-1)}|<\varepsilon $$
# 
# It should be noted that convergence does **not always imply high quality solutions**. However, the plausibility of the results can be checked e.g. via the **volumetric budget** (offered by many available software tools).
# 

# ## General Procedure
# 
# If the headers in the nodes are **fixed**, the **corresponding values** are used.
# 
# If this is **not the case**, proceed as follows:
# - define the starting values: $$h_{ij}^{k,(0)}=h_{i,j}^{k-1}$$
# - perform the iterative steps: $$v=1, 2, \dots, v_{max}$$
#     - update heads: $$h_{ij}^{k,(v-1)} \Rightarrow h_{ij}^{k,(v)}$$
#     - terminate iteratiorn if: $$\max\limits_{i,j}|h_{ij}^{k,(v)}-h_{ij}^{k,(v-1)}|<\varepsilon $$
# 
# If the iteration does not converge, an issue warning message appears.
#     

# ## How to select
# 

# ### Error Tolerance
# A decrease (increase) of the **error tolerance** leads to a larger (smaller) number of iteration steps and a larger (smaller) computing time.
# 
# The **smaller** the error tolerance, the **more accurately** the solution of the FD equations is approximated in most cases. This only applies if the iterative method remains convergent. Sometimes it is sufficient to adjust $ν_{max}$ to restore convergence. 
# 
# **Exception:** An error tolerance close to the accuracy of the computer can lead to rounding errors and correspondingly reduced quality of the solution.
# 
# **Rule of thumb:** The error tolerance should be one order of magnitude below the desired accuracy.
# 
# **Example:** *The calculation of h with an accuracy of 0.01 m requires ε = 0.001 m*
# 
# However, strong hydraulic contrasts may require a lower error tolerance.            

# ### Maximum number of iteration
# 
# The selection of the maximum number of iteration $v_{max}$ is done by:
# - default provided by the software
# - increasing the default if convergence cannot be achieved

# ## Overview of Iterative Methods and Tests

# ### Some Iterative Methods
# There is no iterative method with a general guarantee of convergence. Therefore, groundwater modelling tools usually contain a set of different methods.
# 

# In[ ]:




