
from src.triangle import triangle_type

def test_equilateral_triangle():
    assert triangle_type(3, 3, 3) == "Equilateral"

def test_isosceles_triangle():
    assert triangle_type(3, 4, 3) == "Isosceles"
    assert triangle_type(3, 3, 4) == "Isosceles"
    assert triangle_type(4, 3, 3) == "Isosceles"

def test_scalene_triangle():
    assert triangle_type(3, 4, 5) == "Scalene"
    assert triangle_type(5, 3, 4) == "Scalene"
    assert triangle_type(4, 5, 3) == "Scalene"

def test_not_a_triangle():
    assert triangle_type(1, 2, 3) == "Not a triangle"
    assert triangle_type(3, 1, 2) == "Not a triangle"
    assert triangle_type(2, 3, 1) == "Not a triangle"
