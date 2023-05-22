class MaquinaTuring:

    #a função init é a função construtora da classe
    def __init__(self, AlfabetoFita, tipo, palavra):
        self.AlfabetoFita = str(AlfabetoFita)
        self.blocos = dict()
        self.estadoAtual = []
        self.cabecote = palavra
        self.palavra = str(palavra)