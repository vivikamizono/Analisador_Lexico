# 🌟 Atividade de Compiladores - 7º Semestre 🌟

## 💻 Sobre o Projeto
Este repositório contém um código escrito em **Flex** para a atividade da disciplina de **Compiladores**, feita no **7º semestre** de **Ciências da Computação**. A atividade serve para me ajudar a colocar em prática os conceitos estudados em sala de aula.

## 📚 Descrição da Atividade
Este projeto é um analisador léxico simples utilizando Flex, que reconhece os seguintes padrões:
- Palavras-chave: if, else, while
- Identificadores: Variáveis e nomes válidos
- Números inteiros: Sequências numéricas
- Operadores aritméticos: +, -, *, /

## 📌 Como Compilar e Executar

📌 Como Compilar e Executar

- 1️⃣ Requisitos
    - Flex
    - GCC (GNU Compiler Collection)

- 2️⃣ Passos para Compilar
    - Execute os seguintes comandos no terminal:
```bash
flex lexer.l
gcc lex.yy.c -o lexer -lfl
./lexer < input.txt

