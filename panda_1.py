import pandas as pd
import numpy as np

s = pd.Series([10, 20, 30, 40], name="punkty")
print(s)

dane = {
    "imie": ["Ala", "Ola", "Jan"],
    "wiek": [25, 30, 22],
    "miasto": ["Warszawa", "Kraków", "Gdańsk"]
}

df = pd.DataFrame(dane)
print(df)


df = pd.read_csv("studenci.csv")
print(df.head())
print(df.info())
df = pd.read_excel("studenci.xlsx", sheet_name="Arkusz1")
print(df)

df = pd.DataFrame({
    "imie": ["Ala", "Ola", "Jan", "Piotr", "Ala", "Ron", "Jan"],
    "wiek": [20, 22, 21, 23, 19, 30, 63],
    "kierunek": ["Informatyka", "Matematyka", "Informatyka", "Fizyka", "Informatyka", "Matematyka", "Matematyka"],
    "ocena": [4.5, 5.0, 3.5, 4.0, 4.0, 6.0, 6.0]
})

df1 = df.sort_values("wiek", ascending=False)
print(f"sorted:\n {df1}")

df_sorted = df.sort_index()
print(f"sorted: {df_sorted}")

df = df.sort_values(["kierunek", "ocena"], ascending=[True, False])
print(f"sorted by two columns\n {df}")

df = df.sort_values(["imie","ocena","kierunek"], ascending = [True, True, True])
print(f"sorted by three columns\n {df}")

df_filtred = df[df["ocena"] == 4.0]
print(f"filtered by 4.0 is\n {df_filtred}")

df_filtered = df[df["ocena"].between(3,4)]
print(f" filtered by ocena\n  {df_filtered}")

df["wiek_za_rok"] = df["wiek"] + 1
print(f"wiek za rok \n {df}")

df["ocena procentowa"] = ((df["ocena"]-2)/(6-2))*100
print(f"ocena proc. dodana \n {df}")

podsumowanie = df.groupby("kierunek").agg(
    liczba_studentow=("imie", "count"),
    srednia_ocena=("ocena", "mean"),
    max_ocena=("ocena", "max")
)
print(podsumowanie)

'''kolumna warunkowa z uzyciem numpy'''
print("tu dodanie kolumny")
df["czy zaliczyl"] = np.where(df["ocena"]>=5,"zaliczone","niezaliczone")
print(df)

'''mapowanie - zmiana nazw kolumn'''
mapa = {
    "Informatyka":"informatyka",
    "Matematyka":"matematyka",
    "Fizyka": "fizyka"
}
df["kierunek"] = df["kierunek"].map(mapa)
print(f"po zmapowaniu \n {df}")

df_gr=df.groupby("kierunek")["ocena"].mean()
print(f"średnia ocen dla kierunku {df_gr}")

srednie_oceny = df.groupby("kierunek")["ocena"].mean().reset_index()
print(f"średnie oceny\n {srednie_oceny}")

df_2 = df.groupby("kierunek").agg({
    "imie": "count",   # ile osób
    "wiek": "mean"     # średni wiek
})
print(f"agregacja \n {df_2}")


dframe = pd.DataFrame({'Name': ['Alice', 'Bob', 'Aritra'],
                   'Age': [25, 30, 35],
                   'Location': ['Seattle', 'New York', 'Kona']},
                  index=([0,1,2]))

podsumowanie = df.groupby("kierunek").agg(
    liczba_studentow=("imie", "count"),
    srednia_ocena=("ocena", "mean"),
    max_ocena=("ocena", "max")
)

print(f"podsumowanie\n {podsumowanie}")