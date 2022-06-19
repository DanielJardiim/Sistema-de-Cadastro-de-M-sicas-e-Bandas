def divider():
    print('\n' + '-' * 80 + '\n')

while 1:    
    option = input('1. Musicas\n2. Bandas\n3. Sair\n')

    if option == '1':
        from classes.Musicas import MusicasCRUD
        MusicasCRUD()
    
    elif option == '2':
        from classes.Bandas import BandasCRUD
        BandasCRUD()
    
    elif option == '3':
        break

    else:
        option = input('1. Musicas\n2. Bandas\n3. Sair\n')