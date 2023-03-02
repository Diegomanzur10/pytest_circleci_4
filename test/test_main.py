from code.main import suma, resta, multiplicacion, division
import pytest

@pytest.fixture()
def return_valor():
    return 3

@pytest.mark.parametrize(
       (
            "a",
            "b",
            "valor_esperado",
       ),

       [
            (
                2,
                3,
                5,
            ),

            (
                4, 
                6,
                10
            ),
            (
                5, 
                6,
                11
            ),
       ],
       ids=[
    "test1",
    "test2"
       ] 
)
def test_suma(a, b, valor_esperado):
    assert suma(a, b) == valor_esperado

#@pytest.mark.skip(reason = "Funcion a depricar")
@pytest.mark.xfail()
def test_division():
    assert division(return_valor, 0) == 1
