import numpy as np

# Perceptron Learning
# Sample [val1, val2, val3, class]

Sample1 = np.array([1, 0, 0, -1])
Sample2 = np.array([1, 0, 1, 1])
weight = np.array([0.1, 0.55, 0.91])
threshold = 0.4

print("------------------ Sample 1 ------------------")

InputOutput1 = np.dot(weight, Sample1[:-1])

if InputOutput1 <= threshold:
    print(f"Sample(1) OutputNode1: {InputOutput1:.2f} <= threshold: {threshold:.2f}")
    OutputNode1 = -1
else:
    print(f"Sample(1) Fire: OutputNode1: {InputOutput1:.2f} > threshold: {threshold:.2f}")
    OutputNode1 = 1

if OutputNode1 == Sample1[3]:
    print(f"Sample(1) No Need to change weights, expected={Sample1[3]:.2f}")
else:
    print("Sample(1) Need to change weights.")

print()
print("------------------ Sample 2 ------------------")

InputOutput2 = np.dot(weight, Sample2[:-1])

if InputOutput2 <= threshold:
    print(f"Sample(2) OutputNode: {InputOutput2:.2f} <= threshold: {threshold:.2f}")
    OutputNode2 = -1
else:
    print(f"Sample(2) Fire: OutputNode: {InputOutput2:.2f} > threshold: {threshold:.2f}")
    OutputNode2 = 1

if OutputNode2 == Sample2[3]:
    print(f"Sample(2) No Need to change weights, expected={Sample2[3]:.2f}")
else:
    print("Sample(2) Need to change weights.")


# Output 
"""
------------------ Sample 1 ------------------
Sample(1) OutputNode1: 0.10 <= threshold: 0.40
Sample(1) No Need to change weights, expected=-1.00

------------------ Sample 2 ------------------
Sample(2) Fire: OutputNode: 1.01 > threshold: 0.40
Sample(2) No Need to change weights, expected=1.00
"""

