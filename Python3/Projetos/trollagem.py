def banner():
    print(f'{verde}.s5ssSs.   .s5SSSs.   .s5SSSs.   .s5SSSs.   .s5SSSs.   s. ')
    print('   SS SS.        SS.        SS.        SS.        SS.  SS.')
    print('sS SS S%S  sS    S%S  sS    `:;  sS    S%S  sS    `:;  S%S')
    print('SS :; S%S  SSSs. S%S  SS         SSSs. S%S  `:;;;;.    S%S')
    print('SS :; S%S  SSSs. S%S  SS         SSSs. S%S  `:;;;;.    S%S')
    print('SS    S%S  SS    S%S  SS         SS    S%S        ;;.  S%S')
    print('SS    `:;  SS    `:;  SS         SS    `:;        `:;  `:;')
    print('SS    ;,.  SS    ;,.  SS    ;,.  SS    ;,.  .,;   ;,.  ;,.')
    print(f':;    ;:   :;    ;:   `:;;;;;:   :;    ;:   `:;;;;;:   ;:{fim_da_cor}')


def escolha():
    opcao = int(input(f'Digite a opção:\n[1] Consulta nome {verde}[on]{fim_da_cor}\n[2] Consulta número {verde}[on]{fim_da_cor}\n[3] Consulta cpf {vermelho}[off]{fim_da_cor}\n[4] consulta mãe {vermelho}[off]{fim_da_cor}\n[5] Consulta cnpj {verde}[on]{fim_da_cor}\n[6] Créditos\n   >>>'))


verde = '\033[0;32m'
vermelho = '\033[0;31m'
fim_da_cor = '\033[m'

banner()
escolha()