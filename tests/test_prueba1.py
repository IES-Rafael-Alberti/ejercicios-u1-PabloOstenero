import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.prueba1 import cual_es_mayor

def test_cual_es_mayor():
    assert cual_es_mayor(10, 2) == 10
    assert cual_es_mayor(2, 10) == 10
    assert cual_es_mayor(10, 10) == 0

@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (10, 2, 10),
        (2, 10, 10),
        (10, 10, 0)
    ]
)

def test_cual_es_mayor_params(input_x, input_y, expected):
    assert cual_es_mayor(input_x, input_y) == expected