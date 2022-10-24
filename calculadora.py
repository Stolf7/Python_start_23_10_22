
operation = input("""
Escolha o operador desejado
+ for soma
- for subtracao
/ for divisao
* for multiplicacao
""")

x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

calcule = x + y
calcule1 = x * y 
calcule2 = x / y
calcule3 = x- y 

if operation == "+":
    print ("A soma é", calcule)

elif operation == "*":
    print ("A multiplicação é", calcule1)

elif operation == "/":
    print ("A divisão é", calcule2)
elif operation == "-":
    print ("A subtração é", calcule3)
else:
    print ("Numero invalido")