'''Simple operations on data with pandas and dataframe'''
import pandas as pd

# Przykładowe dane z brakami i duplikatami
data = {
    "Name": ["Anna", "Bartosz", "Cezary", "Anna"],
    "Age": [25, None, 30, 25],
    "City": ["Warszawa", "Kraków", "Gdańsk", "Warszawa"]
}

# Tworzymy DataFrame
df = pd.DataFrame(data)
print(df)
# Usuwamy duplikaty
df = df.drop_duplicates()
print (df)
# Usuwamy wiersze z brakującymi danymi (można też wypełnić je np. średnią)
df = df.dropna()

# Wyświetlamy wyczyszczone dane
print(df)
