def znajdz_pierwsza_podzielna():
    # Przechodzimy przez liczby od 1 do 100
    for liczba in range(1, 101):
        if liczba % 7 == 0:  # Sprawdzamy, czy liczba jest podzielna przez 7
            print(f"Pierwsza liczba podzielna przez 7 to: {liczba}")
            break  # Zatrzymujemy pętlę po znalezieniu pierwszej liczby podzielnej przez 7

# Uruchamiamy program
znajdz_pierwsza_podzielna()

Pierwsza liczba podzielna przez 7 to: 7
