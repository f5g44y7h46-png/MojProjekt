import json
import os

PLIK = "zadania.json"


# =========================
# ZAPIS I ODCZYT ZADAŃ
# =========================

def wczytaj_zadania():
    if os.path.exists(PLIK):
        try:
            with open(PLIK, "r", encoding="utf-8") as plik:
                return json.load(plik)
        except (json.JSONDecodeError, OSError):
            return []
    return []


def zapisz_zadania():
    with open(PLIK, "w", encoding="utf-8") as plik:
        json.dump(zadania, plik, ensure_ascii=False, indent=2)


zadania = wczytaj_zadania()


# =========================
# KALKULATOR
# =========================

def kalkulator():
    print("\n=== KALKULATOR ===")

    try:
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
    except ValueError:
        print("Błąd: wpisz liczby.")
        return

    print("\n1 - Dodawanie")
    print("2 - Odejmowanie")
    print("3 - Mnożenie")
    print("4 - Dzielenie")
    print("5 - Potęgowanie")

    wybor = input("Wybierz działanie: ")

    if wybor == "1":
        print("Wynik:", a + b)

    elif wybor == "2":
        print("Wynik:", a - b)

    elif wybor == "3":
        print("Wynik:", a * b)

    elif wybor == "4":
        if b == 0:
            print("Nie można dzielić przez zero.")
        else:
            print("Wynik:", a / b)

    elif wybor == "5":
        print("Wynik:", a ** b)

    else:
        print("Nieprawidłowa opcja.")


# =========================
# POKAŻ ZADANIA
# =========================

def pokaz_zadania():
    print("\n=== TWOJE ZADANIA ===")

    if not zadania:
        print("Brak zadań.")
        return

    for i, zadanie in enumerate(zadania, start=1):
        status = "✓" if zadanie["wykonane"] else " "
        print(f"{i}. [{status}] {zadanie['tekst']}")


# =========================
# DODAJ ZADANIE
# =========================

def dodaj_zadanie():
    tekst = input("Wpisz zadanie: ").strip()

    if tekst == "":
        print("Zadanie nie może być puste.")
        return

    zadania.append({
        "tekst": tekst,
        "wykonane": False
    })

    zapisz_zadania()
    print("Zadanie dodane!")


# =========================
# OZNACZ JAKO WYKONANE
# =========================

def oznacz_wykonane():
    pokaz_zadania()

    if not zadania:
        return

    try:
        numer = int(input("Które zadanie oznaczyć jako wykonane? "))
    except ValueError:
        print("Nieprawidłowy numer.")
        return

    if 1 <= numer <= len(zadania):
        zadania[numer - 1]["wykonane"] = True
        zapisz_zadania()
        print("Zadanie oznaczone jako wykonane!")
    else:
        print("Nieprawidłowy numer.")


# =========================
# EDYTUJ ZADANIE
# =========================

def edytuj_zadanie():
    pokaz_zadania()

    if not zadania:
        return

    try:
        numer = int(input("Które zadanie edytować? "))
    except ValueError:
        print("Nieprawidłowy numer.")
        return

    if 1 <= numer <= len(zadania):
        nowe = input("Wpisz nową treść zadania: ").strip()

        if nowe == "":
            print("Treść zadania nie może być pusta.")
            return

        zadania[numer - 1]["tekst"] = nowe
        zapisz_zadania()
        print("Zadanie zmienione!")
    else:
        print("Nieprawidłowy numer.")


# =========================
# USUŃ ZADANIE
# =========================

def usun_zadanie():
    pokaz_zadania()

    if not zadania:
        return

    try:
        numer = int(input("Które zadanie usunąć? "))
    except ValueError:
        print("Nieprawidłowy numer.")
        return

    if 1 <= numer <= len(zadania):
        usuniete = zadania.pop(numer - 1)
        zapisz_zadania()
        print("Usunięto:", usuniete["tekst"])
    else:
        print("Nieprawidłowy numer.")


# =========================
# USUŃ WSZYSTKIE
# =========================

def usun_wszystkie():
    if not zadania:
        print("Lista zadań jest już pusta.")
        return

    potwierdzenie = input(
        "Czy na pewno usunąć wszystkie zadania? (tak/nie): "
    ).strip().lower()

    if potwierdzenie == "tak":
        zadania.clear()
        zapisz_zadania()
        print("Wszystkie zadania zostały usunięte!")
    else:
        print("Anulowano.")


# =========================
# WYSZUKIWANIE
# =========================

def wyszukaj_zadanie():
    fraza = input("Czego szukasz? ").strip().lower()

    if not fraza:
        print("Wpisz tekst do wyszukania.")
        return

    znalezione = False

    print("\n=== WYNIKI WYSZUKIWANIA ===")

    for i, zadanie in enumerate(zadania, start=1):
        if fraza in zadanie["tekst"].lower():
            status = "✓" if zadanie["wykonane"] else " "
            print(f"{i}. [{status}] {zadanie['tekst']}")
            znalezione = True

    if not znalezione:
        print("Nie znaleziono zadania.")


# =========================
# LISTA ZADAŃ
# =========================

def lista_zadan():
    while True:
        print("\n=== LISTA ZADAŃ ===")
        print("1 - Dodaj zadanie")
        print("2 - Pokaż zadania")
        print("3 - Oznacz jako wykonane")
        print("4 - Edytuj zadanie")
        print("5 - Usuń zadanie")
        print("6 - Usuń wszystkie zadania")
        print("7 - Wyszukaj zadanie")
        print("8 - Powrót")

        wybor = input("Wybierz: ")

        if wybor == "1":
            dodaj_zadanie()

        elif wybor == "2":
            pokaz_zadania()

        elif wybor == "3":
            oznacz_wykonane()

        elif wybor == "4":
            edytuj_zadanie()

        elif wybor == "5":
            usun_zadanie()

        elif wybor == "6":
            usun_wszystkie()

        elif wybor == "7":
            wyszukaj_zadanie()

        elif wybor == "8":
            break

        else:
            print("Nieprawidłowa opcja.")


# =========================
# INFORMACJA
# =========================

def informacja():
    print("\n=== INFORMACJA ===")
    print("To jest moja aplikacja napisana w Pythonie.")
    print("Aplikacja zawiera:")
    print("- kalkulator")
    print("- listę zadań")
    print("- zapisywanie zadań do pliku")
    print("- wyszukiwanie")
    print("- edycję")
    print("- oznaczanie zadań jako wykonane")


# =========================
# GŁÓWNE MENU
# =========================

def main():
    while True:
        print("\n=== MOJA APLIKACJA ===")
        print("1 - Kalkulator")
        print("2 - Lista zadań")
        print("3 - Informacja")
        print("4 - Wyjście")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            kalkulator()

        elif wybor == "2":
            lista_zadan()

        elif wybor == "3":
            informacja()

        elif wybor == "4":
            print("Do zobaczenia!")
            break

        else:
            print("Nieprawidłowa opcja.")


# =========================
# START PROGRAMU
# =========================

if __name__ == "__main__":
    main()