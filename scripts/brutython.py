import os
import requests
from time import sleep
from random import randint

#path = '/root/Documents/scripts' #Poe o Path de exec
#lista = 'user_lista.txt' #Poe tua lista
#url = 'http://www.google.com' #Sua_Url se tu for usar estatico

def starter():
	print('Bem-Vindo ao Brutython, Url bruteforce feito em Python por @SeuNick')
	print('Altere diretamente no script se for mais de um argumento!\n')

	lista = raw_input('Passa o path da lista: ')
	url = raw_input('Digite a URL: ')
	variavel = raw_input('Campo que iremos Bruceforciar: ')
	str(variavel)
	leitura(url, variavel, lista)

def conn(url, variavel, line):
	new_url = url.replace(variavel, line.rstrip())
	print(new_url)
	response = requests.get(new_url)
	print response.status_code
