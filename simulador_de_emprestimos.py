#SIMULADOR DE EMPRESTIMOS

#Para realizar uma simulação de empréstimo no aplicativo é
#necessário primeiro informar se o usuário é cliente ou não da
#instituição financeira

#Caso o usuário não seja cliente do banco, deverá ser informado
#então o seu Serasa Score para selecionar qual será a taxa de juros
#do empréstimo.

#O Serasa Score é um modelo estatístico calculado com base em informações
#relevantes para a análise de risco de crédito, como dados cadastrais,
#histórico de consultas, dados negativos e positivos (caso possua o Cadastro
#Positivo ativo). É uma pontuação que vai de 0 a 1000 e indica as chances de
#o consumidor pagar suas contas em dia nos próximos 6 meses.

#Tabela Serasa Score e a taxa de juros
#Faixa de score: de 0 a 299 – taxa de juros: 20%
#Faixa de score: de 300 a 499 – taxa de juros: 15%
#Faixa de score: de 500 a 699 – taxa de juros: 10%
#Faixa de score: de 700 a 1000 – taxa de juros: 5%
#Clientes do banco terão 4% de taxa de juros

#O usuário deverá então informar o valor em reais do empréstimo, e
#em quantas parcelas ele deseja dividir

#Para cálculo do valor total a ser pago pelo empréstimo deve ser
#considerado:
#1 – Tarifa de cadastro de R$ 35,00 para não clientes
#2 – Taxa de juros de acordo com o perfil do solicitante
#3 – Imposto IOF de 0,38% sobre o valor do empréstimo
#O IOF (Imposto sobre Operações Financeiras) é um tributo federal
#pago por pessoas físicas e jurídicas nas operações de crédito,
#câmbio de moedas, contratos de seguro, aplicações em valores
#mobiliários, ativos de renda fixa e em alguns fundos de investimento

#O sistema deverá perguntar para o usuário se ele deseja incluir um Seguro
#Desemprego no pedido de empréstimo no valor 3,5%
#Em caso de desemprego, exceto justa causa, a instituição bancária cobre até 6
#parcelas do empréstimo.

#Após calcular os juros e demais encargos do empréstimo, o sistema
#deve apresentar para o usuário a quantidade de parcelas, o valor de
#cada parcela, a taxa de juros utilizada e o CET (Custo Efetivo Total).
#O CET reúne todos os gastos envolvidos na operação de empréstimo.
#São eles: juros, IOF, seguro, tributos, registros e demais despesas,
#que devem ser especificadas no contrato.

#Após apresentar o resultado da simulação o sistema deve perguntar
#ao usuário se ele deseja realizar outra simulação ou encerrar o
#programa.


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

            valor_parcelas = (valor_emprestimo * 0.04)
            cet = valor_emprestimo + valor_parcelas 

            print("--------------------------------------------------")
            print("Parcelas: {}\nValor das parcelas: {}\nTaxa de juros: 4% \nCusto Efetivo Total: {}" .format
            (parcelas, valor_parcelas, cet ))
            print("--------------------------------------------------")

        elif seguro_desemprego in {"s", "S"}:

            valor_parcelas = (valor_emprestimo * 0.035) * 0.04
            cet = valor_emprestimo + valor_parcelas + (valor_emprestimo * 0.038)
            print("--------------------------------------------------")
            print("Parcelas: {}\nValor das parcelas: {}\nTaxa de juros: 4% \nCusto Efetivo Total: {}" .format
            (parcelas, valor_parcelas, cet ))
            print("--------------------------------------------------")
            

    score = 0 

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

            valor_parcelas = (valor_emprestimo * 0.035) * 0.2
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

            valor_parcelas = (valor_emprestimo * 0.035) * 0.15
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

            valor_parcelas = (valor_emprestimo * 0.035) * 0.1
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

            valor_parcelas = (valor_emprestimo * 0.035) * 0.05
            print("--------------------------------------------------")
            print("Parcelas: {}\nValor das parcelas: {}\nTaxa de juros: 5% \nCusto Efetivo Total: {}" .format
            (parcelas, valor_parcelas, valor_emprestimo ))
            print("--------------------------------------------------")




mensagem_de_entrada()
inicio_do_programa()

                















                














