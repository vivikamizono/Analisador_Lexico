# 🚀 Trabalho de Compiladores

Olá! Este é nosso **Trabalho de Compiladores** que realizamos no 7º semestre do Curso de Ciências Da Computação para a matéria de Compiladores. 🧠💻

---

## 📚 Sobre o Projeto

Este projeto tem como objetivo demonstrar, de forma prática, as etapas clássicas do funcionamento de um compilador. Através do desenvolvimento de um compilador simples, buscamos aplicar os conceitos teóricos estudados em sala de aula, como análise léxica, análise sintática, análise semântica, geração de código e otimizações básicas. O projeto proporciona uma compreensão mais profunda dos mecanismos internos de compilação, reforçando o aprendizado e a importância de cada etapa no processo de tradução de linguagens de alto nível para código executável.

---

## 🛠️ Tecnologias Utilizadas

- Linguagem de Programação: `Python` 
- Paradigma Utilizado: Programação Orientada a Objetos (POO)
- Funcionalidades Implementadas Manualmente:
  - **Analisador Léxico (Lexer):** desenvolvido do zero em Python, sem uso de ferramentas externas como Flex.
  - **Sistema de Tokens:** usando enum.Enum para definir os tipos de tokens da linguagem.
  - **Leitura Interativa de Código:**  via input() para permitir que o usuário insira seu próprio código fonte em tempo real.

---

## 📂 Estrutura do Projeto
- **lexer.py**: Arquivo que implementa o analisador léxico da linguagem. Ele é responsável por percorrer o código-fonte, identificar os diferentes componentes (como palavras-chave, operadores, identificadores, literais, etc.) e gerar uma lista de tokens que representam esses elementos de forma estruturada. Inclui as definições das classes TokenType, Token e Lexer.
- **main.py**: Este é o ponto de entrada do programa. Ele permite ao usuário digitar ou colar um código-fonte personalizado para ser analisado. Internamente, ele instancia o Lexer, realiza a tokenização do código e imprime os tokens identificados. Serve como interface principal de uso do analisador.
 



