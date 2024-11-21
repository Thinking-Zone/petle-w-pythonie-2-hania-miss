import random

def pytaj_o_pogode():
    # Losujemy, czy pada deszcz (True) czy nie (False)
    pada = random.choice([True, False])

    # Pętla, która pyta użytkownika, aż zgadnie poprawnie
    while True:
        # Zapytaj użytkownika o pogodę
        odpowiedz = input("Czy pada deszcz? (tak/nie): ").strip().lower()

        # Sprawdzamy odpowiedź
        if odpowiedz == "tak" and pada:
            print("Brawo! Zgadłeś!")
            break
        elif odpowiedz == "nie" and not pada:
            print("Brawo! Zgadłeś!")
            break
        else:
            print("Nie zgadłeś, spróbuj jeszcze raz.")

# Uruchamiamy program
pytaj_o_pogode()
