from ex_01 import *


def test_obter_acrescimos():
    acrescimos_t1, acrescimos_t2 = obter_acrescimos(108)
    assert acrescimos_t1 == 6
    assert acrescimos_t2 == 12