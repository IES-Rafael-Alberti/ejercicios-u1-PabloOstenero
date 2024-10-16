import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ej01_def import saludo

def test_saludo():
    assert saludo("Manolo") == "Hola, Manolo."
    assert saludo("Pepe") == "Hola, Pepe."
    assert saludo("Antonio") == "Hola, Antonio."

@pytest.mark.parametrize(
    "input_x, expected",
    [
        ("Manolo", "Hola, Manolo."),
        ("Pepe", "Hola, Pepe."),
        ("Antonio", "Hola, Antonio."),
    ]
)

def test_saludo_params(input_x, expected):
    assert saludo(input_x) == expected