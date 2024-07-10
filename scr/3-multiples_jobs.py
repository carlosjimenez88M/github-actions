'''
Multiples Jobs
En este cápitulo quiero que abordemos como generar proceos secuenciales
'''

# Importando librerias -------
import os


# Diseñando una función ------

def main():
    name = os.getenv("USERNAME")
    print(f"Hola {name} estas viendo una clase de CICD de la Nacional")


if __name__ == '__main__':
    main()