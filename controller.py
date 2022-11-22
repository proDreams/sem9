import view
import model


def run():
    while True:
        num = view.print_menu()
        if num == '1':
            model.show_file()
        elif num == '2':
            model.add_line()
        elif num == '0':
            break
