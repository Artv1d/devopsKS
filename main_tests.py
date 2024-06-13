import pytest
from main import back_to_head


def test_back_to_head():
    assert back_to_head(23) == 24
    assert back_to_head(0) == 1
    assert back_to_head(11111) == 11112
    assert back_to_head(89) == 90

if __name__ == "__main__":
    pytest.main()
