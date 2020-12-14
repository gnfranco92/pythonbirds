"""
Primeira Classe - criada
"""


# Classe pep 8  - Função letra minuscula e Classe letra maiuscula
# Colocar o estado de todos arquivos, tirando uma foto, fazendo o Push para enviar no repositorio no GitHub; direito na pasta -> Git - > Commit Directory
# Subir no GitHub depois da Print, CTRl+SHIFT+K OU direito na pasta -> Git - > PUSH

# Atribuir Metode (Função que pertence a uma classe, sempre conectado a um objeto

class Pessoa:
    def __init__(self, nome = None, idade=35):    # Criando método especial -- self.nome ( O nome é o nome do objeto self)
        self.idade = idade
        self.nome = nome          # Criando atributo!

    # Atributos de instância e de objetos são criados atreves do metódo __init__

    def cumprimentar(self):  # Metodo: cumprimentar / Objeto:self
        return f'Olá {id(self)}'  # f string!


if __name__ == '__main__':
    p = Pessoa('Guilherme')     # Alterando o nome ja na construção
    print(Pessoa.cumprimentar(p))  # Não é usual executar o método desta maneira
    print(id(p))
    print(p.cumprimentar())  # p: objeto, objeto.método, maneira mais usual!!! - ATRIBUTO DA CLASSE
    print(p.nome)        # Acessar o atributo atraves do objeto
    p.nome = 'Guilherme'  # Alterar o valor do atributo!
    print(p.nome)
    print(p.idade)

