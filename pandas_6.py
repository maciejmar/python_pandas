import pandas as pd
import matplotlib.pyplot as plt

INPUT_CSV = "wydatki.csv"
OUTPUT_XLSX = "raport_wydatki.xlsx"

def wczytaj_dane(csv_path: str) -> pd.DataFrame:
    """Wczytuje CSV i przygotowuje kolumny."""
    df = pd.read_csv(csv_path, encoding="utf-8", sep=",")
    
    # Konwersja daty i czyszczenie
    df["data"] = pd.to_datetime(df["data"], errors="coerce")
    df = df.dropna(subset=["data"])

    # Konwersja kwoty na liczbę
    df["kwota"] = pd.to_numeric(df["kwota"], errors="coerce")
    df = df.dropna(subset=["kwota"])

    # Dodajemy kolumnę pomocniczą "miesiac"
    df["miesiac"] = df["data"].dt.to_period("M").astype(str)
    return df

def generuj_pivoty(df: pd.DataFrame):
    """Tworzy tabele przestawne."""
    pivot_kat_mies = pd.pivot_table(
        df, values="kwota", index="kategoria", columns="miesiac",
        aggfunc="sum", fill_value=0
    )
    pivot_kat_metoda = pd.pivot_table(
        df, values="kwota", index="kategoria", columns="metoda_platnosci",
        aggfunc="sum", fill_value=0
    )
    return pivot_kat_mies, pivot_kat_metoda

def generuj_podsumowania(df: pd.DataFrame):
    """Proste sumy grupowe."""
    suma_kategorie = df.groupby("kategoria", as_index=False)["kwota"].sum().rename(columns={"kwota": "suma_kwota"})
    suma_miesiace = df.groupby("miesiac", as_index=False)["kwota"].sum().sort_values("miesiac")
    return suma_kategorie, suma_miesiace

def generuj_serie_czasowe(df: pd.DataFrame):
    """Oblicza sumy w czasie i średnie kroczące."""
    df_ts = df.set_index("data").sort_index()
    
    dziennie = df_ts.resample("D")["kwota"].sum()
    tygodniowo = df_ts.resample("W")["kwota"].sum()
    miesiecznie = df_ts.resample("M")["kwota"].sum()

    # Okna kroczące (rolling)
    dziennie_7d_suma = dziennie.rolling(window=7).sum()
    dziennie_7d_srednia = dziennie.rolling(window=7).mean()

    return dziennie, tygodniowo, miesiecznie, dziennie_7d_suma, dziennie_7d_srednia

def rysuj_wykresy(suma_kategorie: pd.DataFrame, suma_miesiace: pd.DataFrame):
    """Generuje wykresy PNG."""
    plt.figure(figsize=(10, 6))
    plt.bar(suma_kategorie["kategoria"], suma_kategorie["kwota"] if "kwota" in suma_kategorie else suma_kategorie["suma_kwota"])
    plt.title("Suma wydatków wg kategorii")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("wykres_kategorie.png")
    plt.close()

def zapisz_do_excela(df, p1, p2, s1, s2, ts_d, ts_w, ts_m, rolls, rollm, path):
    """Zapisuje wszystkie wyniki do jednego pliku Excel."""
    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Dane", index=False)
        p1.to_excel(writer, sheet_name="Pivot_kat_mies")
        p2.to_excel(writer, sheet_name="Pivot_kat_metoda")
        s1.to_excel(writer, sheet_name="Suma_kategorie", index=False)
        s2.to_excel(writer, sheet_name="Suma_miesiace", index=False)
        
        # Serie czasowe
        ts_d.to_frame(name="suma_dzienna").to_excel(writer, sheet_name="Analiza_Czasowa")
        # Dodajemy średnie kroczące do tej samej karty lub osobnej
        analysis = pd.DataFrame({
            "suma_dzienna": ts_d,
            "7d_suma_kroczaca": rolls,
            "7d_srednia_kroczaca": rollm
        })
        analysis.to_excel(writer, sheet_name="Trend_7dni")

def main():
    print("1. Wczytywanie danych...")
    df = wczytaj_dane(INPUT_CSV)

    print("2. Generowanie pivotów i podsumowań...")
    p1, p2 = generuj_pivoty(df)
    s1, s2 = generuj_podsumowania(df)

    print("3. Analiza serii czasowych (Resampling & Rolling)...")
    ts_d, ts_w, ts_m, r_sum, r_mean = generuj_serie_czasowe(df)

    print("4. Rysowanie wykresów...")
    rysuj_wykresy(s1, s2)

    print(f"5. Zapisywanie do {OUTPUT_XLSX}...")
    zapisz_do_excela(df, p1, p2, s1, s2, ts_d, ts_w, ts_m, r_sum, r_mean, OUTPUT_XLSX)
    print("Gotowe!")

if __name__ == "__main__":
    main()