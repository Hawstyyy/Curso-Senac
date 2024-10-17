import matplotlib.pyplot as plt
import pandas as pd
from atividades_1 import basePath

gender_dict = {'Male':0,'Female':0}
degree_dict = {'Data Science':0, 'Computer Science':0, 'Information Technology':0, 'Software Engineering':0}
year_dict = {'1st year':0, '3rd year':0, '2nd year':0, '4th year':0}
depression_dict = {'Over 3':0, 'Under 3':0}
anxiety_dict = {'Over 3':0, 'Under 3':0}

df = pd.read_csv(f'{basePath()}/datasets/MentalHealthSurvey new.csv')

gender = df['gender']
degree = df['degree_major']
year = df['academic_year']
depression = df['depression']
anxiety = df['anxiety']

for g in gender:
  match g:
    case 'Female':
      gender_dict['Female'] += 1
    case 'Male':
      gender_dict['Male'] += 1

for d in degree:
  match d:
    case 'Data Science':
      degree_dict['Data Science'] += 1
    case 'Computer Science':
      degree_dict['Computer Science'] += 1
    case 'Information Technology':
      degree_dict['Information Technology'] += 1
    case 'Software Engineering':
      degree_dict['Software Engineering'] += 1

for y in year:
  match y:
    case '1st year':
      year_dict['1st year'] += 1
    case '2nd year':
      year_dict['2nd year'] += 1
    case '3rd year':
      year_dict['3rd year'] += 1
    case '4th year':
      year_dict['4th year'] += 1

for dp in depression:
  if dp > 3:
    depression_dict['Over 3'] += 1
  else:
    depression_dict['Under 3'] += 1

for a in anxiety:
  if a > 3:
    anxiety_dict['Over 3'] += 1
  else:
    anxiety_dict['Under 3'] += 1

plt.subplot(2,3,1)
plt.title('Porcentagem de gênero dos participantes')
plt.pie(gender_dict.values(), labels=gender_dict.keys(), autopct='%.1f%%')

plt.subplot(2,3,2)
plt.title('Cursos mais presentes nas pesquisas')
plt.pie(degree_dict.values(), labels=degree_dict.keys(), autopct='%.1f%%')

plt.subplot(2,3,3)
plt.title('Ano da faculdade')
plt.pie(year_dict.values(), labels=year_dict.keys(), autopct='%.1f%%')

plt.subplot(2,3,4)
plt.title('Sentimento de depressão')
plt.pie(depression_dict.values(), labels=depression_dict.keys(), autopct='%.1f%%')

plt.subplot(2,3,5)
plt.title('Sentimento de ansiedade')
plt.pie(anxiety_dict.values(), labels=anxiety_dict.keys(), autopct='%.1f%%')

plt.show()