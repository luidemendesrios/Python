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
'''
name  = input("What is your name?")
quest = input("What is your quest?")
color = input("What is your favorite color?")

print("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color) )
'''

#COMENTÁRIOS

#Em linha

#EM bloco

'''isto é uma multi-linha comentar, eu sou útil para comentar todo pedaços de código muito rápido  '''

#Tipos de dados básico

'''
Números:	int, long, float, complex
Strings:	str e unicode
Listas e tuplas:	list, tuple
Dicionários:	dict
Arquivos:	file
Booleanos:	bool (True, False)
Conjuntos:	set, frozenset
None:	
'''

#A função type() mostra o tipo do dado, veja alguns exemplos.

'''
type("text")        # <class 'str'>
type(1)             # <class 'int'>
type(0.99)          # <class 'float'>

x = 1    # int
y = 2.8  # float
z = 1j   # complex
'''

#Também é possível elaborar as seguintes expressões.

type(1) == int      # True
type(0.99) == float # True

#-------

#NÚMEROS

'''
Python possui todos os operadores matemáticos sendo alguns deles
soma: +
multiplicação: *
subtração: -
divisão: /
resta da divisão: %
potenciação **
exemplos:
'''

x = 2
y = 9

soma = x + y
subt = x - y
mult = x * y
div = x / y
restoDiv = x % y
pot = x**y

print('O resultado das operações')
print(f'soma:{soma}')
print(f'subtração:{subt}')
print(f'multiplicação:{mult}')
print(f'divisão:{div}')
print(f'resto da divisão:{restoDiv}')
print(f'potencia: {pot}')

#Veja também algumas funções matemáticas:

max(5, 6, 7) # 7 | pega o maior número
min(5, 6, 7) # 5 | pega o menor número
abs(-1)      # 1 | pega o módulo de um número

#Para trabalhar com números randômicos será preciso importar o módulo random.

import random

gerador = random.randint(1, 10)
#O código acima irá gerar números randômicos entre 1 e 10 (incluindo o 1 e o 10).
print(f'O número gerado e: {gerador}')


#Obs: Deve se levar em conta quando realizar uma operação matemática a ordem de precedência dos operadores que são
'''
Tabela 4.2: Precedência Geral de Operadores Aritméticos
Ordem	Operação	Símbolo
 1ª	    Parênteses	  ()
 2ª	    Potenciação	  **
 3ª	    Multiplicação, Divisão, Resto e Divisão Inteira	*, /, mod, div
 4ª	    Adição, Subtração	+, -

'''
#Exemplo de uma operação 

equacao = (5+3)**2 * (5-2) + 8 
print(equacao) #resposta 200


#CONVERSÃO DE TIPO

x = 1 #int
y = 2.5 #float
z = 1j #complex

#converte de int para float:
a = float(x)

#Converte de float para int:
b = int(y)

#Converte de int para complexo:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))




