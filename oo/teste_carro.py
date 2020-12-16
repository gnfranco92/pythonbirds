# Biblioteca de teste unittest

from unittest import TestCase
from carro import Motor


class CarroTesteCase(TestCase):
    def test_velocidade(self):  # Tem que começar com o prefixo test ou teste ou não será reconhecido.
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)