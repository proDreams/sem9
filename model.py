import controller
import view


def show_file():
    with open("file.csv", "r", encoding="utf-8") as f:
        lines = f.readlines()
        view.print_file(lines)


def add_line():
    with open("file.csv", "a", encoding="utf-8") as f:
        data = view.input_data()
        f.write(f'{data}')
