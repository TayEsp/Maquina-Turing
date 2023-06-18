class MaquinaTuring:

    #a função init é a função construtora da classe
    def __init__(self, codigo, palavra):
        self.Codigo = codigo
        self.blocos = dict()
        self.anterior = []
        self.estadoAtual = []
        self.blocoAtual = dict()
        self.fita = str()
        self.cabecote = str(palavra[0])
        self.palavra = str(palavra)
        self.flagErro = True

    def __str__(self):
         s = str('.'*int(20 - len(self.blocoAtual[0][0])) + self.blocoAtual[0][0] + '.' +
                  '0'*int(4 - len(str(self.estadoAtual[0]))) + self.estadoAtual[0] + ':' +
                  self.fita)
         return s

    def criaFita(self):
        #colocado o tamanho dos espacos em branco, dependendo do tamanho da palavra
        tam = int((40 - (len(self.palavra)))/2)
        
        #criando a fita com os espacos em vazio e a palavra
        if (tam%2) == 0:
            self.fita = str(('_'*(tam+1)) + "(" + self.palavra[0] + ")" + self.palavra[(1):] + ('_'*(tam)))
        else:
            self.fita = str(('_'*(tam)) + "(" + self.palavra[0] + ")" + self.palavra[(1):] + ('_'*(tam)))

    def criaBloco(self):
        self.criaFita()
        chave = None
        estados = []

        for linha in self.Codigo:
            estado = linha.split()
            #retirando os comentarios
            if ';' in estado:
                pass
            #colocando os blocos na chave do dicinario e colocando so estados dentro do conteudo
            elif 'bloco' in estado:
                if chave != None:
                    self.blocos[chave] = estados
                    estados = []
                chave = str(estado[1])
                estados.append(estado[1:])
            #colocando os estados em listas  
            else:
                if len(estado) > 0:
                    #retirando o separador --
                    if '--' in estado:
                        estado.remove('--')
                    estados.append(estado)
        self.blocos[chave] = estados
        self.mudaBloco('main')
        #for k in self.blocos:
        #    print("{} = {}".format(k,self.blocos[k]))

    def mudaBloco(self, bloco):
        self.blocoAtual = self.blocos[bloco]
        number = self.blocoAtual[0][1]

        #fazendo a verificacao de qual é o primeiro estado
        for estado in self.blocoAtual:
            if estado[0].isdigit() and int(estado[0]) == int(number):
                if (self.cabecote == estado[1] or estado[1] == '*') and len(estado)==5:
                    self.estadoAtual = estado
                    break
                else:
                    self.estadoAtual = estado
                    break

    def mudaEstadoAtual(self):  
        self.flagErro = True
        #se o estado atual for de parar
        if self.estadoAtual == 'pare':
            return False
        #se o estado for do tipo nao mover de bloco
        if(len(self.estadoAtual) == 5):
            #procurando os estados para trocar o cabecote e trocar o estado atual
            for estado in self.blocoAtual:
                if(self.cabecote == self.estadoAtual[1] or self.estadoAtual[1] == '*'):
                    if (self.estadoAtual[4] == estado[0]):
                        self.mudaCabecote(self.estadoAtual[3], self.estadoAtual[2])
                        self.estadoAtual = estado
                        self.flagErro = False
                        break
                    elif self.estadoAtual[4] == 'pare':
                        self.mudaCabecote(self.estadoAtual[3], self.estadoAtual[2])
                        self.flagErro = False
                        return False
                    elif self.estadoAtual[4] == 'retorne':
                        self.mudaCabecote(self.estadoAtual[3], self.estadoAtual[2])
                        self.flagErro = False
                        if self.anterior[0] != 'pare':
                            self.estadoAtual = self.anterior[0][1]
                            self.blocoAtual = self.blocos[self.anterior[0][0][0]]
                            self.anterior.remove(self.anterior[0])
                        else:
                            self.estadoAtual = self.anterior[0]
                        break
            for sameEstado in self.blocoAtual:
                if len(sameEstado) == 3 and len(self.estadoAtual) == 3:
                    self.flagErro = False
                    break
                if self.estadoAtual[0] == sameEstado[0] and (sameEstado[1] == '*' or self.cabecote == sameEstado[1]):
                    self.estadoAtual = sameEstado
                    self.flagErro = False
                    break
        elif(len(self.estadoAtual) == 3):
            if self.estadoAtual[2] == 'pare':
                self.flagErro = False
                self.anterior.insert(0,'pare')
            for estado in self.blocoAtual:
                if(self.estadoAtual[2] == estado[0]):
                    self.flagErro = False
                    self.anterior.insert(0,[self.blocoAtual[0], estado])
                    break
            self.mudaBloco(self.estadoAtual[1])
        if(self.flagErro):
            print('ERRO!')
            quit()
        return True

    def mudaCabecote(self, direcao, letra):
        novaFita = str()
        car = 0
        if direcao == 'd':
            for i in range(len(self.fita)):
                #adicionando todas as letras antes do cabecote
                if self.fita[i] != '(':
                    novaFita += self.fita[i]
                #depois que chegar no cabecote colocar ou a nova letra ou a letra antiga do cabecote
                else:
                    car = i + 1
                    if(letra != '*'):
                        novaFita += letra
                    else:
                        novaFita += self.fita[car]
                    break
            #adicionando o cabecote
            novaFita += '('
            if self.fita[car+2] != '_':
                novaFita += self.fita[car+2]
                self.cabecote = self.fita[car+2]
                novaFita += ')'
                #depois adicionar o cabecote colocando o resto do 
                for i in range(car+3,len(self.fita)):
                    novaFita += self.fita[i]
            else:
                self.cabecote = '_'
                novaFita += '_'
                novaFita += ')'
                #escrevendo o resto da fita
                for i in range(car+3,len(self.fita)):
                    novaFita += self.fita[i]
        #andando para esquerda
        elif direcao == 'e':
            for i in range(len(self.fita)):
                #adicionando todas as letras antes do cabecote
                if self.fita[i] != '(':
                    novaFita += self.fita[i]
                #depois que chegar no cabecote colocar ou a nova letra ou a letra antiga do cabecote
                else:
                    #colocando o cabecote
                    novaFita += novaFita[i-1]
                    self.cabecote = novaFita[i-1]
                    novaFita = novaFita[:(i-1)] + '(' + novaFita[i:]
                    novaFita += ')'
                    car = i + 1
                    #escrevendo a nova letra ou antiga
                    if(letra != '*'):
                        novaFita += letra
                    else:
                        novaFita += self.fita[car]
                    break
            #escrevendo o resto da fita
            if car+2 < len(self.fita):
                for i in range(car+2,len(self.fita)):
                    novaFita += self.fita[i]
        elif(direcao == 'i'):
            for i in range(len(self.fita)):
                #adicionando todas as letras antes do cabecote
                if self.fita[i] != '(':
                    novaFita += self.fita[i]
                #depois que chegar no cabecote colocar ou a nova letra ou a letra antiga do cabecote
                else:
                    #colocando o cabecote
                    novaFita += novaFita[i-1]
                    if(letra != '*'):
                        novaFita = novaFita[:(i)] + '(' + letra
                        self.cabecote = letra
                    else:
                        novaFita = novaFita[:(i)] + '(' + self.fita[i+1]
                        self.cabecote = self.fita[i+1]
                    novaFita += ')'
                    car = i + 1
                    break
            if car+2 < len(self.fita):
                    for i in range(car+2,len(self.fita)):
                        novaFita += self.fita[i]
        self.fita = novaFita

    def resume(self):
        parada = True
        print(self)
        while(parada):
            parada = self.mudaEstadoAtual()
            if(self.estadoAtual[len(self.estadoAtual)-1] == '!'):
                print(self)
                self.estadoAtual.remove('!')
                print('BREAKPOINT!')
                return True
        print(self)
        return False
        
    def verbose(self):
        parada = True
        print(self)
        while(parada):
            parada = self.mudaEstadoAtual()
            print(self)
            if(self.estadoAtual[len(self.estadoAtual)-1] == '!'):
                self.estadoAtual.remove('!')
                print('BREAKPOINT!')
                return True
        return False
    
    def step(self, number):
        parada = True
        print(self)
        for i in range(int(number)):
            parada = self.mudaEstadoAtual()
            print(self)
            if(self.estadoAtual[len(self.estadoAtual)-1] == '!'):
                self.estadoAtual.remove('!')
                print('BREAKPOINT!')
                return True
            elif(parada == False):
                return False
        return False