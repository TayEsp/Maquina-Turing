class MaquinaTuring:

    #a função init é a função construtora da classe
    def __init__(self, AlfabetoFita, tipo, palavra):
        self.AlfabetoFita = str(AlfabetoFita)
        self.blocos = dict()
        self.estadoAtual = []
        self.cabecote = str(palavra[0])
        self.palavra = str(palavra)

    def criaBloco(self):
        self.blocos

    def mudaCabecote(self):
        self.cabecote