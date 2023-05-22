import MaquinaTuring as MT

#print("Simulador de Máquina de Turing − IFMG 2023\nDesenvolvido como trabalho prático para a disciplina de Teoria da Computação\nAutores : Tayna\n")

#file = input("Nome do arquivo do algoritmo: ")

#with open (file, "r") as arq:
#    nome = arq.read()
palavra = "abb"

car = 0

cabecote = "(" + palavra[car] + ")" + palavra[(car+1):]
while(True):
    print(cabecote)
    novocabe = str()
    escolha = input("e ou d:")
    if(escolha == "e"):
        for i in range(len(palavra)):
            if(i==car):
                novocabe += palavra[i]
                car = car + 1
                novocabe += "(" + palavra[car] + ")" + palavra[(car+1):]
                cabecote = novocabe
                break
            else:
                novocabe += palavra[i]


#MT(nome)