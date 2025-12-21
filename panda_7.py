import pandas as pd
import numpy as np

# Generujemy przykładowy zbiór danych z 100 wierszami
np.random.seed(42)
data = {
    "Name": np.random.choice(["Anna", "Bartosz", "Cezary", "Dorota"], 100),
    "Age": np.random.randint(20, 60, 100),
    "Salary": np.random.randint(3000, 12000, 100),
    "City": np.random.choice(["Warszawa", "Kraków", "Gdańsk"], 100)
}
df = pd.DataFrame(data)
print(df)

df.loc[df.sample(frac=(0.05)).index, 'Age']= np.nan
print(df)
df.drop_duplicates()
print ('without duplicates')
print(df)
df['Age'] = df['Age'].fillna(df['Age']).mean()
print(df)
df['Salary'] = (df['Salary']- df['Salary'].min()) /(df['Salary'].max()-df['Salary'].min())
city_salary_mean = df.groupby('City')['Salary'].mean()
print(f"city salary mean\n{city_salary_mean}")