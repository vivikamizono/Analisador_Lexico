import re
from enum import Enum, auto

class TokenType(Enum):
    # Palavras-chave
    VAR = auto()          # var
    FUNC = auto()         # func
    IF = auto()           # if
    ELSE = auto()         # else
    WHILE = auto()        # while
    FOR = auto()          # for
    RETURN = auto()       # return
    TRUE = auto()         # true
    FALSE = auto()        # false
    PRINT = auto()        # print
    INPUT = auto()        # input
    
    # Tipos de dados
    INT = auto()          # int
    FLOAT = auto()        # float
    STRING = auto()       # string
    BOOL = auto()         # bool
    
    # Literais
    INTEGER = auto()      # 123
    DECIMAL = auto()      # 123.45
    STRING_LITERAL = auto() # "texto"
    
    # Identificadores
    IDENTIFIER = auto()   # nome_variavel
    
    # Operadores
    PLUS = auto()         # +
    MINUS = auto()        # -
    MULTIPLY = auto()     # *
    DIVIDE = auto()       # /
    MODULO = auto()       # %
    ASSIGN = auto()       # =
    
    # Operadores de comparação
    EQUAL = auto()        # ==
    NOT_EQUAL = auto()    # !=
    GREATER = auto()      # >
    LESS = auto()         # <
    GREATER_EQUAL = auto() # >=
    LESS_EQUAL = auto()   # <=
    
    # Delimitadores
    LPAREN = auto()       # (
    RPAREN = auto()       # )
    LBRACE = auto()       # {
    RBRACE = auto()       # }
    SEMICOLON = auto()    # ;
    COMMA = auto()        # ,
    
    # Outros
    COMMENT = auto()      # // comentário
    WHITESPACE = auto()   # espaços, tabs, quebras de linha
    EOF = auto()          # fim do arquivo
    UNKNOWN = auto()      # caractere desconhecido

class Token:
    def __init__(self, token_type, value, line, column):
        self.type = token_type
        self.value = value
        self.line = line
        self.column = column
    
    def __str__(self):
        return f"Token({self.type}, '{self.value}', linha={self.line}, coluna={self.column})"

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.line = 1
        self.column = 1
        self.current_char = self.source_code[0] if len(self.source_code) > 0 else None
        
        # Palavras-chave da linguagem
        self.keywords = {
            'var': TokenType.VAR,
            'func': TokenType.FUNC,
            'if': TokenType.IF,
            'else': TokenType.ELSE,
            'while': TokenType.WHILE,
            'for': TokenType.FOR,
            'return': TokenType.RETURN,
            'true': TokenType.TRUE,
            'false': TokenType.FALSE,
            'print': TokenType.PRINT,
            'input': TokenType.INPUT,
            'int': TokenType.INT,
            'float': TokenType.FLOAT,
            'string': TokenType.STRING,
            'bool': TokenType.BOOL,
        }
    
    def advance(self):
        """Avança para o próximo caractere."""
        self.position += 1
        self.column += 1
        
        if self.position >= len(self.source_code):
            self.current_char = None
        else:
            self.current_char = self.source_code[self.position]
            
            # Atualiza linha e coluna se for quebra de linha
            if self.current_char == '\n':
                self.line += 1
                self.column = 0
    
    def peek(self, n=1):
        """Retorna o caractere n posições à frente, sem avançar."""
        peek_pos = self.position + n
        if peek_pos >= len(self.source_code):
            return None
        return self.source_code[peek_pos]
    
    def skip_whitespace(self):
        """Pula espaços em branco."""
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
    
    def skip_comment(self):
        """Pula comentários de linha."""
        # Comentário de linha (//...)
        if self.current_char == '/' and self.peek() == '/':
            while self.current_char is not None and self.current_char != '\n':
                self.advance()
            if self.current_char == '\n':
                self.advance()
    
    def get_identifier(self):
        """Processa um identificador ou palavra-chave."""
        start_column = self.column
        result = ''
        
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        
        # Verifica se é uma palavra-chave
        token_type = self.keywords.get(result, TokenType.IDENTIFIER)
        return Token(token_type, result, self.line, start_column)
    
    def get_number(self):
        """Processa um número (inteiro ou decimal)."""
        start_column = self.column
        result = ''
        is_decimal = False
        
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            if self.current_char == '.':
                if is_decimal:  # Já encontrou um ponto decimal
                    break
                is_decimal = True
            result += self.current_char
            self.advance()
        
        token_type = TokenType.DECIMAL if is_decimal else TokenType.INTEGER
        value = float(result) if is_decimal else int(result)
        return Token(token_type, value, self.line, start_column)
    
    def get_string(self):
        """Processa uma string literal."""
        start_column = self.column
        self.advance()  # Pula a primeira aspas
        result = ''
        
        while self.current_char is not None and self.current_char != '"':
            # Tratamento de caracteres de escape
            if self.current_char == '\\' and self.peek() == '"':
                self.advance()  # Pula o '\'
                result += self.current_char  # Adiciona as aspas escapadas
            else:
                result += self.current_char
            self.advance()
        
        if self.current_char == '"':
            self.advance()  # Pula a última aspas
        else:
            # Erro: string não terminou
            pass
        
        return Token(TokenType.STRING_LITERAL, result, self.line, start_column)
    
    def get_operator_or_punctuation(self):
        """Processa operadores e pontuação."""
        start_column = self.column
        char = self.current_char
        
        if char == '+':
            self.advance()
            return Token(TokenType.PLUS, '+', self.line, start_column)
        elif char == '-':
            self.advance()
            return Token(TokenType.MINUS, '-', self.line, start_column)
        elif char == '*':
            self.advance()
            return Token(TokenType.MULTIPLY, '*', self.line, start_column)
        elif char == '/':
            # Verifica se é um comentário
            if self.peek() == '/':
                comment_start = self.position
                self.advance()  # Pula o primeiro '/'
                self.advance()  # Pula o segundo '/'
                
                comment_text = ""
                while self.current_char is not None and self.current_char != '\n':
                    comment_text += self.current_char
                    self.advance()
                
                return Token(TokenType.COMMENT, comment_text, self.line, start_column)
            else:
                self.advance()
                return Token(TokenType.DIVIDE, '/', self.line, start_column)
        elif char == '%':
            self.advance()
            return Token(TokenType.MODULO, '%', self.line, start_column)
        elif char == '=':
            if self.peek() == '=':
                self.advance()
                self.advance()
                return Token(TokenType.EQUAL, '==', self.line, start_column)
            else:
                self.advance()
                return Token(TokenType.ASSIGN, '=', self.line, start_column)
        elif char == '!':
            if self.peek() == '=':
                self.advance()
                self.advance()
                return Token(TokenType.NOT_EQUAL, '!=', self.line, start_column)
            else:
                self.advance()
                return Token(TokenType.UNKNOWN, '!', self.line, start_column)
        elif char == '>':
            if self.peek() == '=':
                self.advance()
                self.advance()
                return Token(TokenType.GREATER_EQUAL, '>=', self.line, start_column)
            else:
                self.advance()
                return Token(TokenType.GREATER, '>', self.line, start_column)
        elif char == '<':
            if self.peek() == '=':
                self.advance()
                self.advance()
                return Token(TokenType.LESS_EQUAL, '<=', self.line, start_column)
            else:
                self.advance()
                return Token(TokenType.LESS, '<', self.line, start_column)
        elif char == '(':
            self.advance()
            return Token(TokenType.LPAREN, '(', self.line, start_column)
        elif char == ')':
            self.advance()
            return Token(TokenType.RPAREN, ')', self.line, start_column)
        elif char == '{':
            self.advance()
            return Token(TokenType.LBRACE, '{', self.line, start_column)
        elif char == '}':
            self.advance()
            return Token(TokenType.RBRACE, '}', self.line, start_column)
        elif char == ';':
            self.advance()
            return Token(TokenType.SEMICOLON, ';', self.line, start_column)
        elif char == ',':
            self.advance()
            return Token(TokenType.COMMA, ',', self.line, start_column)
        else:
            self.advance()
            return Token(TokenType.UNKNOWN, char, self.line, start_column)
    
    def get_next_token(self):
        """Retorna o próximo token."""
        while self.current_char is not None:
            # Ignora espaços em branco
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
                
            # Identificador ou palavra-chave
            if self.current_char.isalpha() or self.current_char == '_':
                return self.get_identifier()
                
            # Número
            if self.current_char.isdigit():
                return self.get_number()
                
            # String
            if self.current_char == '"':
                return self.get_string()
                
            # Operadores e pontuação
            return self.get_operator_or_punctuation()
        
        # Fim do arquivo
        return Token(TokenType.EOF, None, self.line, self.column)
    
    def tokenize(self):
        """Retorna uma lista de todos os tokens no código fonte."""
        tokens = []
        
        while True:
            token = self.get_next_token()
            tokens.append(token)
            
            if token.type == TokenType.EOF:
                break
                
        return tokens


# Exemplo de uso
def analyze_code(source_code):
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    
    print("Análise Léxica:")
    for token in tokens:
        if token.type != TokenType.EOF:
            print(token)


# Código de teste
if __name__ == "__main__":
    test_code = """
    // Programa de exemplo na nossa linguagem
    func calcular_media(a, b) {
        var media = (a + b) / 2;
        return media;
    }
    
    func main() {
        var x = 10;
        var y = 20.5;
        var resultado = calcular_media(x, y);
        
        if (resultado > 15) {
            print("Valor alto!");
        } else {
            print("Valor baixo!");
        }
        
        return 0;
    }
    """
    
    analyze_code(test_code)