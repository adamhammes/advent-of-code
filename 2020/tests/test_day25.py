from day25 import *


def test_determine_loop_size():
    assert determine_loop_size(5764801) == 8
    assert determine_loop_size(17807724) == 11
