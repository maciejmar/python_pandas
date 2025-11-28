import pandas as pd

df = pd.DataFrame({
    "imie": ["Ala", "Ola", "Jan", "Piotr"],
    "wiek": [20, None, 21, None],
    "miasto": ["Warszawa", "Kraków", None, "Gdańsk"]
})
print(df)
df.isna()          # True/False dla każdej komórki
print(f"braki \n {df.isna().sum()}") 