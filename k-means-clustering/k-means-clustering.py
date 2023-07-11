import numpy as np
import math

# Define the points
point1 = np.array([1.0, 1.5])
point2 = np.array([1.0, 4.5])
point3 = np.array([2.0, 1.5])
point4 = np.array([2.0, 3.5])
point5 = np.array([3.0, 2.5])
point6 = np.array([5.0, 6.5])

points = {"p1_p2": point1, "p1_p3": point2, "p1_p4": point3, "p1_p5": point4, "p1_p6": point5}

# Calculate Euclidean distance between point1 and all other points
euclidean_distance = {k: np.linalg.norm(v - point1) for k, v in points.items()}

# Print the Euclidean distances
for k, v in euclidean_distance.items():
    print(f"{k}: {v}")

# Assign the cluster centers
C1 = point1
C2 = point3

# Compute the Euclidean distance from each point to C1 and C2
# Choose the smaller value of C1 and C2.
distances_c1 = [np.linalg.norm(point - C1) for point in [point1, point2, point3, point4, point5, point6]]
distances_c2 = [np.linalg.norm(point - C2) for point in [point1, point2, point3, point4, point5, point6]]

print("Euclidean Distance for C1:", distances_c1)
print("Euclidean Distance for C2:", distances_c2)

# Compute new C1 and C2
New_C1 = np.mean([point1, point2, point3], axis=0)
New_C2 = np.mean([point4, point5, point6], axis=0)

print("New C1:", New_C1)
print("New C2:", New_C2)

"""
Output:

p1_p2: 0.0
p1_p3: 3.0
p1_p4: 1.0
p1_p5: 2.23606797749979
p1_p6: 2.23606797749979
Euclidean Distance for C1: [0.0, 3.0, 1.0, 2.23606797749979, 2.23606797749979, 6.4031242374328485]
Euclidean Distance for C2: [1.0, 3.1622776601683795, 0.0, 2.0, 1.4142135623730951, 5.830951894845301]
New C1: [1.33333333 2.5       ]
New C2: [3.33333333 4.16666667]
""

