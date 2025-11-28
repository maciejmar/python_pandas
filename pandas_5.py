import pandas as pd
import matplotlib.pyplot as plt

INPUT_CSV = "wydatki.csv"
OUTPUT_XLSX = "raport_wydatki.xlsx"

def wczytaj_dane(csv_path: str) -> pd.DataFrame:
    """Wczytuje CSV z wydatkami i przygotowuje kolumny."""
    df = pd.read_csv(csv_path, encoding="cp1250")

    # Oczekiwane kolumny: data, kategoria, kwota, metoda_platnosci, sklep
    # Konwersja daty
    df["data"] = pd.to_datetime(df["data"], errors="coerce")

    # Jeśli coś nie dało się zrzutować na datę -> wyrzuć ten wiersz
    df = df.dropna(subset=["data"])

    # Konwersja kwoty na liczbę
    df["kwota"] = pd.to_numeric(df["kwota"], errors="coerce")
    df = df.dropna(subset=["kwota"])

    # Dodajemy kolumnę "miesiac" w formacie RRRR-MM
    df["miesiac"] = df["data"].dt.to_period("M").astype(str)

    return df

def generuj_pivoty(df: pd.DataFrame):
    """Tworzy tabele przestawne (pivoty)."""
    # Pivot 1: suma kwot wg kategorii i miesiąca
    pivot_kat_mies = pd.pivot_table(
        df,
        values="kwota",
        index="kategoria",
        columns="miesiac",
        aggfunc="sum",
        fill_value=0,
    )

    # Pivot 2: suma kwot wg kategorii i metody płatności
    pivot_kat_metoda = pd.pivot_table(
        df,
        values="kwota",
        index="kategoria",
        columns="metoda_platnosci",
        aggfunc="sum",
        fill_value=0,
    )

    return pivot_kat_mies, pivot_kat_metoda

def generuj_podsumowania(df: pd.DataFrame):
    """Tworzy proste podsumowania: suma wg kategorii i wg miesięcy."""
    suma_kategorie = (
        df.groupby("kategoria", as_index=False)["kwota"].sum()
        .rename(columns={"kwota": "suma_kwota"})
    )

    suma_miesiace = (
        df.groupby("miesiac", as_index=False)["kwota"].sum()
        .rename(columns={"kwota": "suma_kwota"})
        .sort_values("miesiac")
    )

    return suma_kategorie, suma_miesiace

def rysuj_wykresy(suma_kategorie: pd.DataFrame,
                  suma_miesiace: pd.DataFrame):
    """Tworzy wykresy i zapisuje je do PNG w bieżącym katalogu."""
    # Wykres 1: słupki wg kategorii
    plt.figure()
    plt.bar(suma_kategorie["kategoria"], suma_kategorie["suma_kwota"])
    plt.title("Suma wydatków wg kategorii")
    plt.xlabel("Kategoria")
    plt.ylabel("Kwota [zł]")
    plt.tight_layout()
    plt.savefig("wykres_kategorie.png")
    plt.close()

    # Wykres 2: linia wg miesiąca
    plt.figure()
    plt.plot(suma_miesiace["miesiac"], suma_miesiace["suma_kwota"], marker="o")
    plt.title("Suma wydatków wg miesiąca")
    plt.xlabel("Miesiąc")
    plt.ylabel("Kwota [zł]")
    plt.tight_layout()
    plt.savefig("wykres_miesiace.png")
    plt.close()

def zapisz_do_excela(df: pd.DataFrame,
                     pivot_kat_mies: pd.DataFrame,
                     pivot_kat_metoda: pd.DataFrame,
                     suma_kategorie: pd.DataFrame,
                     suma_miesiace: pd.DataFrame,
                     xlsx_path: str):
    """Zapisuje dane i podsumowania do jednego pliku Excel."""
    with pd.ExcelWriter(xlsx_path, engine="openpyxl") as writer:
        # Surowe dane
        df.to_excel(writer, sheet_name="Dane", index=False)

        # Pivoty
        pivot_kat_mies.to_excel(writer, sheet_name="Pivot_kat_mies")
        pivot_kat_metoda.to_excel(writer, sheet_name="Pivot_kat_metoda")

        # Podsumowania
        suma_kategorie.to_excel(writer, sheet_name="Suma_kategorie", index=False)
        suma_miesiace.to_excel(writer, sheet_name="Suma_miesiace", index=False)

def main():
    print("Wczytywanie danych z CSV...")
    df = wczytaj_dane(INPUT_CSV)

    print("Generowanie pivotów...")
    pivot_kat_mies, pivot_kat_metoda = generuj_pivoty(df)

    print("Generowanie podsumowań...")
    suma_kategorie, suma_miesiace = generuj_podsumowania(df)

    print("Rysowanie wykresów...")
    rysuj_wykresy(suma_kategorie, suma_miesiace)

    print(f"Zapisywanie wszystkiego do pliku {OUTPUT_XLSX}...")
    zapisz_do_excela(
        df,
        pivot_kat_mies,
        pivot_kat_metoda,
        suma_kategorie,
        suma_miesiace,
        OUTPUT_XLSX,
    )

    print("Gotowe! Powinieneś mieć:")
    print(f"- {OUTPUT_XLSX}")
    print("- wykres_kategorie.png")
    print("- wykres_miesiace.png")
    
    
    df["data"] = pd.to_datetime(df["data"], errors="coerce")
    df = df.dropna(subset=["data"])
    df["kwota"] = pd.to_numeric(df["kwota"], errors="coerce")
    df = df.dropna(subset=["kwota"])
    df["miesiac"] = df["data"].dt.to_period("M").astype(str)
    
    def generuj_serie_czasowe(df: pd.DataFrame):
    # upewniamy się, że data jest indeksem
        df_ts = df.set_index("data").sort_index()

        # dzienna suma wydatków
        dziennie = df_ts.resample("D")["kwota"].sum()

        # tygodniowa suma wydatków (np. tydzień kalendarzowy)
        tygodniowo = df_ts.resample("W")["kwota"].sum()

        # miesięczna suma wydatków (pełne miesiące kalendarzowe)
        miesiecznie = df_ts.resample("M")["kwota"].sum()

        return dziennie, tygodniowo, miesiecznie
    print("Generowanie serii czasowych...")
    dziennie, tygodniowo, miesiecznie = generuj_serie_czasowe(df)
    def zapisz_do_excela(
    df: pd.DataFrame,
    pivot_kat_mies: pd.DataFrame,
    pivot_kat_metoda: pd.DataFrame,
    suma_kategorie: pd.DataFrame,
    suma_miesiace: pd.DataFrame,
    dziennie: pd.Series,
    tygodniowo: pd.Series,
    miesiecznie: pd.Series,
    xlsx_path: str,
) -> None:
        with pd.ExcelWriter(xlsx_path, engine="openpyxl") as writer:
                df.to_excel(writer, sheet_name="Dane", index=False)
                pivot_kat_mies.to_excel(writer, sheet_name="Pivot_kat_mies")
                pivot_kat_metoda.to_excel(writer, sheet_name="Pivot_kat_metoda")
                suma_kategorie.to_excel(writer, sheet_name="Suma_kategorie", index=False)
                suma_miesiace.to_excel(writer, sheet_name="Suma_miesiace", index=False)

                # NOWOŚĆ: serie czasowe
                dziennie.to_frame(name="kwota").to_excel(writer, sheet_name="Dziennie")
                tygodniowo.to_frame(name="kwota").to_excel(writer, sheet_name="Tygodniowo")
                miesiecznie.to_frame(name="kwota").to_excel(writer, sheet_name="Miesiecznie")
    def generuj_serie_czasowe(df: pd.DataFrame):
        df_ts = df.set_index("data").sort_index()
        dziennie = df_ts.resample("D")["kwota"].sum()

        tygodniowo = df_ts.resample("W")["kwota"].sum()
        miesiecznie = df_ts.resample("M")["kwota"].sum()

        # 7-dniowa suma krocząca na dziennej serii
        dziennie_7d_suma = dziennie.rolling(window=7).sum()

        # 7-dniowa średnia krocząca
        dziennie_7d_srednia = dziennie.rolling(window=7).mean()

        return dziennie, tygodniowo, miesiecznie, dziennie_7d_suma, dziennie_7d_srednia

if __name__ == "__main__":
    main()

