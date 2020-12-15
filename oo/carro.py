

"""
Você deve criar uma classe carro que vai possuir dois atributos compostos por duas outras classe:
1. Motor
2. Direção

Motor - terá a responsabilidade de controlar a velocidade.
Ele oferece os atributos:
1. Atributo de dado velocidade;
2. Método acelearar, que deverá incrementar a velocidade de uma unidade;
3. Método frear que deverá decrementar a velocidade em duas unidade.

Direção - terá a responsabilidade de controlar a direção.
Ela oferece os atributos:
1. Valor da direção com valores possíveis: Norte, Sul, Leste, Oeste;
2. Método girar_a_direita
3. Método girar_a_esquerda

  N
O   L
  S

  Exemplo:
  >>> # Testando motor
  >>> motor = Motor()
  >>> motor.velocidade
  0
  >>> motor.acelerar()
  >>> motor.velocidade
  1
  >>> motor.acelerar()
  >>> motor.velocidade
  2
  >>> motor.acelerar()
  >>> motor.velocidade
  3

  >>> motor.frear()
  >>> motor.velocidade
  1
  >>> motor.frear()
  >>> motor.velocidade
  0

 >>> # Testando direção
 >>> direcao = Direcao()
 >>> direcao.valor
 'Norte'
 >>> direcao.girar_a_direita()
 >>> direcao.valor
 'Leste'
 >>> direcao.girar_a_direita()
 >>> direcao.valor
 'Sul'
 >>> direcao.girar_a_direita()
 >>> direcao.valor
 'Oeste'
 >>> direcao.girar_a_direita()
 >>> direcao.valor
 'Norte'
 >>> direcao.girar_a_esquerda()
 >>> direcao.valor
 'Oeste'
 >>> direcao.girar_a_esquerda()
 >>> direcao.valor
 'Sul'
 >>> direcao.girar_a_esquerda()
 >>> direcao.valor
 'Leste'

 >>> carro = Carro(direcao,motor)
 >>> carro.calcular_velocidade()
 0
 >>> carro.acelerar()
 >>> carro.calcular_velocidade()
 1
 >>> carro.acelerar()
 >>> carro.calcular_velocidade()
 2
 >>> carro.frear()
 >>> carro.calcular_velocidade()
 0
 >>> carro.calcular_direcao()
 'Leste'
 >>> carro.girar_a_direita()
 >>> carro.calcular_direcao()
 'Sul'

"""

# Convensão para variável constante

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'


class Direcao:
    rotacao_a_direita_dct = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotacao_a_esquerda_dct = {NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL}

    def __init__(self):
        self.valor = NORTE         # Norte é a partida da direção!!

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]  # Maneira de não utilizar o If, diminuindo o código.

        # if self.valor == NORTE:
        #     self.valor = LESTE
        # elif self.valor == LESTE:
        #     self.valor = SUL
        # elif self.valor == SUL:
        #     self.valor = OESTE

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)    # Função Max - Se existir valor menor que '0', retorna o '0', se não retorna o valor da velocidade.


class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        return self.direcao.girar_a_direita()
    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()










