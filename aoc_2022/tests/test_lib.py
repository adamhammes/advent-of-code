from lib import *


def test_extract_ints():
    assert extract_ints("123 -923") == [123, -923]
