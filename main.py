import MaquinaTuring as MT

print("Simulador de Máquina de Turing − IFMG 2023\nDesenvolvido como trabalho prático para a disciplina de Teoria da Computação\nAutores : Tayna & Poliana\n")

file = input("Nome do arquivo do algoritmo: ")

with open (file, "r") as arq:
    nome = arq.read()

MT(nome)