import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ej04_def2 import calcular_celsius

def test_calcular_celsius():
    assert calcular_celsius(212) == 100
    assert calcular_celsius(0) == -17.78
    assert calcular_celsius(28) == -2.22

@pytest.mark.parametrize(
    "input_x, expected",
    [
        (212, 100),
        (0, -17.78),
        (28, -2.22)
    ]
)

def test_calcular_celsius_params(input_x, expected):
    assert calcular_celsius(input_x) == expected