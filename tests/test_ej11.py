import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ej11_def import factorial

def test_factorial():
    assert factorial(5) == "La suma de todos los números desde 1 hasta 5 es: 15.0"
    assert factorial(10) == "La suma de todos los números desde 1 hasta 10 es: 55.0"
    assert factorial(20) == "La suma de todos los números desde 1 hasta 20 es: 210.0"

@pytest.mark.parametrize(
    "input_x, expected",
    [
        (5, "La suma de todos los números desde 1 hasta 5 es: 15.0"),
        (10, "La suma de todos los números desde 1 hasta 10 es: 55.0"),
        (20, "La suma de todos los números desde 1 hasta 20 es: 210.0"),
    ]
)

def test_factorial_params(input_x, expected):
    assert factorial(input_x) == expected