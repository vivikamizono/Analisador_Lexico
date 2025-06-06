# Código Python gerado a partir do SimpleLang

def soma ( a , b ) :
return a + b 

def subtracao ( a , b ) :
return a - b 

def multiplicacao ( a , b ) :
return a * b 

def divisao ( a , b ) :
if ( b == 0 ) :
print( Erro: Divisao por zero! ) 
return 0 

return a / b 

def fatorial ( n ) :
if ( n <= 1 ) :
return 1 

return n * fatorial ( n - 1 ) 

def eh_primo ( num ) :
if ( num <= 1 ) :
return false 

if ( num <= 3 ) :
return true 

if ( num % 2 == 0 | | num % 3 == 0 ) :
return false 

i = 5 
while ( i * i <= num ) :
if ( num % i == 0 | | num % ( i + 2 ) == 0 ) :
return false 

i = i + 6 

return true 

def main ( ) :
inteiro = 42 
decimal = 3.14 
texto = Ola, mundo! 
booleano = true 
resultado1 = soma ( 10 , 5 ) 
resultado2 = subtracao ( 10 , 5 ) 
resultado3 = multiplicacao ( 10 , 5 ) 
resultado4 = divisao ( 10 , 5 ) 
print( ===== TESTE DE OPERACOES ARITMETICAS ===== ) 
print( Soma: 10 + 5 =  + resultado1 ) 
print( Subtracao: 10 - 5 =  + resultado2 ) 
print( Multiplicacao: 10 * 5 =  + resultado3 ) 
print( Divisao: 10 / 5 =  + resultado4 ) 
print( ===== TESTE DE ESTRUTURAS CONDICIONAIS ===== ) 
idade = 18 
if ( idade >= 18 ) :
print( Maior de idade ) 

else :
print( Menor de idade ) 

a = 5 
b = 10 
print( ===== TESTE DE OPERADORES DE COMPARACAO ===== ) 
if ( a == b ) :
print( a e igual a b ) 

if ( a != b ) :
print( a e diferente de b ) 

if ( a < b ) :
print( a e menor que b ) 

if ( a > b ) :
print( a e maior que b ) 

if ( a <= b ) :
print( a e menor ou igual a b ) 

if ( a >= b ) :
print( a e maior ou igual a b ) 

print( ===== TESTE DE LOOPS ===== ) 
print( Loop while: ) 
contador = 1 
while ( contador <= 5 ) :
print( Contador:  + contador ) 
contador = contador + 1 

print( Loop for: ) 
for ( i = 1 
i <= 5 
i = i + 1 ) :
print( i:  + i ) 

print( ===== TESTE DE FUNCOES MATEMATICAS ===== ) 
print( Fatorial de 5:  + fatorial ( 5 ) ) 
print( ===== TESTE DE NUMEROS PRIMOS ===== ) 
for ( i = 1 
i <= 20 
i = i + 1 ) :
if ( eh_primo ( i ) ) :
print( i +  e primo ) 

else :
print( i +  nao e primo ) 


print( ===== TESTE CONCLUIDO ===== ) 
print( Todos os testes foram executados com sucesso! ) 
return 0 

