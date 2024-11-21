def pytaj_o_pogode():
    # Licznik odpowiedzi "nie"
    liczba_nie = 0

    # Pętla, która pyta użytkownika, aż odpowie "tak"
    while True:
        odpowiedz = input("Czy pada deszcz? (tak/nie/nie wiem): ").strip().lower()

        if odpowiedz == "tak":
            print(f"Koniec programu. Liczba odpowiedzi 'nie': {liczba_nie}")
            break
        elif odpowiedz == "nie":
            liczba_nie += 1
        elif odpowiedz == "nie wiem":
            print("To wyjdź na zewnątrz i się dowiedz.")
        else:
            print("Nie rozumiem odpowiedzi. Proszę wpisz 'tak', 'nie' lub 'nie wiem'.")

# Uruchamiamy program
pytaj_o_pogode()
