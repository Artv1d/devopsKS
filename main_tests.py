import pytest
from main import back_to_head


def test_dummy():
    pass

def test_back_to_head():
    assert back_to_head(123) == 321
    assert back_to_head(0) == 0
    assert back_to_head(432) == 234
    assert back_to_head(123342) == 243321
    assert back_to_head(52) == 25
    assert back_to_head(106) == 601
    assert back_to_head(1234567) == 7654321
    assert back_to_head(55555555) == 55555555
    assert back_to_head(91832) == 23819
    assert back_to_head(777) == 777
    assert back_to_head(993) == 399


if __name__ == "__main__":
    pytest.main()
