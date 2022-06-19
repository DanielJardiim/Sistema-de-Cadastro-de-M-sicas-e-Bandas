from pprintpp import pprint as pp
from classes.BancoDeDados import BandasCRUD

def divider():
    print('\n' + '-' * 80 + '\n')

b = BandasCRUD()

while 1:    
    option = input('1. Create\n2. Read\n3. Update\n4. Delete\n5. Sair\n')

    if option == '1':
        nome = input('  Nome: ')
        estilo = input('   Estilo: ')
        autor = input('  Autor: ')
        quantIntegrantes = input('  QuantIntegrantes: ')
        banda = {
            'nome': nome,
            'estilo': estilo,
            'autor': autor,
            'quantIntegrantes': quantIntegrantes
        }
        aux = b.create(banda)
        divider()

    elif option == '2':
        aux = b.read_bandas()
        pp(aux)
        divider()

    elif option == '3':
        nome = input('  Nome: ')
        estilo = input('   Estilo: ')
        banda = {
            'nome': nome,
            'estilo': estilo
        }
        
        aux = b.update_estilo(banda)
        divider()

    elif option == '4':
        nome = input('  Nome: ')
        banda = {
            'nome': nome
        }
        
        aux = b.delete(banda)
        divider()

    elif option == '5':
        break

b.db.close()