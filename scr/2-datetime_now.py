'''
Ejecutando un script programado
Este es un ejemplo sencillo de como pedirle a github actions
que ejecute programas agendados
'''

## Libreria --------
import datetime


## Código---------
def main():
    now = datetime.datetime.utcnow()
    print(f"Script executed at: {now} UTC")

if __name__ == "__main__":
    main()
