import numpy as np

# Compute entropy and information gain for refund
# Higher entropy means lower gain
# Refund Information Gain = 0.5857

# Entropy Cheat
Cheat = -(3/10)*np.log2(3/10) - (7/10)*np.log2(7/10)

# Entropy Refund Yes
RefundYes = -(3/3)*np.log2(4/4) - (0/3)*np.log2(1/4)

# Entropy Refund No
RefundNo = -(4/7)*np.log2(4/7) - (3/7)*np.log2(3/7)

# Compute for Info Gain for Refund
Gain_Refund = Cheat - (7/10)*RefundYes - (3/10)*RefundNo

# Compute entropy and information gain for marital status.
# Marital Information Gain = 0.2813

# Entropy for Cheat Class
Class_Cheat = -(3/10)*np.log2(3/10) - (7/10)*np.log2(7/10)

# Entropy for Single
Single = -(2/4)*np.log2(2/4) - (2/4)*np.log2(2/4)

# Entropy for Married
Married = -(0/4)*np.log2(1/5) - (4/4)*np.log2(5/5)

# Entropy for Divorce
Divorced = -(1/2)*np.log2(1/2) - (1/2)*np.log2(1/2)

# Compute for Info Gain
Gain_Marriage = Class_Cheat - (4/10)*Single - (4/10)*Married - (2/10)*Divorced

# Print the gains
print("Gain_Refund: ", Gain_Refund)
print("Gain_Marriage: ", Gain_Marriage)

# Compare the gains
if Gain_Refund > Gain_Marriage:
    print("Refund should be chosen as an attribute to split the root node of a decision tree")
else:
    print("Marital status should be chosen as an attribute to split the root node of a decision tree")


# Output
# Gain_Refund:   0.5857224584204173
# Gain_Marriage: 0.28129089923069267
# Refund should be chosen as an attribute to split the root node of a decision tree
