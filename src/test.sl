// test_program.sl

// Declaracoes de funcoes
func soma(a, b) {
    return a + b;
}

func subtracao(a, b) {
    return a - b;
}

func multiplicacao(a, b) {
    return a * b;
}

func divisao(a, b) {
    if (b == 0) {
        print("Erro: Divisao por zero!");
        return 0;
    }
    return a / b;
}

// Calculo do fatorial (recursivo)
func fatorial(n) {
    if (n <= 1) {
        return 1;
    }
    return n * fatorial(n - 1);
}

// Verifica se um numero e primo
func eh_primo(num) {
    if (num <= 1) {
        return false;
    }
    
    if (num <= 3) {
        return true;
    }
    
    if (num % 2 == 0 || num % 3 == 0) {
        return false;
    }
    
    var i = 5;
    while (i * i <= num) {
        if (num % i == 0 || num % (i + 2) == 0) {
            return false;
        }
        i = i + 6;
    }
    
    return true;
}

// Funcao principal
func main() {
    // Teste de variaveis e tipos
    var inteiro = 42;
    var decimal = 3.14;
    var texto = "Ola, mundo!";
    var booleano = true;
    
    // Teste de operacoes aritmeticas
    var resultado1 = soma(10, 5);
    var resultado2 = subtracao(10, 5);
    var resultado3 = multiplicacao(10, 5);
    var resultado4 = divisao(10, 5);
    
    // Exibicao de resultados
    print("===== TESTE DE OPERACOES ARITMETICAS =====");
    print("Soma: 10 + 5 = " + resultado1);
    print("Subtracao: 10 - 5 = " + resultado2);
    print("Multiplicacao: 10 * 5 = " + resultado3);
    print("Divisao: 10 / 5 = " + resultado4);
    
    // Teste de estruturas condicionais
    print("===== TESTE DE ESTRUTURAS CONDICIONAIS =====");
    var idade = 18;
    
    if (idade >= 18) {
        print("Maior de idade");
    } else {
        print("Menor de idade");
    }
    
    // Teste com operadores de comparacao
    var a = 5;
    var b = 10;
    
    print("===== TESTE DE OPERADORES DE COMPARACAO =====");
    if (a == b) {
        print("a e igual a b");
    }
    
    if (a != b) {
        print("a e diferente de b");
    }
    
    if (a < b) {
        print("a e menor que b");
    }
    
    if (a > b) {
        print("a e maior que b");
    }
    
    if (a <= b) {
        print("a e menor ou igual a b");
    }
    
    if (a >= b) {
        print("a e maior ou igual a b");
    }
    
    // Teste de loops
    print("===== TESTE DE LOOPS =====");
    print("Loop while:");
    var contador = 1;
    while (contador <= 5) {
        print("Contador: " + contador);
        contador = contador + 1;
    }
    
    print("Loop for:");
    for (var i = 1; i <= 5; i = i + 1) {
        print("i: " + i);
    }
    
    // Teste de funcoes matematicas
    print("===== TESTE DE FUNCOES MATEMATICAS =====");
    print("Fatorial de 5: " + fatorial(5));
    
    // Teste de numeros primos
    print("===== TESTE DE NUMEROS PRIMOS =====");
    for (var i = 1; i <= 20; i = i + 1) {
        if (eh_primo(i)) {
            print(i + " e primo");
        } else {
            print(i + " nao e primo");
        }
    }
    
    // Teste final - Mensagem de conclusao
    print("===== TESTE CONCLUIDO =====");
    print("Todos os testes foram executados com sucesso!");
    
    return 0;
}