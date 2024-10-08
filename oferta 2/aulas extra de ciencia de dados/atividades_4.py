import matplotlib.pyplot as plt
import pandas as pd
from atividades_1 import basePath

gender_dict = {'Male':0,'Female':0}
degree_dict = {'Data Science':0, 'Computer Science':0, 'Information Technology':0, 'Software Engineering':0}

df = pd.read_csv(f'{basePath()}/datasets/MentalHealthSurvey new.csv')
gender = df['gender']

for g in gender:
  match g:
    case 'Female':
      gender_dict['Female'] += 1
    case 'Male':
      gender_dict['Male'] += 1

for d in degree:

plt.subplot(2,3,1)
plt.title('Porcentagem de gênero dos participantes')
plt.pie(gender_dict.values(), labels=gender_dict.keys(), autopct='%.1f%%')

plt.subplot(2,3,2)
plt.title()

plt.show()