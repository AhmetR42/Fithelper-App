def vraag_tekst(vraag):
    while True:
        antwoord = input(vraag).strip()

        if antwoord:
            return antwoord

        print("Dit veld mag niet leeg zijn. Probeer opnieuw.")


def vraag_getal(vraag, minimum, maximum):
    while True:
        try:
            waarde = float(input(vraag))

            if minimum <= waarde <= maximum:
                return waarde

            print(f"Voer een getal in tussen {minimum} en {maximum}.")

        except ValueError:
            print("Ongeldige invoer. Voer een geldig getal in.")