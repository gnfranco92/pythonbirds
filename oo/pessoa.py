"""
Primeira Classe - criada
"""


# Classe pep 8  - Função letra minuscula e Classe letra maiuscula
# Colocar o estado de todos arquivos, tirando uma foto, fazendo o Push para enviar no repositorio no GitHub; direito na pasta -> Git - > Commit Directory
# Subir no GitHub depois da Print, CTRl+SHIFT+K OU direito na pasta -> Git - > PUSH

# Atribuir Metode (Função que pertence a uma classe, sempre conectado a um objeto

class Pessoa: # Objeto tipo pessoa, dentro de uma lista que é atributo que é instancia da própria classe pessoa.
    olhos = 2  # Criano atributo Default ou atributo de Classe

    def __init__(self, *filhos, nome = None, idade=35):
        self.idade = idade
        self.nome = nome          # Criando método especial -- self.nome ( O nome é o nome do objeto self)
        self.filhos = list(filhos)          # Criando a lista filhos, objeto complexo

    # Atributos de instância e de objetos são criados atreves do metódo __init__

    def cumprimentar(self):  # Metodo: cumprimentar / Objeto indice:self
        return f'Olá, meu nome é: {self.nome}' # f string!

    @staticmethod         # Criar metodo estatico da classe, independe do objeto. Decoraitor começa com @
    def metodo_estatico(): # Não precisa informar o parametro, devido o metodo ser da classe
        return 42

    @classmethod     # Criar metodo estatico da classe, independe do objeto. Decoraitor começa com @. Tera acesso a classe que esta executando.
    def nome_e_atributos_de_classe(cls):  # cls é preenchido automatico, cls = 'class'
        return f'{cls} - olhos {cls.olhos}'  # Acessar o atribuo olhos da classe Pessoa


class testando_metodo_super(Pessoa):
    pass

# Herença, reutilizar o código de uma classe ja pré-existente
class Homem(testando_metodo_super):
    def cumprimentar(self):
        #cumprimentar_da_classe = Pessoa.cumprimentar(self)      # Não é usual, porque se for pegar da classe Mutante, teria problema.
        cumprimentar_da_classe = super().cumprimentar()          # Utilizar o método especial super, acessa os elementos da classe pai, seja ela quem for, não precisa estar descrita no ().
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    guilherme = Mutante(nome='Guilherme')   # Alterando o nome ja na construção e Utilizando a classe herdada Homem.
    sabina = Homem(guilherme,nome='Sabina')  # Guilherme entra como filho da Sabina.
    print(Pessoa.cumprimentar(sabina))  # Não é usual executar o método desta maneira
    print(id(sabina))
    print(sabina.cumprimentar())  # p: objeto, objeto.método, maneira mais usual!!! - ATRIBUTO DA CLASSE
    print(sabina.nome)        # Acessar o atributo atraves do objeto
    # p.nome = 'Guilherme'  # Alterar o valor do atributo!
    # print(p.nome)
    print(sabina.idade)
    for filho in sabina.filhos:
        print('Filhos:', filho.nome)  # Lista com todos os filhos

    guilherme.sobrenome = 'Neto'  # Adicinando atributo para objeto especifico de maneira DINÂMICA
    del sabina.filhos             # Deleta os atributos do objeto sabina, remover de forms DINÂMICA, não é boa prática!
    print('Mostra o __dict__ de Guilherme: ', guilherme.__dict__)    # Atributo especial __dict__, acessa atributos de instância do objeto guilherme, todos os atributos complexos e dinâmicos
    print('Mostra o __dict__ de Sabina: ', sabina.__dict__)
    print('---' * 30)

    print('Mostrando o atributo da classe (olhos):', Pessoa.olhos)
    print('Atributo da classe, acessado pelo ojeto guilherme:', guilherme.olhos)
    print("Mostrando que o id é igual para todos os acesso:", id(Pessoa.olhos), "-", id(guilherme.olhos), '-', id(sabina.olhos))
    print('---' * 30)

    print('Mostrando o metodo estático da classe:', Pessoa.metodo_estatico(),'\nMetodo estático da classe acessado pelo objeto guilherme:', guilherme.metodo_estatico())

    print('---'*30)

    print('Mostrando o metodo da classe:', Pessoa.nome_e_atributos_de_classe(),'\nMetodo da classe acessado pelo objeto guilherme:', guilherme.nome_e_atributos_de_classe())

    print('---'*30)

    # Se o objeto pessoa é do tipo Pessoa.
    pessoa = Pessoa('Anonimo')
    print('Se o objeto pessoa é do tipo Pessoa.')
    print(isinstance(pessoa, Pessoa))
    print('Se o objeto pessoa é do tipo Homem.')
    print(isinstance(pessoa, Homem))

    print('Se a instância de homem pessoa é do tipo Pessoa.')
    print(isinstance(guilherme, Pessoa))
    print('Se a instância de homem pessoa é do tipo Homem.')
    print(isinstance(guilherme, Homem))

    print('---' * 30)

    # Sobrescria de Atributos

    print('Mostra quantos olhos o Guilherme tem: ', guilherme.olhos)

    print('---' * 30)

    # Sobrescria de Metodo

    print('', guilherme.cumprimentar())

    print('', sabina.cumprimentar())



