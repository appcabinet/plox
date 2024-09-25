from tokens import Token, TokenType
from main import Lox


class Scanner:
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1

    def scan_tokens(self):
        while not self.is_at_end():
            # We are at the beginning of the next lexeme.
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens

    def scan_token(self):
        switcher = {
            '(': self.add_token(TokenType.LEFT_PAREN),
            ')': self.add_token(TokenType.RIGHT_PAREN),
            '{': self.add_token(TokenType.LEFT_BRACE),
            '}': self.add_token(TokenType.RIGHT_BRACE),
            ',': self.add_token(TokenType.COMMA),
            '.': self.add_token(TokenType.DOT),
            '-': self.add_token(TokenType.MINUS),
            '+': self.add_token(TokenType.PLUS),
            ';': self.add_token(TokenType.SEMICOLON),
            '*': self.add_token(TokenType.STAR),
        }
        c = self.advance()
        func = switcher.get(c, lambda: None)
        func()

    def handle_default_token_case(self):
        Lox.error(self.line, "Unexpected character.")

    def advance(self):
        self.current += 1
        return self.source[self.current - 1]

    def add_token(self, token_type: TokenType):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(token_type, text, None, self.line))



    def is_at_end(self):
        return self.current >= len(self.source)

    def scan_token(self):
        # This method should be implemented to scan the next token.
        pass
