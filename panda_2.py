import pandas as pd

# 1. Przykładowe dane o wydatkach
dane = {
    "data": [
        "2025-01-02", "2025-01-03", "2025-01-05", "2025-01-08",
        "2025-01-10", "2025-01-15", "2025-01-18", "2025-01-20",
        "2025-02-01", "2025-02-03", "2025-02-07", "2025-02-10",
        "2025-02-14", "2025-02-18", "2025-02-21", "2025-02-25",
        "2025-03-02", "2025-03-05", "2025-03-08", "2025-03-12"
    ],
    "kategoria": [
        "Jedzenie", "Transport", "Rachunki", "Jedzenie",
        "Rozrywka", "Jedzenie", "Inne", "Transport",
        "Jedzenie", "Rachunki", "Jedzenie", "Rozrywka",
        "Transport", "Rachunki", "Inne", "Jedzenie",
        "Rachunki", "Transport", "Rozrywka", "Jedzenie"
    ],
    "kwota": [
        45.30, 6.00, 230.00, 32.50,
        55.00, 24.90, 120.00, 7.20,
        38.40, 210.00, 29.99, 70.00,
        5.60, 190.00, 80.00, 33.33,
        205.00, 4.40, 60.00, 27.50
    ],
    "metoda_platnosci": [
        "Karta", "Gotówka", "Przelew", "Karta",
        "Karta", "Gotówka", "Karta", "Karta",
        "Przelew", "Przelew", "Karta", "Karta",
        "Gotówka", "Przelew", "Karta", "Karta",
        "Przelew", "Gotówka", "Karta", "Karta"
    ],
    "sklep": [
        "Biedronka", "ZTM", "Energia", "Lidl",
        "Kino", "Żabka", "Allegro", "ZTM",
        "Lidl", "Gaz", "Biedronka", "Netflix",
        "ZTM", "Woda", "Media Markt", "Żabka",
        "Energia", "ZTM", "Kino", "Lidl"
    ]
}

df = pd.DataFrame(dane)
df["data"] = pd.to_datetime(df["data"])

# 2. Dodanie kolumny miesiąc (rok-miesiąc)
df["miesiac"] = df["data"].dt.to_period("M").astype(str)

# 3. Pivot table: suma wydatków wg kategorii i miesiąca
pivot = pd.pivot_table(
    df,
    values="kwota",
    index="kategoria",   # wiersze
    columns="miesiac",   # kolumny
    aggfunc="sum",       # suma kwot
    fill_value=0
)

# 4. Zapis do Excela
with pd.ExcelWriter("wydatki_pivot_2.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Dane", index=False)
    pivot.to_excel(writer, sheet_name="Pivot")
