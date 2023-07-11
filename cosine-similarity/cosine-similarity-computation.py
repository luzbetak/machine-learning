import math

x = [3, 2, 0, 5, 0, 0, 0, 2, 0, 0]
y = [1, 0, 0, 0, 0, 0, 0, 1, 0, 2]

xy = sum(xi * yi for xi, yi in zip(x, y))
x1 = math.sqrt(sum(xi * xi for xi in x))
y1 = math.sqrt(sum(yi * yi for yi in y))

cosine_similarity = xy / (x1 * y1)

result = f"""
xy = {xy}
x1 = {x1:.4f}
y1 = {y1:.4f}
CosineSimilarity = {cosine_similarity:.4f}
"""

print(result)


# Output
"""
xy = 5
x1 = 6.4807
y1 = 2.4495
CosineSimilarity = 0.3150
"""

