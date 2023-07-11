Learning Algorithms ID3 & J4.8
==============================

The ID3 algorithm doesn't handle numerical data or missing values, and it doesn't do any pruning. The J48, which is the Weka implementation of the C4.5 algorithm, does handle these aspects, but it's significantly more complex.

---

## ID3 (Iterative Dichotomiser 3)

ID3, which stands for Iterative Dichotomiser 3, is a decision tree algorithm used for machine learning and natural language processing. It was developed by Ross Quinlan, a researcher in the field of machine learning.

The ID3 algorithm builds a decision tree by employing a top-down, greedy search through the given sets to test each attribute at every tree node. In order to choose an attribute to test at each node, ID3 uses the concept of entropy and information gain.

### Entropy

Entropy is a measure of the impurity in the input set. In the context of machine learning, it is used to quantify the randomness or disorder within a set of class values.

### Information Gain

Information gain is the decrease in entropy. ID3 uses information gain to decide which attribute goes into a decision node. The attribute with the highest information gain will be split first.

After splitting an attribute, the algorithm continues the process with the subsets of the original set. It continues to do this recursively until it reaches a point where all data is classified (i.e., the data in the subset all have the same value for the target attribute), or there are no more attributes to be split.

The ID3 algorithm is simple and effective, but it also has some limitations. For example, it doesn't handle numeric attributes and missing values well, and it may overfit the training data. Later algorithms, like C4.5 (also developed by Ross Quinlan), are extensions of ID3 that address some of these limitations.

---

## J4.8

J4.8 is an extension of the J48 algorithm, which is itself a Java-based implementation of the C4.5 algorithm in the WEKA machine learning library. The C4.5 algorithm is an extension of the ID3 algorithm, both developed by Ross Quinlan.

C4.5 introduced a number of improvements over ID3. Some of the most significant changes include:

1. **Handling both continuous and discrete attributes**: While ID3 can only handle categorical attributes, C4.5 can handle both categorical and continuous attributes.

2. **Use of a different metric, Gain Ratio, to choose attributes**: ID3 uses information gain, which is biased towards attributes with many outcomes. C4.5 corrects this bias by normalizing information gain using a "split information" value, which leads to the gain ratio criterion.

3. **Handling training data with missing attribute values**: C4.5 goes beyond ID3 by providing a robust method for handling missing attribute values.

4. **Pruning of decision trees after creation**: C4.5 prunes the decision tree using a method called error-based pruning, which helps to avoid overfitting the training data.

The J48/J4.8 algorithm is simply the implementation of the C4.5 algorithm in Java as part of the WEKA data mining software. The number '48' or '4.8' is just a version number and does not indicate a fundamental change to the algorithm itself.

Ross Quinlan has also developed an algorithm called C5.0, which is an improved and proprietary version of C4.5. C5.0 offers additional improvements such as speed, memory usage, and more options for winnowing down decision trees.




