import msvcrt
from colorama import Fore, Style

def clear_screen():
    print("\033c", end="")  # Limpa a tela do terminal

def print_menu(items, selected_item):
    clear_screen()
    for i, item in enumerate(items):
        if i == selected_item:
            print(f"{Fore.GREEN}>>> {item}{Style.RESET_ALL}")  # Destaca o item selecionado
        else:
            print(f"    {item}")

def menu():
    items = ["Fazer Login", "Cadastrar usuário", "Sair"]
    selected_item = 0

    while True:
        print("Escolha uma opção:")
        print()
        print_menu(items, selected_item)

        key = msvcrt.getch()

        if key == b'\xe0':  # Tecla especial (setas direcionais)
            key = msvcrt.getch()

            if key == b'H':  # Seta para cima
                selected_item = (selected_item - 1) % len(items)
            elif key == b'P':  # Seta para baixo
                selected_item = (selected_item + 1) % len(items)
        elif key == b'\r':  # Tecla Enter
            if selected_item == len(items) - 1:
                clear_screen()
                print()
                print(f"{Fore.YELLOW}Programa encerrado.{Style.RESET_ALL}")
                print()
                break
            else:
                clear_screen()
                print()
                print(f"Item selecionado: {Fore.BLUE}{items[selected_item]}{Style.RESET_ALL}")
                print()
                break
# Chama a função para iniciar o menu
menu()
