import sys #importa biblioteca que mexe nas funções e parâmetros do próprio Python.
from ui.cli import show_main_menu, get_menu_choice, clear_screen #importa funções dos arquivos do próprio projeto.

def main():
#Estamos definindo o menu ao invés de escrever na raiz pois assim as variáveis não são criadas para todo o código.
#é como se estivesse sido criado dentro de uma caixa segura, isso evita conflitos e bugs difíceis de achar.

    while True:
        show_main_menu()
        try: #é como se dissesse 'tente rodar o código normalmente'.
            choice = get_menu_choice()

            if choice == '1':
                input('[Módulo de Pacientes] Em breve, pressione Enter para voltar.')
            elif choice =='2':
                input('[Módulo de Médicos] Em breve, pressione Enter para voltar.')
            elif choice =='3':
                input('[Módulo de Consultas] Em breve, pressione Enter para voltar.')
            elif choice == '4':
                input('[Módulo de Relatórios] Em breve, pressione Enter para voltar.')
            elif choice == '0':
                clear_screen()
                print('Sistema encerrado!')
                sys.exit(0)
            else:
                input('Opção inválida! Tente novamente.')
        
        except KeyboardInterrupt: #Caso o usuário aperte Ctrl+C, evita o travamento feio do terminal.
            clear_screen()
            print('Sistema interrompido pelo usuário.')
            sys.exit(0) #0: código universal de computação que indica sucesso (zero erros).
                        #caso fosse 1 ou outro número: crash ou erro crítico. 

if __name__ == "__main__":
#Toda vez que o Python roda um arquivo, ele cria uma variável escondida chamada __name__
#Se eu abrir o terminal agora e digitar 'python main.py' O Python define que __name__ do arquivo é __main__
    main()