import os
os.system

login_cadastrado = "marcio"
senha_cadastrada = "3366"

login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

if login == login_cadastrado and senha == senha_cadastrada:
    print("Bem-vindo")
else:
    print("Login ou senha incorretos")


