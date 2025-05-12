from antlr4 import *
from grammar.JavaSubsetLexer import JavaSubsetLexer
from grammar.JavaSubsetParser import JavaSubsetParser
from src.ASTPrinter import ColoredASTPrinter
from src.ErrorListener import CustomErrorListener
from colorama import init, Fore, Style

init()  # Инициализация colorama для цветного вывода


def main():
    try:
        # Чтение входного файла
        input_stream = FileStream("examples/input.java", encoding='utf-8')
        # Лексический анализатор
        lexer = JavaSubsetLexer(input_stream)
        stream = CommonTokenStream(lexer)

        # Синтаксический анализатор
        parser = JavaSubsetParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(CustomErrorListener())

        # Построение AST
        tree = parser.program()

        # Печать AST
        printer = ColoredASTPrinter()
        printer.visit(tree)

        # Вывод AST в консоль
        printer.print_to_console()

        print(Fore.GREEN + "Парсинг завершен успешно!" + Style.RESET_ALL)

    except FileNotFoundError:
        print(Fore.RED + "Ошибка: файл input.java не найден" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Произошла ошибка: {str(e)}" + Style.RESET_ALL)


if __name__ == '__main__':
    main()
