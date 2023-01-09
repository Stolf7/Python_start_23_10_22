nome_produto = []
valor_compra = []
valor_venda = []
quantidade_estoque = []
quantidade_vendida = []
while True:
    def inicio():
        print('''
        [1] - Vender
        [2] - Cadastrar Produto
        [3] - Remover produto do estoque
        [4] - Consultar Estoque
        [5] - Consultar Lucro
        [6] - Repor estoque
        [0] - Sair
        ''')
    #def vender():
    def cadastrar_produto():
        print('Cadastre o produto...')
        nome_produto.append(input('Nome do produto: '))
        valor_compra.append(float(input('Valor de compra: ')))
        valor_venda.append(float(input('Valor de venda: ')))
        quantidade_estoque.append(int(input('Quantidade em estoque: ')))
        print('O item {}, com valor de R${}, que sera vendido por R${}, tendo em estoque {} peças, foi cadastrado com sucesso'.format(nome_produto, valor_compra, valor_venda, quantidade_estoque))
        inicio()
    inicio()
    user_entrada = int(input('O que você deseja?: '))

    #if user_entrada == 1:

    if user_entrada == 2:
        cadastrar_produto()

    #if user_entrada == 3:

    #if user_entrada == 4:

    #if user_entrada == 5:

    #if user_entrada == 6:

    #if user_entrada == 0:

    if user_entrada == 20:
        print(nome_produto)
        
        
