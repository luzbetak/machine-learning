import numpy as np

# Measures of Similarity and Dissimilarity
# ------------------------------------------------------------------------
# Cosine Similarity, Correlation, and Euclidean Distance Computation
# ------------------------------------------------------------------------

x = np.array([1, 0, 0])
y = np.array([1, 0, 1])

# Cosine Similarity
xy = np.dot(x, y)
x1 = np.linalg.norm(x)
y1 = np.linalg.norm(y)
cosine_similarity = xy / (x1 * y1)

# Covariance computation
covariance = np.dot(x - np.mean(x), y - np.mean(y)) / 2

# Standard Deviation computation
standard_dev1 = np.sqrt(np.sum((x - np.mean(x))**2) / 2)
standard_dev2 = np.sqrt(np.sum((y - np.mean(y))**2) / 2)

# Correlation Similarity computation
correlation_similarity = covariance / (np.std(x) * np.std(y))

# Euclidean Distance computation
euclidean_distance = np.linalg.norm(x - y)

print(f"Cosine Similarity: {cosine_similarity:.4f}")
print(f"Covariance: {covariance:.4f}")
print(f"Standard Deviation 1: {standard_dev1:.4f}")
print(f"Standard Deviation 2: {standard_dev2:.4f}")
print(f"Correlation Similarity: {correlation_similarity:.4f}")
print(f"Euclidean Distance: {euclidean_distance:.4f}")


# Output
"""
Cosine Similarity: 0.7071
Covariance: 0.1667
Standard Deviation 1: 0.5774
Standard Deviation 2: 0.5774
Correlation Similarity: 0.7500
Euclidean Distance: 1.0000
"""
