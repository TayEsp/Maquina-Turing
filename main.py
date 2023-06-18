from MaquinaTuring import MaquinaTuring 

file = input("Nome do arquivo do algoritmo: ")

with open (file, "r", encoding="utf-8") as arq:
    codigo = arq.readlines()

print("Simulador de Máquina de Turing − IFMG 2023\nDesenvolvido como trabalho prático para a disciplina de Teoria da Computação\nAutora : Tayna\n")
palavra = input("Forneça a palavra inicial: ")

MT = MaquinaTuring(codigo, palavra)

MT.criaBloco()

def Menu(tipo):
    if(tipo == 'r'):
        parada = MT.resume()
        return parada
    elif(tipo == 'v'):
        parada =  MT.verbose()
        return parada
    elif(tipo == 's'):
        number = input("Quantos passos deseja passar: ")
        parada = True
        while(parada):
            parada = MT.step(number)
            tipo = input("Forneça opção (r, v, s): ")
            Menu(tipo)
        return parada
    else:
        print('opcao Invalida')
        return True


menu = True
while(menu):
    tipo = input("Forneça opção (r, v, s): ")
    menu = Menu(tipo)