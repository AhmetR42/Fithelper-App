import json
import os
from datetime import date


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


def bereken_bmi(gewicht, lengte_cm):
    lengte_meter = lengte_cm / 100
    return gewicht / (lengte_meter ** 2)


def geef_bmi_advies(bmi):
    if bmi < 18.5:
        return (
            "Je hebt ondergewicht. Het is belangrijk om een gezond gewicht te bereiken. "
            "Overweeg om meer voedzame maaltijden te eten en regelmatig te bewegen."
        )
    elif bmi < 25:
        return (
            "Je hebt een gezond gewicht. Blijf zo doorgaan met een gebalanceerd dieet "
            "en regelmatige lichaamsbeweging!"
        )
    elif bmi < 30:
        return (
            "Je hebt overgewicht. Overweeg om meer te bewegen en gezondere voedingskeuzes "
            "te maken."
        )
    else:
        return (
            "Je hebt obesitas. Overweeg om een professional te raadplegen voor advies "
            "over voeding en lichaamsbeweging."
        )


def geef_leefstijl_advies(keuze):
    keuze = keuze.lower().strip()

    if keuze == "voeding":
        return (
            "Voor voeding is het belangrijk om een gebalanceerd dieet te volgen met "
            "groenten, fruit, volkoren producten en voldoende eiwitten."
        )
    elif keuze == "beweging":
        return (
            "Voor beweging is het aan te raden om regelmatig actief te zijn. Denk aan "
            "wandelen, fietsen, krachttraining of een sport die je leuk vindt."
        )
    elif keuze == "beide":
        return (
            "Voor een gezonde levensstijl is het belangrijk om zowel op voeding als "
            "beweging te letten. Combineer gezond eten met regelmatige training."
        )
    else:
        return "Ongeldige keuze. Kies 'voeding', 'beweging' of 'beide'."


def maak_profiel():
    print("\n--- Profiel aanmaken ---")

    naam = vraag_tekst("Wat is je naam? ")

    print(
        f"\nHallo {naam}! Welkom bij de FitHelper app. "
        "Beantwoord de komende vragen om jouw startprofiel te maken.\n"
    )

    leeftijd = int(vraag_getal("Wat is je leeftijd? ", 10, 100))
    gewicht = vraag_getal("Wat is je gewicht in kg? ", 30, 250)
    lengte = vraag_getal("Wat is je lengte in cm? ", 100, 250)

    bmi = bereken_bmi(gewicht, lengte)

    print(f"\nJe BMI is: {bmi:.2f}")
    print(geef_bmi_advies(bmi))

    advies_keuze = input("\nWil je advies over voeding, beweging of beide? ").lower()
    leefstijl_advies = geef_leefstijl_advies(advies_keuze)

    print(leefstijl_advies)

    profiel = {
        "naam": naam,
        "leeftijd": leeftijd,
        "gewicht": gewicht,
        "lengte": lengte,
        "bmi": round(bmi, 2),
        "advies_keuze": advies_keuze,
        "leefstijl_advies": leefstijl_advies
    }

    return profiel


def sla_profiel_op(profiel):
    os.makedirs("data", exist_ok=True)

    with open("data/user.json", "w", encoding="utf-8") as bestand:
        json.dump(profiel, bestand, indent=4, ensure_ascii=False)

    print("\nProfiel is succesvol opgeslagen in data/user.json.")


def bereken_volume(sets, reps, gewicht):
    return sets * reps * gewicht


def maak_workout():
    print("\n--- Workout toevoegen ---")

    oefening = vraag_tekst("Welke oefening heb je gedaan? ")
    sets = int(vraag_getal("Aantal sets: ", 1, 20))
    reps = int(vraag_getal("Aantal reps: ", 1, 100))
    gewicht = vraag_getal("Gewicht in kg: ", 0, 500)

    datum = input("Datum (YYYY-MM-DD), laat leeg voor vandaag: ").strip()

    if datum == "":
        datum = str(date.today())

    volume = bereken_volume(sets, reps, gewicht)

    workout = {
        "datum": datum,
        "oefening": oefening,
        "sets": sets,
        "reps": reps,
        "gewicht": gewicht,
        "volume": round(volume, 2)
    }

    return workout


def sla_workout_op(workout):
    os.makedirs("data", exist_ok=True)

    try:
        with open("data/workouts.json", "r", encoding="utf-8") as bestand:
            workouts = json.load(bestand)
    except FileNotFoundError:
        workouts = []
    except json.JSONDecodeError:
        workouts = []

    workouts.append(workout)

    with open("data/workouts.json", "w", encoding="utf-8") as bestand:
        json.dump(workouts, bestand, indent=4, ensure_ascii=False)

    print("\nWorkout succesvol opgeslagen in data/workouts.json.")


def toon_profiel_overzicht(profiel):
    print("\n--- Profiel overzicht ---")
    print(f"Naam: {profiel['naam']}")
    print(f"Leeftijd: {profiel['leeftijd']}")
    print(f"Gewicht: {profiel['gewicht']} kg")
    print(f"Lengte: {profiel['lengte']} cm")
    print(f"BMI: {profiel['bmi']}")


def toon_workout_overzicht(workout):
    print("\n--- Workout overzicht ---")
    print(f"Datum: {workout['datum']}")
    print(f"Oefening: {workout['oefening']}")
    print(f"Sets: {workout['sets']}")
    print(f"Reps: {workout['reps']}")
    print(f"Gewicht: {workout['gewicht']} kg")
    print(f"Volume: {workout['volume']} kg")


def toon_menu():
    print("\n--- FitHelper ---")
    print("1. Profiel aanmaken")
    print("2. Workout toevoegen")
    print("0. Afsluiten")


def main():
    while True:
        toon_menu()
        keuze = input("Kies een optie: ").strip()

        if keuze == "1":
            profiel = maak_profiel()
            sla_profiel_op(profiel)
            toon_profiel_overzicht(profiel)

        elif keuze == "2":
            workout = maak_workout()
            sla_workout_op(workout)
            toon_workout_overzicht(workout)

        elif keuze == "0":
            print("Programma afgesloten.")
            break

        else:
            print("Ongeldige keuze. Probeer opnieuw.")


if __name__ == "__main__":
    main()