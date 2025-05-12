from antlr4.tree.Tree import TerminalNodeImpl
from colorama import Fore, Style


class ColoredASTPrinter:
    def __init__(self):
        self.output = ""
        self.indent_level = 0
        self.colors = {
            'TerminalNodeImpl': Fore.YELLOW,
            'ProgramContext': Fore.CYAN,
            'ClassDefContext': Fore.MAGENTA,
            'FieldDeclContext': Fore.GREEN,
            'MethodDeclContext': Fore.BLUE,
            'TypeContext': Fore.WHITE,
            'StatementContext': Fore.RED,
            'ExprContext': Fore.CYAN,
        }

    def visit(self, node):
        if isinstance(node, TerminalNodeImpl):
            self._print_terminal(node)
        else:
            self._print_non_terminal(node)

    def _print_terminal(self, node):
        node_type = type(node).__name__
        color = self.colors.get(node_type, Fore.WHITE)
        self.output += "  " * self.indent_level + color + node.getText() + Style.RESET_ALL + "\n"

    def _print_non_terminal(self, node):
        node_type = type(node).__name__
        color = self.colors.get(node_type, Fore.WHITE)
        self.output += "  " * self.indent_level + color + node_type + Style.RESET_ALL + "\n"
        self.indent_level += 1
        for child in node.getChildren():
            self.visit(child)
        self.indent_level -= 1

    def print_to_console(self):
        print("\n" + "=" * 50 + " Дерево AST " + "=" * 50)
        print(self.output)
        print("=" * 100 + "\n")

    def get_output(self):
        return "\n".join(self.output)
