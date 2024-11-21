def sumuj_parzyste():
    suma = 0  # Inicjalizujemy zmienną do sumowania

    # Przechodzimy przez liczby od 1 do 200
    for liczba in range(1, 201):
        if liczba % 2 == 0:  # Sprawdzamy, czy liczba jest parzysta
            suma += liczba  # Dodajemy liczbę do sumy

    print(f"Suma liczb parzystych w zakresie od 1 do 200 wynosi: {suma}")

# Uruchamiamy program
sumuj_parzyste()
