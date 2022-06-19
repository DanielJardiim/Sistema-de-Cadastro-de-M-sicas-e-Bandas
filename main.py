from classes.Musicas import Musicas
from classes.Bandas import Bandas

def divider():
    print('\n' + '-' * 80 + '\n')

while 1:    
    option = input('1. Musicas\n2. Bandas\n3. Sair\n')

    if option == '1':
        Musicas()
    
    elif option == '2':
        Bandas()
    
    elif option == '3':
        break

    else:
        option = input('1. Musicas\n2. Bandas\n3. Sair\n')