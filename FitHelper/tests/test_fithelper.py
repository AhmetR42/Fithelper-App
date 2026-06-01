import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

from main import (
    bereken_bmi,
    bereken_volume,
    bereken_totaal_volume,
    vind_zwaarste_workout,
    vind_meest_getrainde_oefening
)

def test_bereken_bmi():
    bmi = bereken_bmi(80, 180)

    assert round(bmi, 2) == 24.69


def test_bereken_volume():
    volume = bereken_volume(3, 10, 50)

    assert volume == 1500


def test_bereken_totaal_volume():
    workouts = [
        {
            "oefening": "Bench press",
            "sets": 3,
            "reps": 10,
            "gewicht": 50,
            "volume": 1500
        },
        {
            "oefening": "Squat",
            "sets": 4,
            "reps": 8,
            "gewicht": 70,
            "volume": 2240
        }
    ]

    totaal = bereken_totaal_volume(workouts)

    assert totaal == 3740


def test_vind_zwaarste_workout():
    workouts = [
        {
            "datum": "2026-06-01",
            "oefening": "Bench press",
            "volume": 1500
        },
        {
            "datum": "2026-06-02",
            "oefening": "Squat",
            "volume": 2240
        }
    ]

    zwaarste = vind_zwaarste_workout(workouts)

    assert zwaarste["oefening"] == "Squat"
    assert zwaarste["volume"] == 2240


def test_vind_meest_getrainde_oefening():
    workouts = [
        {"oefening": "Bench press", "volume": 1500},
        {"oefening": "Squat", "volume": 2240},
        {"oefening": "Bench press", "volume": 1600}
    ]

    oefening, aantal = vind_meest_getrainde_oefening(workouts)

    assert oefening == "bench press"
    assert aantal == 2