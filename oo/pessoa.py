"""
Primeira Classe - criada
"""

# Classe pep 8  - Função letra minuscula e Classe letra maiuscula
# Coloca o estado de todos arquivos, tirando uma foto, fazendo o Push para enviar no repositorio no GitHub; direito na pasta -> Git - > Commit Directory
# Subir no GitHub depois da Print, CTRl+SHIFT+K OU direito na pasta -> Git - > PUSH

# Atribuir Metode (Função que pertence a uma classe, sempre conectado a um objeto

class Pessoa:
    def cumprimentar(self):    # Metodo: cumprimentar / Objeto:self
        return f'Olá {id(self)}'  # f string!

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))  # Não é usual executar o método desta maneira
    print(id(p))
    print(p.cumprimentar())   # p: objeto, objeto.método, maneira mais usual!!!
