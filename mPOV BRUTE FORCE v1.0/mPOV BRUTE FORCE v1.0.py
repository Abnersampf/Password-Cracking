from colorama import Fore
import hashlib, binascii

while True:
    print(f'Informe o hash:')
    print('[EXEMPLO: caf13c4f321b608b27fd75d2549ba53c]')
    hash_entrada = str(input(Fore.LIGHTBLUE_EX + '>> ' + Fore.RESET)).lower().replace(' ', '')

    print(f'\n{"Digite o conjunto de caracteres (sem aspas)":^94}')
    print('-'*94)
    print('[EXEMPLO_1: \"abcdefghijklmnopqrstuvwxyz\"]')
    print('[EXEMPLO_2: \"ABCDEFGHIJLKMNOPQRSTUVWXYZ\"]')
    print('[EXEMPLO_3: \"abcdefghijklmnopqrstuvwxyzABCDEFGHIJLKMNOPQRSTUVWXYZ\"]')
    print('[EXEMPLO_4: \"abcdefghijklmnopqrstuvwxyzABCDEFGHIJLKMNOPQRSTUVWXYZ0123456789\"]')
    print('[EXEMPLO_5: \"abcdefghijklmnopqrstuvwxyzABCDEFGHIJLKMNOPQRSTUVWXYZ0123456789!@#$%&*_+-=-,.?/\\\"]')
    charset_Escolhido = str(input(Fore.LIGHTBLUE_EX + '>> ' + Fore.RESET))
    print(f'\nConjunto de caracteres escolhido: \"{Fore.GREEN + charset_Escolhido + Fore.RESET}\"')

    caracteres = [0] * (len(charset_Escolhido) + 1)
    caracteres[0] = ''
    for c in range(1, len(caracteres)):
        caracteres[c] = charset_Escolhido[c - 1]

    print('\nDeseja ver as combinações sendo geradas? [s/n]')
    print(Fore.RED + '[ATIVAR ESSA OPÇÃO REDUZ O DESEMPENHO DO PROGRAMA]' + Fore.RESET)
    ver = input(Fore.LIGHTBLUE_EX + '>> ' + Fore.RESET)
    while ver not in 'sn':
        print(Fore.RED + 'Opção inválida - Tente novamente!' + Fore.RESET)
        ver = input(Fore.LIGHTBLUE_EX + '>> ' + Fore.RESET)

    print('\nIniciando o processo de quebra de senha...')
    print('AGARDE...')

    senha = ''
    hash = ''
    hash_final = ''
    for c in range(0, len(caracteres)):
        if str(hash_final) == hash_entrada:
            break
        for c2 in range(0, len(caracteres)):
            if str(hash_final) == hash_entrada:
                break
            for c3 in range(0, len(caracteres)):
                if str(hash_final) == hash_entrada:
                    break
                for c4 in range(0, len(caracteres)):
                    if str(hash_final) == hash_entrada:
                        break
                    for c5 in range(0, len(caracteres)):
                        if str(hash_final) == hash_entrada:
                            break
                        for c6 in range(0, len(caracteres)):
                            if str(hash_final) == hash_entrada:
                                break
                            for c7 in range(0, len(caracteres)):
                                if str(hash_final) == hash_entrada:
                                    break
                                for c8 in range(0, len(caracteres)):
                                    senha = f'{caracteres[c] + caracteres[c2] + caracteres[c3] + caracteres[c4] + caracteres[c5] + caracteres[c6] + caracteres[c7] + caracteres[c8]}'
                                    if ver == 's':
                                        print(senha)
                                    hash = hashlib.new('md4', senha.encode('utf-16le')).digest()
                                    hash_final = binascii.hexlify(hash).decode()
                                    if str(hash_final) == hash_entrada:
                                        break
    if str(hash_final) == hash_entrada:
        print(f'\nO hash {Fore.BLUE + hash_entrada + Fore.RESET} corresponde a string \"{Fore.BLUE + senha + Fore.RESET}\"')
    else:
        print(Fore.RED + 'A senha ultrapassa 8 caracteres, não foi possível encontrar um hash correspondente!' + Fore.RESET)

    print('\nQuer quebrar outro hash? [s/n]')
    outro_hash = input(Fore.LIGHTBLUE_EX + '>> ' + Fore.RESET)
    while outro_hash not in 'sn':
        print(Fore.RED + 'Opção inválida - Tente novamente!' + Fore.RESET)
        outro_hash = input(Fore.LIGHTBLUE_EX + '>> ' + Fore.RESET)
    print()
    if outro_hash == 'n':
        break