import pandas as pd
import numpy as np


df2 = pd.DataFrame({
    "imie": ["Ala", "Ola", "Ala", "Jan", "Ala"],
    "kierunek": ["INF", "MAT", "INF", "FIZ", "INF"],
    "ocena": [4.5, 5.0, 4.5, 3.0, 4.5]
})
print(df2)


df = pd.DataFrame({
    "imie": ["Ala", "Ola", "Jan", "Piotr", "Ewa"],
    "wiek": [19, 22, 35, 41, 28]
})
print(df2)

bins = [0, 25, 40, 120]  # granice przedziałów
labels = ["mlody", "sredni", "starszy"]

df["wiek_kategoria"] = pd.cut(df["wiek"], bins=bins, labels=labels, right=False)
print(df)
print(df["wiek_kategoria"].value_counts())

studenci = pd.DataFrame({
    "id_studenta": [1, 2, 3],
    "imie": ["Ala", "Ola", "Jan"]
})

oceny = pd.DataFrame({
    "id_studenta": [1, 1, 2, 3],
    "przedmiot": ["Matematyka", "Fizyka", "Fizyka", "Informatyka"],
    "ocena": [5.0, 4.0, 3.5, 5.0]
})

df_polaczone = pd.merge(
    studenci,
    oceny,
    on="id_studenta",   # klucz łączenia
    how="inner"         # typ JOIN
)

print(df_polaczone)

df_left = pd.merge(studenci, oceny, on="id_studenta", how="left")
print(f"joined left \n {df_left}")

import pandas as pd

df = pd.DataFrame({
    "imie": ["Ala", "Ola", "Jan", "Piotr", "Ewa"],
    "wiek": [20, 22, 21, 23, 19],
    "kierunek": ["INF", "MAT", "INF", "FIZ", "INF"],
    "ocena": [4.5, 5.0, 3.5, 4.0, 2.0]
})

df.to_csv("studenci_3.csv", index=False)


df = pd.DataFrame({
    "imie": ["Ala", "Ola", "Jan", "Piotr", "Ewa"],
    "wiek": [20, 22, 21, 23, 19],
    "kierunek": ["INF", "MAT", "INF", "FIZ", "INF"],
    "ocena": [4.5, 5.0, 3.5, 4.0, 2.0]
})

df.to_csv("studenci_4.csv", index=False)
df[df["ocena"] >= 4].to_csv("studenci_dobrzy.csv", index=False)

def opis_oceny(x):
    if x >= 4.5:
        return "super"
    elif x >= 3.0:
        return "ok"
    else:
        return "slabo"

df["opis_oceny"] = df["ocena"].apply(opis_oceny)
print(df)

df["opis_oceny"] = df["ocena"].apply(
    lambda x: "super" if x >= 4.5 else ("ok" if x >= 3.0 else "slabo")
)

def opisz_wiersz(r):
    return f"{r['imie']} ({r['kierunek']}), wiek {r['wiek']}, ocena {r['ocena']}"

df["opis"] = df.apply(opisz_wiersz, axis=1)
print(df[["opis"]])
df_inf_mat = df.query('kierunek in ["INF", "MAT"]')

# ocena między 3 a 5
df_3_5 = df.query('ocena >= 3 and ocena <= 5')

# młodzi (wiek < 21)
df_mlodzi = df.query('wiek < 21')
print (df)

df = pd.DataFrame({
    "data": [
        "2025-01-02", "2025-01-03", "2025-01-05"
    ],
    "kategoria": [
        "Jedzenie", "Transport", "Rachunki"
    ],
    "kwota": [
        45.30, 6.00, 230.00
    ]
})

df["data"] = pd.to_datetime(df["data"])
print(df)

df["data"] = pd.to_datetime(df["data"])
df["miesiac"] = df["data"].dt.to_period("M").astype(str)