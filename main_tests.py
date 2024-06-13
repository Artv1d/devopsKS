import pytest
from main import back_to_head


def test():
    assert back_to_head(123) == 321
    assert back_to_head(0) == 0
    assert back_to_head(432) == 234
    assert back_to_head(123342) == 243321


if __name__ == "__main__":
    pytest.main()
