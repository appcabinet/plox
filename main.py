import sys
import os

from scanner import Scanner


class Lox:
    had_error = False

    @staticmethod
    def main(args):
        if len(args) > 1:
            print("Usage: pylox [script]")
            sys.exit(64)
        elif len(args) == 1:
            Lox.run_file(args[0])
        else:
            Lox.run_prompt()

    @staticmethod
    def run_file(path):
        with open(path, 'r', encoding='utf-8') as file:
            contents = file.read()
        Lox.run(contents)
        if Lox.had_error:
            sys.exit(65)

    @staticmethod
    def run_prompt():
        while True:
            try:
                line = input("> ")
                Lox.run(line)
                had_error = False
            except EOFError:
                break
            print()  # Add a newline for better formatting

    @staticmethod
    def run(source):
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()

        for token in tokens:
            print(token)

    @staticmethod
    def error(line, message):
        Lox.report(line, "", message)

    @staticmethod
    def report(line, where, message):
        print(f"[line {line}] Error{where}: {message}", file=sys.stderr)
        Lox.had_error = True

if __name__ == "__main__":
    Lox.main(sys.argv[1:])

