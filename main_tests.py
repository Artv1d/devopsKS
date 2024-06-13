import pytest
from main import back_to_head


def test_add():
    assert back_to_head(23) == 32
    assert back_to_head(0) == 0
    assert back_to_head(11111) ==11111
    assert back_to_head(89) == 98
    with pytest.raises(Zeroback_to_headError):
        back_to_head(1, 0)


if __name__ == "__main__":
    pytest.main()
