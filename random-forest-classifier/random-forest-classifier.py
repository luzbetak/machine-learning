import numpy as np

# Random Forest Classifier

"""
NumPy arrays are used to represent the data and cost matrices. 
The calculation of Normal_TP and DoS_FN are simplified by using the np.sum() 
function to calculate the sum of all elements in an array. 
The total cost is calculated as the sum of element-wise multiplication of the 
data matrix and the cost matrix, which is equivalent to the long series of 
additions in the original Matlab code.
"""

normal = np.array([60262, 243,  78,     4,  6])
probe  = np.array([511,   3471, 184,    0,  0])
dos    = np.array([5299,  1328, 223226, 0,  0])
u2r    = np.array([168,   20,   0,      30, 10])
r2l    = np.array([14527, 294,  0,      8,  1360])

matrix = np.array([normal, probe, dos, u2r, r2l])

cost_normal = np.array([0, 1, 2, 2, 2])
cost_probe  = np.array([1, 0, 2, 2, 2])
cost_dos    = np.array([2, 1, 0, 2, 2])
cost_u2r    = np.array([3, 2, 2, 0, 2])
cost_r2l    = np.array([4, 2, 2, 2, 0])

cost_matrix = np.array([cost_normal, cost_probe, cost_dos, cost_u2r, cost_r2l])
Normal_TP   = normal[0] / np.sum(normal)
DoS_FN      = (dos[0] + dos[1] + dos[3] + dos[4]) / np.sum(dos)

# Calculate the total cost
Total_Cost = np.sum(matrix * cost_matrix)

print("Total Cost: ", Total_Cost)

# Output 
# Total Cost:  72500 

