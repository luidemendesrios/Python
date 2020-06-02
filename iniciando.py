#Este documento é uma introdução a linguagem Python
#Pode ser usado também como um guia rápido para lembrar de algum comando que esqueceu

#O comentário abaixo serve para poder ativar utf-8 para poder usar acentuação e outros símbolos. 

# -*- coding: utf-8 -*-

#Comando para printar um texto na tela
#SAÍDAS:

print('Olá Mundo')

#Saída usando VARIÁVEIS

nome = "Luiz"
linguagem = "python"
print("Olá, seja bem vindo %s. 'Vamos começar a programar em %s." % (nome, linguagem))

#ENTRADAS

name  = input("What is your name?")
quest = input("What is your quest?")
color = input("What is your favorite color?")

print("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color) )

#COMENTÁRIOS

#Em linha

#EM bloco

'''isto é uma multi-linha comentar, eu sou útil para comentar todo pedaços de código muito rápido  '''



