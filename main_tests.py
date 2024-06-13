import pytest
from main import back_to_head


def test_back_to_head():
    assert back_to_head(23) == 32
    assert back_to_head(0) == 0
    assert back_to_head(11111) == 11111
    assert back_to_head(89) == 98

if __name__ == "__main__":
    pytest.main()
