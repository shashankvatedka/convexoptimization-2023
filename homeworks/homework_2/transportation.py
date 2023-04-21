import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cp


m = 3
n = 4

# compute C
C = np.zeros([m,n])
for i in range(m):
    for j in range(n):
        C[i,j] =  1 + np.abs(i-j)

alpha = np.array([3,4,5])
beta = np.array([2.5,2.5,3.5,3.5])


"""
Code for solving the primal problem
"""
#define the variable
X = cp.Variable([m,n])
#objective is to minimize the total cost
objective = cp.Minimize(cp.sum(cp.multiply(C,X)))
# constraints: supply and demand constraints, and nonnegativity
constraints = [ X>=0, cp.sum(X,axis=1)<=alpha, cp.sum(X,axis=0)>=beta ]
prob = cp.Problem(objective, constraints)
opt_value = prob.solve()

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("C = \n",C)
print("alpha = ",alpha)
print("beta = ",beta)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("\n*** Primal Problem Solution ***")
print("Optimal cost: ",opt_value)
print("Optimal transport allocation:\n",X.value)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")


"""
Code for solving the dual problem
"""
# define two sets of variables, corresponding to alpha constraints and beta constraints
U = cp.Variable(n)
V = cp.Variable(m)
#objective
dual_objective = cp.Maximize( -cp.sum(cp.multiply(beta,U)) + cp.sum(cp.multiply(alpha,V)) )
#constraints
Atransposej = np.zeros([m*n,n])
Atransposei = np.zeros([m*n,m])
Cvec = np.zeros(m*n)
for i in range(m):
    for j in range(n):
        Cvec[i+m*j] = C[i,j]
        Atransposej[i+m*j,j] = 1
        Atransposei[i+m*j,i] = -1

dual_constraints = [ U>=0, V>=0, Atransposej@U + Atransposei@V >= -Cvec]
dual_prob = cp.Problem(dual_objective, dual_constraints)
dual_opt_value = dual_prob.solve()

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("\n*** Dual Problem Solution ***")
print("Optimum value: ",dual_opt_value)
print("U_opt:\n",U.value)
print("V_opt:\n",V.value)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

#print(Cvec)
#print(Atransposei)
#print(Atransposej)

