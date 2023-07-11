print("Naïve Bayes Classifier")


print('Travel   - Age  -  Sex   - Survived')
class01 = ['First',  'Adult',  'Male',    'Yes']
class02 = ['First',  'Adult',  'Male',    'No']
class03 = ['First',  'Adult',  'Female',  'Yes']
class04 = ['Second', 'Adult',  'Female',  'Yes']
class05 = ['Second', 'Adult',  'Male',    'No']
class06 = ['Second', 'Child',  'Female',  'Yes']
class07 = ['Third',  'Child',  'Female',  'Yes']
class08 = ['Third',  'Adult',  'Male',    'No']
class09 = ['First',  'Child',  'Female',  'Yes']

print("-" * 70)
print("Predict whether A child from second class will survive in Titanic")
class10 = ['Second', 'Child',  'Male',    '?']
print("-" * 70)

matrix = [class01, class02, class03, class04, class05, 
          class06, class07, class08, class09, class10]

print('P( Survived=Yes |Class=Second, Age=Child, Sex=Male )\n')
print('  = P(Class=Second | Survived=Yes)  * ')
print('    P(Age=Child    | Survived=Yes)  * ')
print('    P(Sex=Male     | Survived=Yes)  * ')
print('    P(Survived=Yes)               / ')
print('    P(Class=Second, Age=Child, Sex=Male)\n')

Total        = 9
SurviveYes   = 6
SurviveNo    = 3

TravelTypes  = 3  # first, second, third
AgeTypes     = 2  # adult, child
SurviveTypes = 2  # male, female

SecondYes    = 2
SecondNo     = 1

ChildYes     = 3
ChildNo      = 0

MaleYes      = 1
MaleNo       = 3

Survived = ((SecondYes + 1) / (SurviveYes + TravelTypes)) *  \
           ((ChildYes + 1)  / (SurviveYes + AgeTypes)) *     \
           ((MaleYes + 1)   / (SurviveYes + SurviveTypes)) * \
           (SurviveYes / Total)

print(f"Survived     = {Survived:.4f}")

NotSurvived = ((SecondNo + 1) / (SurviveNo + TravelTypes)) *  \
              ((ChildNo + 1)  / (SurviveNo + AgeTypes)) *     \
              ((MaleNo + 1)   / (SurviveNo + SurviveTypes)) * \
              (SurviveNo / Total)

print(f"Not Survived = {NotSurvived:.4f}")

print("-" * 70)
print("Determine Survival Chance")
print("-" * 70)

if Survived > NotSurvived:
   print('Male child from second class survived.\n')
else:
   print('Male child from second class did not survive.\n')


# Output
"""
Naïve Bayes Classifier
Travel   - Age  -  Sex   - Survived
----------------------------------------------------------------------
Predict whether A child from second class will survive in Titanic
----------------------------------------------------------------------
P( Survived=Yes |Class=Second, Age=Child, Sex=Male )

  = P(Class=Second | Survived=Yes)  * 
    P(Age=Child    | Survived=Yes)  * 
    P(Sex=Male     | Survived=Yes)  * 
    P(Survived=Yes)               / 
    P(Class=Second, Age=Child, Sex=Male)

Survived     = 0.0278
Not Survived = 0.0178
----------------------------------------------------------------------
Determine Survival Chance
----------------------------------------------------------------------
Male child from second class survived.
"""
