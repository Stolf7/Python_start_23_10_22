#ex - 1 – Faça um fluxograma para receber um digito. Se o digito for igual a “M” exiba “Masculino”; Senão, exiba “Feminino”

#digito_entrada = input("Digite M para masculino e F para feminino: ")

#if digito_entrada == "M" or "m":
#    print("Masculino")

#else:
#   print("Feminino")

#ex 2 – Faça um fluxograma para receber um número. Caso seja menor de 18 exiba a mensagem “Menor de idade”

#idade = int(input("Digite a sua idade: "))

#if idade < 18:
#    print("Menor de idade")
#else:
#    print("Maior de idade")

#ex 3   - Faça um fluxograma que receba um número e:
#Se o número for zero deve-se exibir a mensagem “Número nulo”;
#Se o número for menor que 0, deve-se exibir a mensagem “Número negativo”;

#numero = int(input("Digite um número: "))

#if numero == 0:
#    print("Numero nulo")

#if numero < 0:
#    print("Número negativo")

#ex 4 - Escreva um algoritmo (pseudocódigo) para calcular a área de um retângulo.
#fórmula A=b⋅h

#base =  float(input("Digite o valor da base do retangulo: "))
#altura = float(input("Digite o valor da altura do retangulo: "))

#area_retangulo = base * altura

#print("A área do retangulo é {}".format(area_retangulo))
  
#ex 5 - Escreva um algoritmo (pseudocódigo) que leia um número e exiba para o usuário o quadrado e a metade desse número.

#numero = float(input("Digite um número: "))

#quadrado = numero * numero
#metade = numero / 2

#print("O quadrado desse número é {}, e a metade dele é {}".format(quadrado, metade))

#ex 6 -  Escreva um algoritmo (pseudocódigo) que leia a idade de uma pessoa e calcule quantas horas essa pessoa viveu.

#idade = int(input("Digite sua idade: "))

#horas_vividas = (idade * 24) * 365

#print("Você viveu {} horas".format(horas_vividas))

#ex 7 - Escreva um algoritmo (pseudocódigo) para calcular a área de um trapézio.
#formula: A = (B + b).h / 2

#base_maior = float(input("Digite o valor da base maior: "))
#base_menor = float(input("Digite o valor da base menor: "))
#altura = float(input("Digite o valor da altura: "))

#area_trapezio = (base_maior + base_menor) * altura / 2

#print("A área do trapézio é {}" .format(area_trapezio))

#ex 8 -  Escreva um algoritmo que calcule 10% de um número fornecido pelo usuário.

#numero = float(input("Digite um número: "))

#dez_por_cento = numero * 0.10

#print("10 por cento desse número é {}".format(dez_por_cento))

#ex 9 - Escreva um algoritmo que calcule 5% e 50% de um número fornecido pelo usuário.

#numero = float(input("Digite um número: "))

#cinco_porcento = numero * 0.05
#dez_porcento = numero * 0.5

#print("Cinco por cento desse número é {} e cinquenta por cento é {}".format(cinco_porcento, dez_porcento))

#ex 10 - Escreva um algoritmo que receba o valor de um produto e mostre o valor com desconto de 7%.

#valor_produto = float(input("Digite o valor do produto: "))

#desconto = valor_produto - (valor_produto * 0.07) 

#print("O valor do produto com sete por cento de desconto é de R${}".format(desconto))

#ex 11 - Escreva um algoritmo que receba o valor de um produto e mostre o valor com acréscimo de 12%.

#valor_produto = float(input("Digite o valor do produto: "))

#acrescimo = valor_produto + (valor_produto * 0.12) 

#print("O valor do produto com sete por cento de desconto é de R${}".format(acrescimo))

#ex 12 - Escreva um algoritmo que calcule e apresente o volume de uma caixa retangular.
#formula V = 2 . h . l . c

#altura = float(input("Digite a altura: "))
#largura = float(input("Digite a largura: "))
#comprimento = float(input("Digite a comprimento: "))

#volume = (altura * 2) * largura * comprimento

#print("O volume da caixa retangular é de {} litros".format(volume))

#ex 13 - Escreva um algoritmo para ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula de
#conversão é F = (9 * C + 160) / 5, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

#celsius = float(input("Digite a temperatura em celsius: "))
#fahrenheit = (9 * celsius + 160) / 5

#Inicio do programa

#print("{} Celsius convertidos para Fahrenheit equivalem a {} fahrenheits".format(celsius, fahrenheit))

#ex 14 - Escreva um algoritmo que leia a velocidade de um objeto em Km/h e exiba para o usuário a velocidade em m/s (metros por segundo).

#velocidade = float(input("Digite o valor da velocidade em km/h: "))
#conversor = velocidade / 3.6

#print("{} km/h equivalem a {} m/s".format(velocidade, conversor))

#ex 15 - Escreva um algoritmo que leia dois números, calcule o quadrado de cada um, some os quadrados e mostre o resultado.

#numero1 = float(input("Digite o primeiro número: "))
#numero2 = float(input("Digite o segundo número: "))

#quadrado1 = numero1 * numero1
#quadrado2 = numero2 * numero2

#soma_dos_quadrados = quadrado1 + quadrado2

#print("O quadrado do número {} é {}, e o quadrado de {} é {} e a soma dos quadrados é {}" .format(numero1, quadrado1, numero2, quadrado2, soma_dos_quadrados))

#ex 16 - Escreva um algoritmo que leia três números, calcule a média simples e exiba para o usuário o resultado.

#numero1 = float(input("Digite o primeiro número: "))
#numero2 = float(input("Digite o segundo número: "))
#numero3 = float(input("Digite o terceiro número: "))

#media = (numero1 + numero2 + numero3) / 3

#print("A média dos números é {}" .format(media))



#----------------------------------
#ESTRUTURA DE CASO
#----------------------------------




#ex 17 - Escreva um algoritmo (fluxograma) que leia uma letra e:
#Se a letra for igual a “A” exiba “Azul”;
#Se a letra for igual a “V” exiba “Vermelho”;
#Se for qualquer outra letra exiba “Cor inválida”

#letra = input("Digite a letra [A/V]: ")

#if letra in {"a", "A"}:
#    print("Azul")
    
#if letra in ("v", "V"):
#    print("Vermelho")

#else:
#    print("Cor Inválida")

#ex 18 -  Escreva um algoritmo para ler um número. Se o número for menor que 100, deve-se exibir a mensagem “Número inválido!”.

#numero = float(input("Digite um número: "))

#if numero < 100:
#    print("Número Inválido")

#ex 19 - Escreva um algoritmo para receber um número. Se o número for maior que 100, deve-se exibir a mensagem “Número maior que
#100!”; caso contrário, exiba a mensagem “Programa encerrado”.

#numero = float(input("Digite um número: "))

#if numero > 100:
#    print("Número maior que 100!")
#else:
#    print(“Programa encerrado”)

#ex 20 - Escreva um algoritmo que leia dois números inteiros e exiba a multiplicação entre eles SE o primeiro número for menor que 10; caso
#contrário, exiba a soma dos números.

#numero1 = int(input("Digite o primeiro número: "))
#numero2 = int(input("Digite o segundo número: "))

#if numero1 < 10:
#    print("A multiplicação entre eles é {}" .format(numero1 * numero2))

#else:
#    print("A soma dos números é {}" .format(numero1 + numero2))

#ex 21 - Escreva um algoritmo para ler dois números e apresente a multiplicação deles apenas se o resultado for maior ou igual a 50.

#numero1 = int(input("Digite o primeiro número: "))
#numero2 = int(input("Digite o segundo número: "))

#resultado = numero1 * numero2

#if resultado >= 50:
#    print(resultado)

#else:
#    print("Programa encerrado")

#ex 22 - Escreva um algoritmo que receba um número e:
#- Se o número for zero deve-se exibir a mensagem “Número nulo”;
#- Se o número for menor que zero, deve-se exibir a mensagem “Número negativo”;
#- Se o número for maior que zero; deve-se exibir a mensagem “Número positivo”

#numero = int(input("Digite o número: "))

#if numero == 0:
#    print("Número nulo")

#if numero < 0:
#    print("Número negativo")

#if numero > 0:
#    print("Número positivo")

#ex 23 - Escreva um algoritmo que leia 3 notas de um aluno e calcule a média final considerando que a média é ponderada, ou seja, o peso
#das notas são 2, 3 e 5.

#nota1 = float(input("Digite a primeira nota: "))
#nota2 = float(input("Digite a segunda nota: "))
#nota3 = float(input("Digite a terceira nota: "))

#media_ponderada = (nota1 * 2 + nota2 * 3 + nota3 * 5) / (2 + 3 + 5)

#print("Media ponderada igual a {}" .format(media_ponderada))

#ex 24 - Escreva um algoritmo que receba de entrada a distância total (em km) percorrida por um automóvel e a quantidade de combustível
#(em litros) consumida para percorrê-la, calcule e imprima o consumo médio de combustível.

#distancia = float(input("Digite a distancia em km/h percorrida: "))
#gasolina = float(input("Digite o consumo de gasolina em litros: "))

#media = distancia / gasolina

#print("O consumo médio de gasolina foi de {} litros" .format(media))


#----------------------------------
#ESTRUTURA DE REPETIÇÃO
#----------------------------------


#ex 25 - Escreva um algoritmo que exiba na tela os números do 10 ao 20.

#for i in range(0, 10 + 1):
#    print(i)

#ex 26 - Escreva um algoritmo que exiba na tela os números pares do zero ao 10.

#for i in range(0 ,10 + 1, 2):
#    print(i)

#ex 27 - Escreva um algoritmo que exiba na tela os números 10 ao 1.

#for i in range(10 , 0, -1):
#    print(i)

#ex 28 - Escreva um algoritmo que receba um número e exiba na tela os números do zero até o número digitado pelo usuário.

#numero = int(input("Digite um número: "))

#for i in range(0 , numero + 1):
#    print(i)

#ex 29 - Escreva um algoritmo que receba dois números inteiros e armazene nas variáveis A e B. Calcule e apresente os resultados
#das quatros operações básicas utilizando essas variáveis

#a = int(input("Digite o número: "))
#b = int(input("Digite o número: "))

#print("A soma de A e B É {}" .format(a + b))
#print("A subtração de A e B É {}" .format(a - b))
#print("A multiplicação de A e B É {}" .format(a * b))
#print("A divisão de A e B É {}" .format(a / b))

#ex 30 - Escreva um algoritmo que receba 7 valores digitados pelo usuário e no final exiba o maior número.
#maior = 0
#for i in range(0, 7):
#    numero = int(input("Digite um número: "))
#    if numero > maior:
#        maior = numero
#print("O maior número é {}" .format(maior))

#ex 31 - Escreva um algoritmo que exiba na tela todos os números ímpares até o 49.

#numero = 49

#for i in range(0 , numero, 2):
#    i = i + 1
#    print(i)

#ex 32 - Escreva um algoritmo que verifique se uma letra digitada é vogal ou consoante.

#letra = input("Digite uma letra: ")

#if letra in {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}:
#    print("Vogal")

#else:
#    print("Consoante")

#ex 33 -  Escreva um algoritmo que receba um número inteiro e determine se ele e par ou ímpar. Dica: utilize o operador módulo (resto da
#divisão).

#numero = int(input("Digite um número: "))

#if numero % 2 == 1:
#    print("Impar")

#else:
#    print("Par")
