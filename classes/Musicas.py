from pprintpp import pprint as pp
from classes.BancoDeDados import MusicasCRUD

def divider():
    print('\n' + '-' * 80 + '\n')

m = MusicasCRUD()

while 1:    
    option = input('1. Create\n2. Read\n3. Update\n4. Delete\n5. Sair\n')

    if option == '1':
        nome = input('  Nome: ')
        estilo = input('   Estilo: ')
        autor = input('  Autor: ')
        duracao = input('  Duração: ')
        musica = {
            'nome': nome,
            'estilo': estilo,
            'autor': autor,
            'duracao': duracao
        }
        aux = m.create(musica)
        divider()

    elif option == '2':
        aux = m.read_musicas()
        pp(aux)
        divider()

    elif option == '3':
        nome = input('  Nome: ')
        estilo = input('   Estilo: ')
        musica = {
            'nome': nome,
            'estilo': estilo
        }
        
        aux = m.update_estilo(musica)
        divider()

    elif option == '4':
        nome = input('  Nome: ')
        musica = {
            'nome': nome
        }
        
        aux = m.delete(musica)
        divider()

    elif option == '5':
        break

m.db.close()