import tkinter as tk
from tkinter import scrolledtext
from enum import Enum, auto

# === Seus tipos de tokens ===
class TokenType(Enum):
    VAR = auto(); FUNC = auto(); IF = auto(); ELSE = auto()
    WHILE = auto(); FOR = auto(); RETURN = auto(); TRUE = auto(); FALSE = auto()
    PRINT = auto(); INPUT = auto()
    INT = auto(); FLOAT = auto(); STRING = auto(); BOOL = auto()
    INTEGER = auto(); DECIMAL = auto(); STRING_LITERAL = auto()
    IDENTIFIER = auto()
    PLUS = auto(); MINUS = auto(); MULTIPLY = auto(); DIVIDE = auto(); MODULO = auto(); ASSIGN = auto()
    EQUAL = auto(); NOT_EQUAL = auto(); GREATER = auto(); LESS = auto(); GREATER_EQUAL = auto(); LESS_EQUAL = auto()
    LPAREN = auto(); RPAREN = auto(); LBRACE = auto(); RBRACE = auto(); SEMICOLON = auto(); COMMA = auto()
    COMMENT = auto(); WHITESPACE = auto(); EOF = auto(); UNKNOWN = auto()

class Token:
    def __init__(self, token_type, value, line, column):
        self.type = token_type
        self.value = value
        self.line = line
        self.column = column

    def __str__(self):
        return f"Token({self.type.name}, '{self.value}', linha={self.line}, coluna={self.column})"

# === Lexer simplificado ===
class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.line = 1
        self.column = 1
        self.current_char = self.source_code[0] if self.source_code else None
        self.keywords = {
            'var': TokenType.VAR, 'func': TokenType.FUNC, 'if': TokenType.IF,
            'else': TokenType.ELSE, 'while': TokenType.WHILE, 'for': TokenType.FOR,
            'return': TokenType.RETURN, 'true': TokenType.TRUE, 'false': TokenType.FALSE,
            'print': TokenType.PRINT, 'input': TokenType.INPUT,
            'int': TokenType.INT, 'float': TokenType.FLOAT,
            'string': TokenType.STRING, 'bool': TokenType.BOOL
        }

    def advance(self):
        if self.current_char == '\n':
            self.line += 1
            self.column = 0
        self.position += 1
        self.column += 1
        self.current_char = self.source_code[self.position] if self.position < len(self.source_code) else None

    def peek(self):
        return self.source_code[self.position + 1] if self.position + 1 < len(self.source_code) else None

    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()

    def get_identifier(self):
        start_col = self.column
        result = ''
        while self.current_char and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        token_type = self.keywords.get(result, TokenType.IDENTIFIER)
        return Token(token_type, result, self.line, start_col)

    def get_number(self):
        start_col = self.column
        result = ''
        is_decimal = False
        while self.current_char and (self.current_char.isdigit() or self.current_char == '.'):
            if self.current_char == '.':
                if is_decimal:
                    break
                is_decimal = True
            result += self.current_char
            self.advance()
        token_type = TokenType.DECIMAL if is_decimal else TokenType.INTEGER
        return Token(token_type, result, self.line, start_col)

    def get_string(self):
        start_col = self.column
        self.advance()  # skip opening "
        result = ''
        while self.current_char and self.current_char != '"':
            result += self.current_char
            self.advance()
        self.advance()  # skip closing "
        return Token(TokenType.STRING_LITERAL, result, self.line, start_col)

    def get_operator(self):
        start_col = self.column
        c = self.current_char
        next_c = self.peek()
        if c == '=' and next_c == '=':
            self.advance(); self.advance()
            return Token(TokenType.EQUAL, '==', self.line, start_col)
        if c == '!' and next_c == '=':
            self.advance(); self.advance()
            return Token(TokenType.NOT_EQUAL, '!=', self.line, start_col)
        if c == '<' and next_c == '=':
            self.advance(); self.advance()
            return Token(TokenType.LESS_EQUAL, '<=', self.line, start_col)
        if c == '>' and next_c == '=':
            self.advance(); self.advance()
            return Token(TokenType.GREATER_EQUAL, '>=', self.line, start_col)
        simple_tokens = {
            '+': TokenType.PLUS, '-': TokenType.MINUS, '*': TokenType.MULTIPLY,
            '/': TokenType.DIVIDE, '%': TokenType.MODULO, '=': TokenType.ASSIGN,
            '>': TokenType.GREATER, '<': TokenType.LESS,
            '(': TokenType.LPAREN, ')': TokenType.RPAREN,
            '{': TokenType.LBRACE, '}': TokenType.RBRACE,
            ';': TokenType.SEMICOLON, ',': TokenType.COMMA
        }
        if c in simple_tokens:
            self.advance()
            return Token(simple_tokens[c], c, self.line, start_col)
        else:
            self.advance()
            return Token(TokenType.UNKNOWN, c, self.line, start_col)

    def get_next_token(self):
        while self.current_char:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isalpha() or self.current_char == '_':
                return self.get_identifier()
            if self.current_char.isdigit():
                return self.get_number()
            if self.current_char == '"':
                return self.get_string()
            return self.get_operator()
        return Token(TokenType.EOF, None, self.line, self.column)

    def tokenize(self):
        tokens = []
        while True:
            token = self.get_next_token()
            tokens.append(token)
            if token.type == TokenType.EOF:
                break
        return tokens

# === Interface com Tkinter ===
class LexerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Analisador Léxico com Tkinter")

        # Entrada de código-fonte
        self.input_area = scrolledtext.ScrolledText(root, width=80, height=15, font=("Consolas", 12))
        self.input_area.pack(padx=10, pady=10)

        # Botão de análise
        self.analyze_button = tk.Button(root, text="Analisar", command=self.analyze)
        self.analyze_button.pack(pady=5)

        # Saída de tokens
        self.output_area = scrolledtext.ScrolledText(root, width=80, height=15, font=("Consolas", 12), state='disabled')
        self.output_area.pack(padx=10, pady=10)

    def analyze(self):
        code = self.input_area.get("1.0", tk.END)
        lexer = Lexer(code)
        tokens = lexer.tokenize()

        self.output_area.config(state='normal')
        self.output_area.delete("1.0", tk.END)

        for token in tokens:
            if token.type != TokenType.EOF:
                self.output_area.insert(tk.END, str(token) + '\n')

        self.output_area.config(state='disabled')

# Executa a interface
if __name__ == "__main__":
    root = tk.Tk()
    gui = LexerGUI(root)
    root.mainloop()
