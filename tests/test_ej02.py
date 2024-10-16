import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ej02_def import Importe

def test_Importe():
    assert Importe(10, 2) == 20
    assert Importe(2, 0) == 0
    assert Importe(10, 10) == 100

@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (10, 2, 20),
        (2, 0, 0),
        (10, 10, 100)
    ]
)

def test_Importe_params(input_x, input_y, expected):
    assert Importe(input_x, input_y) == expected