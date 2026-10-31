
import pytest

from agente_ucv.agent import explicar_concepto, calcular_promedio


def test_explicar_concepto_correcto():
    resultado = explicar_concepto("API")
    assert resultado is not None
    assert isinstance(resultado, dict)


def test_explicar_concepto_desconocido():
    resultado = explicar_concepto("concepto_inexistente")
    assert isinstance(resultado, dict)


def test_explicar_concepto_vacio():
    resultado = explicar_concepto("")
    assert isinstance(resultado, dict)


def test_calcular_promedio_correcto():
    resultado = calcular_promedio([15, 18, 20])
    assert isinstance(resultado, dict)
    assert resultado["status"] == "success"
    assert resultado["resultado"] == pytest.approx(17.67)


def test_calcular_promedio_lista_vacia():
    resultado = calcular_promedio([])
    assert isinstance(resultado, dict)
    assert resultado["status"] == "error"
    assert resultado["resultado"] is None


def test_calcular_promedio_datos_no_numericos():
    resultado = calcular_promedio(["a", "b", "c"])
    assert isinstance(resultado, dict)
    assert resultado["status"] == "error"
    assert resultado["resultado"] is None
