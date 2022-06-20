from classes.Musicas import Musicas
from classes.Bandas import Bandas
from classes.BancoDeDados import Relacionamentos

def divider():
    print('\n' + '-' * 80 + '\n')

while 1:    
    option = input('1. Musicas\n2. Bandas\n3. Relação\n4. Deletar Banco\n5. Sair\n')

    if option == '1':
        Musicas()
    
    elif option == '2':
        Bandas()
    
    elif option == '3':
        nome1 = input("Nome da Musica: ")
        nome2 = input("Nome da Banda: ")
        desde = input("Desde de quando está Musica pertence a está Banda: ")

        musica = {'nome': nome1}
        banda = {'nome': nome2}
        relacao = {'desde': desde}

        aux = Relacionamentos().create_relation(musica, banda, relacao)
        divider()

    elif option == '4':
        aux = Relacionamentos().delete_all_nodes()
        divider()

    elif option == '5':
        break

    else:
        option = input('1. Musicas\n2. Bandas\n3. Relação\n4. Deletar Banco\n5. Sair\n')