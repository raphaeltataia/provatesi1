import requests
from bs4 import BeautifulSoup
from sklearn.naive_bayes import MultinomialNB
import pandas
pandas.set_option('display.expand_frame_repr', False)

df = pandas.read_csv('train.csv')
first_three = df.tail(3)

#2a.
survived = df[df['Survived'].isin(['1'])]

#2b.
passangers = len(df['Survived'])

#2c.
percentage = (100 * len(survived))/ passangers

classes = df['Pclass']

class_1 = len(df[(df['Pclass'] == 1) & (df['Sex'] == 'female')])
class_2 = len(df[(df['Pclass'] == 2) & (df['Sex'] == 'female')])
class_3 = len(df[(df['Pclass'] == 3) & (df['Sex'] == 'female')])

class_1_survived = len(df[(df['Pclass'] == 1) & (df['Sex'] == 'female') & (df['Survived'] == 1)])
class_2_survived = len(df[(df['Pclass'] == 2) & (df['Sex'] == 'female') & (df['Survived'] == 1)])
class_3_survived = len(df[(df['Pclass'] == 3) & (df['Sex'] == 'female') & (df['Survived'] == 1)])

percentual_mulheres_class_1 = (100 * class_1_survived) / class_1
percentual_mulheres_class_2 = (100 * class_2_survived) / class_2
percentual_mulheres_class_3 = (100 * class_3_survived) / class_3

#2d.
embarcados = df[~df['Embarked'].isin([''])]

#2e.
df['Sex']= df['Sex'].map({'female': 1, 'male': 0})

#2f.
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1


def isalone_value(row):
    if row['FamilySize'] > 1 :
        return 1
    else:
        return 0

df['IsAlone'] = df.apply(isalone_value, axis=1)

#2h.
x = df[['Sex', 'IsAlone', 'Embarked', 'Pclass']].copy()
y = df[['Survived']].copy()

