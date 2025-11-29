import pytest
from cal import square

def main():
    test_pos()
    test_neg()
    test_zero()
    test_str()

def test_pos():
    assert square(2) == 4
    assert square(3) == 9

def test_neg():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")

if __name__ == "__main__":
    main()