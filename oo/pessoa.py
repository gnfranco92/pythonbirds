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

    def cumprimentar(self):  # Metodo: cumprimentar / Objeto:self
        return f'Olá {id(self)}'  # f string!


if __name__ == '__main__':
    guilherme = Pessoa(nome='Guilherme')   # Alterando o nome ja na construção
    sabina = Pessoa(guilherme,nome='Sabina')  # Guilherme entra como filho da Sabina.
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
    print(guilherme.__dict__)    # Atributo especial __dict__, acessa atributos de instância do objeto guilherme, todos os atributos complexos e dinâmicos
    print(sabina.__dict__)

    print('Mostrando o atributo da classe (olhos):', Pessoa.olhos)
    print('Atributo da classe, acessado pelo ojeto guilherme:', guilherme.olhos)
    print("Mostrando que o id é igual para todos os acesso:", id(Pessoa.olhos), "-", id(guilherme.olhos), '-', id(sabina.olhos))


