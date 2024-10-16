import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ej05_def2 import precio_final

def test_precio_final():
    assert precio_final(20, 37) == "El precio final del artículo con IVA (37.00) es 27.40€."
    assert precio_final(100, -1) == "El precio final del artículo con IVA (21.00) es 121.00€."
    assert precio_final(40, 200) == "El precio final del artículo con IVA (21.00) es 48.40€."

@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (20, 37, "El precio final del artículo con IVA (37.00) es 27.40€."),
        (100, -1, "El precio final del artículo con IVA (21.00) es 121.00€."),
        (40, 200, "El precio final del artículo con IVA (21.00) es 48.40€."),
    ]
)

def test_precio_final_params(input_x, input_y, expected):
    assert precio_final(input_x, input_y) == expected