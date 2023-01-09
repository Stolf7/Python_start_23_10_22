parcelas = float
valor_parcelas = float
score = 0

def mensagem_de_entrada():

    print("----------------------------------")
    print("   Seja bem vindo(a) ao MyBank    ")
    print("    SIMULADOR DE EMPRESTIMOS     ")
    print("----------------------------------")


def inicio_do_programa():

    cadastro = input("Você já é nosso cliente? [s/n]: ")
    if cadastro in {"S", "s"}:

        valor_emprestimo = float(input("Digite o valor em reais emprestimo desejado: "))
        parcelas = float(input("Digite a quantidade de parcelas: "))
        
        seguro_desemprego = input("Deseja incluir um seguro desemprego no seu emprestimo? [s/n]: ")

        if seguro_desemprego in {"n", "N"}:

            valor_parcelas = (valor_emprestimo * 0.4)
            print("Parcelas: {}\nValor das parcelas: {}\nTaxa de juros: 4% \nCusto Efetivo Total: {}" .format
            (parcelas, valor_parcelas, valor_emprestimo ))

        elif seguro_desemprego in {"s", "S"}:

            valor_parcelas = (valor_emprestimo * 0.038) * 0.04
            print("--------------------------------------------------")
            print("Parcelas: {}\nValor das parcelas: {}\nTaxa de juros: 4% \nCusto Efetivo Total: {}" .format
            (parcelas, valor_parcelas, valor_emprestimo ))
            print("--------------------------------------------------")
            

   
    
    if cadastro in {"N", "n"}:
        score = float(input("Você não possui cadastro!\nDigite seu Serasa Score de 0 - 1000:  "))


    if (score >= 0) or (score <= 299): 

        valor_emprestimo = float(input("Digite o valor em reais emprestimo desejado: "))
        valor_emprestimo = valor_emprestimo + 35
        parcelas = float(input("Digite a quantidade de parcelas: "))

        seguro_desemprego = input("Deseja incluir um seguro desemprego no seu emprestimo? [s/n]: ")

        if seguro_desemprego in {"n", "N"}:

            valor_parcelas = (valor_emprestimo * 0.2) 
            print("--------------------------------------------------")
            print("Parcelas: {}\nValor das parcelas: {}\nTaxa de juros: 20% \nCusto Efetivo Total: {}" .format
            (parcelas, valor_parcelas, valor_emprestimo ))
            print("--------------------------------------------------")

        elif seguro_desemprego in {"s", "S"}:

            valor_parcelas = (valor_emprestimo * 0.038) * 0.2
            print("--------------------------------------------------")
            print("Parcelas: {}\nValor das parcelas: {}\nTaxa de juros: 20% \nCusto Efetivo Total: {}" .format
            (parcelas, valor_parcelas, valor_emprestimo ))
            print("--------------------------------------------------")


    elif (score >= 300) or (score <= 499): 
        valor_emprestimo = float(input("Digite o valor em reais emprestimo desejado: "))
        valor_emprestimo = valor_emprestimo + 35
        parcelas = float(input("Digite a quantidade de parcelas: "))
        
        seguro_desemprego = input("Deseja incluir um seguro desemprego no seu emprestimo? [s/n]: ")
        
        if seguro_desemprego in {"n", "N"}:

            valor_parcelas = (valor_emprestimo * 0.15) 
            print("--------------------------------------------------")
            print("Parcelas: {}\nValor das parcelas: {}\nTaxa de juros: 15% \nCusto Efetivo Total: {}" .format
            (parcelas, valor_parcelas, valor_emprestimo ))
            print("--------------------------------------------------")

        elif seguro_desemprego in {"s", "S"}:

            valor_parcelas = (valor_emprestimo * 0.038) * 0.15
            print("--------------------------------------------------")
            print("Parcelas: {}\nValor das parcelas: {}\nTaxa de juros: 15% \nCusto Efetivo Total: {}" .format
            (parcelas, valor_parcelas, valor_emprestimo ))
            print("--------------------------------------------------")

    elif (score >= 500) or (score <= 699): 
        valor_emprestimo = float(input("Digite o valor em reais emprestimo desejado: "))
        valor_emprestimo = valor_emprestimo + 35
        parcelas = float(input("Digite a quantidade de parcelas: "))

        seguro_desemprego = input("Deseja incluir um seguro desemprego no seu emprestimo? [s/n]: ")

        if seguro_desemprego in {"n", "N"}:

            valor_parcelas = (valor_emprestimo * 0.1)
            print("--------------------------------------------------")
            print("Parcelas: {}\nValor das parcelas: {}\nTaxa de juros: 10% \nCusto Efetivo Total: {}" .format
            (parcelas, valor_parcelas, valor_emprestimo ))
            print("--------------------------------------------------")

        elif seguro_desemprego in {"s", "S"}:

            valor_parcelas = (valor_emprestimo * 0.038) * 0.1
            print("--------------------------------------------------")
            print("Parcelas: {}\nValor das parcelas: {}\nTaxa de juros: 10% \nCusto Efetivo Total: {}" .format
            (parcelas, valor_parcelas, valor_emprestimo ))
            print("--------------------------------------------------")

    elif (score >= 700) or (score <= 1000): 
        valor_emprestimo = float(input("Digite o valor em reais emprestimo desejado: "))
        valor_emprestimo = valor_emprestimo + 35
        parcelas = float(input("Digite a quantidade de parcelas: "))

        seguro_desemprego = input("Deseja incluir um seguro desemprego no seu emprestimo? [s/n]: ")

        if seguro_desemprego in {"n", "N"}:

            valor_parcelas = (valor_emprestimo * 0.05) 
            print("--------------------------------------------------")
            print("Parcelas: {}\nValor das parcelas: {}\nTaxa de juros: 5% \nCusto Efetivo Total: {}" .format
            (parcelas, valor_parcelas, valor_emprestimo ))
            print("--------------------------------------------------")

        elif seguro_desemprego in {"s", "S"}:

            valor_parcelas = (valor_emprestimo * 0.038) * 0.05
            print("--------------------------------------------------")
            print("Parcelas: {}\nValor das parcelas: {}\nTaxa de juros: 5% \nCusto Efetivo Total: {}" .format
            (parcelas, valor_parcelas, valor_emprestimo ))
            print("--------------------------------------------------")



mensagem_de_entrada()
inicio_do_programa()

                














