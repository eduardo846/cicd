"""
Tests unitarios para src/app.py
Ejecutar con: pytest tests/ -v
"""
import pytest
from src.app import sumar, saludar


# ─── Tests: sumar ───────────────────────────────────────────
class TestSumar:
    def test_enteros_positivos(self):
        assert sumar(2, 3) == 5

    def test_enteros_negativos(self):
        assert sumar(-1, -4) == -5

    def test_mixto(self):
        assert sumar(-1, 5) == 4

    def test_flotantes(self):
        assert sumar(1.5, 2.5) == pytest.approx(4.0)

    def test_cero(self):
        assert sumar(0, 0) == 0


# ─── Tests: saludar ─────────────────────────────────────────
class TestSaludar:
    def test_nombre_simple(self):
        assert saludar("Hector") == "Hola, Hector!"

    def test_nombre_con_espacios(self):
        assert saludar("  Ana  ") == "Hola, Ana!"

    def test_nombre_vacio_lanza_error(self):
        with pytest.raises(ValueError):
            saludar("")

    def test_nombre_solo_espacios_lanza_error(self):
        with pytest.raises(ValueError):
            saludar("   ")
