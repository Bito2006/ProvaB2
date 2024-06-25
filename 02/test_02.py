from ex_02 import *


def test_obter_lucro_maximo_com_lucro():
    lucro = obter_lucro_maximo([8, 3, 9, 12, 8])
    assert lucro == 9


def test_obter_lucro_maximo_sem_lucro():
    lucro = obter_lucro_maximo([15, 15, 12, 10])
    assert lucro == 0