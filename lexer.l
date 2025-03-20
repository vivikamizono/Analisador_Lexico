%{
#include <stdio.h>
#include "y.tab.h"
%}

%%

"if"      { printf("PALAVRA-CHAVE: %s\n", yytext); }
"else"    { printf("PALAVRA-CHAVE: %s\n", yytext); }
"while"   { printf("PALAVRA-CHAVE: %s\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]* { printf("IDENTIFICADOR: %s\n", yytext); }
[0-9]+    { printf("NÚMERO INTEIRO: %s\n", yytext); }
[+\-*/]   { printf("OPERADOR: %s\n", yytext); }
[ \t\n]   ; /* Ignorar espaços, tabulações e quebras de linha */
.         { printf("CARACTERE INVÁLIDO: %s\n", yytext); }

%%

int main() {
    printf("Digite um código para análise léxica:\n");
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}

