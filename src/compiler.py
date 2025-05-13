import sys
from lexical_analyzer import Lexer, TokenType

class Compiler:
    def __init__(self, source_code):
        self.source_code = source_code
        self.lexer = Lexer(source_code)
        
    def analyze(self):
        """Realiza a análise léxica do código-fonte."""
        tokens = self.lexer.tokenize()
        return tokens
    
    def print_analysis(self, tokens):
        """Imprime o resultado da análise léxica de forma formatada."""
        print("\n======= ANÁLISE LÉXICA =======")
        print(f"{'TIPO':20} {'VALOR':20} {'LINHA':8} {'COLUNA'}")
        print("-" * 60)
        
        for token in tokens:
            if token.type == TokenType.EOF:
                print(f"{'EOF':20} {'':20} {token.line:<8} {token.column}")
            else:
                print(f"{token.type.name:20} {str(token.value):20} {token.line:<8} {token.column}")
    
    def compile_to_python(self, tokens):
        python_code = "#SimpleLang\n\n"
        i = 0
        while i < len(tokens):
            token = tokens[i]

            if token.type in [TokenType.COMMENT, TokenType.WHITESPACE]:
                i += 1
                continue

            if token.type == TokenType.EOF:
                break

            if token.type == TokenType.FUNC:
                python_code += "def "
                i += 1
                continue

            if token.type == TokenType.VAR:
    
                i += 1
                continue
                
            if token.type == TokenType.PRINT:
                python_code += "print"
                i += 1
                continue

            if token.type in [TokenType.IF, TokenType.ELSE, TokenType.WHILE, TokenType.FOR]:
                python_code += token.value + " "
                i += 1
                continue

            if token.type == TokenType.RETURN:
                python_code += "return "
                i += 1
                continue

            if token.type == TokenType.SEMICOLON:
                python_code += "\n"
                i += 1
                continue
                
            if token.type == TokenType.LBRACE:
                python_code += ":\n"
                i += 1
                continue
                
            if token.type == TokenType.RBRACE:
                python_code += "\n"
                i += 1
                continue
                

            python_code += str(token.value) + " "
            i += 1
            
        return python_code


def main():
    if len(sys.argv) < 2:
        print("Uso: python compiler.py arquivo.sl")
        sys.exit(1)
        
    try:
        with open(sys.argv[1], 'r', encoding='utf-8', errors='replace') as file:
            source_code = file.read()
            
        compiler = Compiler(source_code)
        tokens = compiler.analyze()
        compiler.print_analysis(tokens)
        
        python_code = compiler.compile_to_python(tokens)
        
        output_file = sys.argv[1].replace('.sl', '.py')
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(python_code)
            
        print(f"\nCódigo Python gerado em '{output_file}'")
        
    except FileNotFoundError:
        print(f"Erro: Arquivo '{sys.argv[1]}' não encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Erro durante a compilação: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()