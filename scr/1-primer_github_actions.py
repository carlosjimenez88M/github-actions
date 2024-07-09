'''
Primer CI
En este ejercicio entenderemos como diseñaremos nuestros
script para poder ejecutar códigos de manera Pro!!
Como ustedes mis amigos, pro! 👨🏻‍💻
'''


# Importando librerias -------
import os


# Diseñando una función ------

def main():
    name = os.getenv("USERNAME")
    print(f"Hola {name} estas viendo una clase de CICD de la Nacional")


if __name__ == '__main__':
    main()