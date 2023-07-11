import numpy as np
import pprint 
pp = pprint.PrettyPrinter(indent=4)

print("-" * 60)
print("Learning Algorithms ID3 & J4.8")
print("-" * 60)
print()

print('Magazine - Watch - Sex - Class')
class1  = ['Yes', 'Yes', 'Female', 'Yes']
class2  = ['Yes', 'Yes', 'Female', 'Yes']
class3  = ['Yes', 'No',  'Male',   'Yes']
class4  = ['Yes', 'No',  'Female', 'Yes']
class5  = ['Yes', 'Yes', 'Male',   'Yes']
class6  = ['Yes', 'No',  'Male',   'Yes']
class7  = ['Yes', 'No',  'Male',   'Yes']
class8  = ['No',  'No',  'Male',   'No']
class9  = ['No',  'No',  'Female', 'No']
class10 = ['No',  'Yes', 'Male',   'No']

matrix = [class1, class2, class3, class4, class5, class6, class7, class8, class9, class10]
pp.pprint(matrix)

# EntropyClass   ClassYes=7/10     ClassNo=3/10
EntropyClass = -0.7 * np.log2(0.7) - 0.3 * np.log2(0.3)

print("-" * 60)
print(f"EntropyClass = {EntropyClass:.4f}")
print()

print('------------ Split using "Magazine" Attribute: -------------')

# Magazine  (MagYes+ClassYes)/TotMagYes  (MagNo+ClassNo)/TotMagYes
Entropy1Mag = -(7/7) * np.log2(7/7) - (0/7) * np.log2(1)

# Magazine  (MagNo+ClassYes)/TotMagNo  (MagNo+ClassNo)/TotMagNo
Entropy2Mag = -(0/3) * np.log2(1) - (3/3) * np.log2(3/3)

# Information Gain              MagYes/TotalMag    MagNo/TotalMag
GainMagazine = EntropyClass  - (7/10)*Entropy1Mag - (3/10)*Entropy2Mag
print(f"GainMagazine = {GainMagazine:.4f}")
print()

print('----------- Split using "Watch" Attribute: -------------------')

# Watch  (WatchYes+ClassYes)/TotWatchYes  (WatchNo+ClassNo)/TotWatchYes
Entropy1Watch  = -(3/4) * np.log2(3/4) -(1/4) * np.log2(1/4)

# Watch  (WatchNo+ClassYes)/TotWatchNo  (WatchNo+ClassNo)/TotWatchNo
Entropy2Watch  = -(4/6) * np.log2(4/6) -(2/6) * np.log2(2/6)

# Information Gain        WatchYes/TotalWatch  WatchNo/TotalWatch
GainWatch = EntropyClass - (4/10)*Entropy1Watch - (6/10)*Entropy2Watch
print(f"GainWatch = {GainWatch:.4f}")
print()

print('----------- Split using "Sex" Attribute: -------------------')

# SexAttr  (SexFem+ClassYes)/TotalFem)  SexFem+ClassNo)/TotalFem)
Entropy1Sex  = -(3/4) * np.log2(3/4) -(1/4) * np.log2(1/4)

# SexAttr  (SexMale+ClassYes)/TotalMale   (SexMale+ClassNo)/TotalMale
Entropy2Sex  = -(4/6) * np.log2(4/6) -(2/6) * np.log2(2/6)

# Information Gain         Female/TotalSex    Male/TotalSex
GainSex = EntropyClass - (4/10)*Entropy1Sex - (6/10)*Entropy2Sex
print(f"GainSex = {GainSex:.4f}")
print()
print('-------- Result of Information Gain Lowest is Greatest -----')
print('The highest information gain is magazine attribute.')
print('Magazine attribute will be use to split for ID3/J4.8 methods.\n')

# Output
"""
------------------------------------------------------------
EntropyClass = 0.8813

------------ Split using "Magazine" Attribute: -------------
GainMagazine = 0.8813

----------- Split using "Watch" Attribute: -------------------
GainWatch = 0.0058

----------- Split using "Sex" Attribute: -------------------
GainSex = 0.0058

-------- Result of Information Gain Lowest is Greatest -----
The highest information gain is magazine attribute.
Magazine attribute will be use to split for ID3/J4.8 methods.
"""
