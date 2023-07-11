import pandas as pd
import numpy as np
import pprint 
pp = pprint.PrettyPrinter(indent=4)


def entropy(target_col):
    elements,counts = np.unique(target_col,return_counts = True)
    entropy = np.sum([(-counts[i]/np.sum(counts))*np.log2(counts[i]/np.sum(counts)) for i in range(len(elements))])
    return entropy

def InfoGain(data,split_attribute_name,target_name="class"):
    total_entropy = entropy(data[target_name])
    vals,counts= np.unique(data[split_attribute_name],return_counts=True)
    Weighted_Entropy = np.sum([(counts[i]/np.sum(counts))*entropy(data.where(data[split_attribute_name]==vals[i]).dropna()[target_name]) for i in range(len(vals))])
    Information_Gain = total_entropy - Weighted_Entropy
    return Information_Gain

def ID3(data,originaldata,features,target_attribute_name="class",parent_node_class = None):
    if len(np.unique(data[target_attribute_name])) <= 1:
        return np.unique(data[target_attribute_name])[0]
    elif len(data)==0:
        return np.unique(originaldata[target_attribute_name])[np.argmax(np.unique(originaldata[target_attribute_name],return_counts=True)[1])]
    elif len(features) ==0:
        return parent_node_class
    else:
        parent_node_class = np.unique(data[target_attribute_name])[np.argmax(np.unique(data[target_attribute_name],return_counts=True)[1])]
        item_values = [InfoGain(data,feature,target_attribute_name) for feature in features]
        best_feature_index = np.argmax(item_values)
        best_feature = features[best_feature_index]
        tree = {best_feature:{}}
        features = [i for i in features if i != best_feature]
        for value in np.unique(data[best_feature]):
            value = value
            sub_data = data.where(data[best_feature] == value).dropna()
            subtree = ID3(sub_data,originaldata,features,target_attribute_name,parent_node_class)
            tree[best_feature][value] = subtree
        return(tree)


# Define the dataset
"""
     Outlook Temperature Humidity     Wind PlayTennis
0      Sunny         Hot     High     Weak         No
1      Sunny         Hot     High   Strong         No
2   Overcast         Hot     High     Weak        Yes
3       Rain        Mild     High     Weak        Yes
4       Rain        Cool   Normal     Weak        Yes
5       Rain        Cool   Normal   Strong         No
6   Overcast        Cool   Normal   Strong        Yes
7      Sunny        Mild     High     Weak         No
8      Sunny        Cool   Normal     Weak        Yes
9       Rain        Mild   Normal     Weak        Yes
10     Sunny        Mild   Normal   Strong        Yes
11  Overcast        Mild     High   Strong        Yes
12  Overcast         Hot   Normal     Weak        Yes
13      Rain        Mild     High   Strong         No
"""

data = {
'Outlook':     ['Sunny', 'Sunny',  'Overcast', 'Rain', 'Rain',   'Rain',   'Overcast', 'Sunny', 'Sunny',  'Rain',   'Sunny',  'Overcast', 'Overcast', 'Rain'],
'Temperature': ['Hot',   'Hot',    'Hot',      'Mild', 'Cool',   'Cool',   'Cool',     'Mild',  'Cool',   'Mild',   'Mild',   'Mild',     'Hot',      'Mild'],
'Humidity':    ['High',  'High',   'High',     'High', 'Normal', 'Normal', 'Normal',   'High',  'Normal', 'Normal', 'Normal', 'High',     'Normal',   'High'],
'Wind':        ['Weak',  'Strong', 'Weak',     'Weak', 'Weak',   'Strong', 'Strong',   'Weak',  'Weak',   'Weak',   'Strong', 'Strong',   'Weak',     'Strong'],
'PlayTennis':  ['No',    'No',     'Yes',      'Yes',  'Yes',    'No',     'Yes',      'No',    'Yes',    'Yes',    'Yes',    'Yes',      'Yes',      'No']
}

df = pd.DataFrame(data)

# define target and feature columns
target = 'PlayTennis'
features = df.columns[df.columns != target].tolist()

# apply ID3
tree = ID3(df, df, features, target)
pp.pprint(tree)

#----------------------------------------------------------------------------------------#
# Output
"""
{   'Outlook': {   'Overcast': 'Yes',
                   'Rain'    : {'Wind'    : {'Strong': 'No', 'Weak'  : 'Yes'}},
                   'Sunny'   : {'Humidity': {'High'  : 'No', 'Normal': 'Yes'}}
               }
}

This output can be read as:

If the outlook is overcast, then play tennis.
If the outlook is rainy and the wind is strong, then do not play tennis.
If the outlook is rainy and the wind is weak, then play tennis.
If the outlook is sunny and the humidity is high, then do not play tennis.
If the outlook is sunny and the humidity is normal, then play tennis.
"""



