import os #biblioteca que executa direto no terminal do sistema operacional

def clear_screen():
#Limpa a tela do terminal (Windows e Linux)
    if os.name == 'nt':    #recebe o tipo de Sistema Operacional, se for Windows retorna 'nt'
        os.system('cls')   #'cls' é como o Windows limpa o terminal
    else:
        os.system('clear') #se for Linux, retorna 'posix' então cai no else.

def show_main_menu():
#Exibe o menu principal
    clear_screen()
    print('='*45)
    print('         HOSPITAL MANAGEMENT SYSTEM         ')
    print('='*45)

    print('1. Área de Pacientes')
    print('2. Área de Médicos')
    print('3. Área de Consultas')
    print('4. Relatórios')
    print('0. Sair do Sistema')
    print('='*45)

def get_menu_choice():
#Recebe a escolha do usuário
    return input('Selecione uma opção: ').strip()

