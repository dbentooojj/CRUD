# crir um banco de daados que vai ter 3 tbelas:
# -uma com os dados dos clientes: id, nome, idade, cpf, endereco, cep, numero
# -outra com os dados dos produtos: id, nome, familia, codigo_produto
# -outra com os dados das vendas: data_venda, codigo_produto, cpf_cliente, quntidade, valor unitario, valor_total

import sqlite3
import requests

conexao = sqlite3.connect('Controle1.db')
cursor = conexao.cursor()


class Cliente:
    def __init__(self, nome, idade, cpf, cep, numero):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.cep = cep
        self.numero = numero

    def Cadastrar_Cliente(self):
        self.cep = cep
        url = 'https://viacep.com.br/ws/%s/json/' % cep
        response = requests.get(url)
        response_json = response.json()
        cursor.execute('INSERT INTO Clientes (nome, idade, cpf, cep, rua, estado, cidade, bairro, numero) VALUES (?, '
                       '?, ?, ?, ?, ?, ?, ?, ?)',
                       (self.nome, self.idade, self.cpf, self.cep, response_json['logradouro'], response_json['uf'],
                        response_json['localidade'], response_json['bairro'], self.numero))
        conexao.commit()
        print('Cliente cadastrado com sucesso!')

    def Alterar_Cliente(self):
        while True:
            cpf = int(input('Digite o CPF do cliente que deseja alterar: '))
            break

        cursor.execute('SELECT * FROM Clientes WHERE cpf = ?', (cpf,))
        linha = cursor.fetchone()
        if linha is None:
            print('Cliente não encontrado!')
        else:
            print(f'{linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8]}')
            print('-' * 50)
            while True:
                print('Digite o campo que deseja alterar:')
                print('''
                1 - Nome
                2 - Idade
                3 - CPF
                4 - CEP
                5 - Numero
                6 - Todas as informações
                ''')
                op = int(input('Digite a opção desejada: '))
                if op == 1:
                    nome = input('Digite o novo nome: ')
                    cursor.execute('UPDATE Clientes SET nome = ? WHERE cpf = ?', (nome, cpf))
                    conexao.commit()
                    print('Nome alterado com sucesso!')
                    break
                elif op == 2:
                    idade = input('Digite a nova idade: ')
                    cursor.execute('UPDATE Clientes SET idade = ? WHERE id = ?', (idade, cpf))
                    conexao.commit()
                    print('Idade alterada com sucesso!')
                    break
                elif op == 3:
                    cpf = input('Digite o novo CPF: ')
                    cursor.execute('UPDATE Clientes SET cpf = ? WHERE id = ?', (cpf, cpf))
                    conexao.commit()
                    print('CPF alterado com sucesso!')
                    break
                elif op == 4:
                    cep = input('Digite o novo CEP: ')
                    cursor.execute('UPDATE Clientes SET cep = ? WHERE id = ?', (cep, cpf))
                    conexao.commit()
                    print('CEP alterado com sucesso!')
                    break
                elif op == 5:
                    numero = input('Digite o novo número: ')
                    cursor.execute('UPDATE Clientes SET numero = ? WHERE id = ?', (numero, cpf))
                    conexao.commit()
                    print('Número alterado com sucesso!')
                    break
                elif op == 6:
                    nome = input('Digite o novo nome: ')
                    idade = input('Digite a nova idade: ')
                    cpf = input('Digite o novo CPF: ')
                    cep = input('Digite o novo CEP: ')
                    numero = input('Digite o novo número: ')
                    cursor.execute('UPDATE Clientes SET nome = ?, idade = ?, cpf = ?, cep = ?, numero = ? WHERE id = ?',
                                   (nome, idade, cpf, cep, numero, cpf))
                    conexao.commit()
                    print('Informações alteradas com sucesso!')
                    break
                else:
                    print('Opção inválida!')
                    break

    def Listar_Clientes(self):
        if cursor.execute('SELECT * FROM Clientes').fetchone() is None:
            print('Não há clientes cadastrados!')
        else:
            cursor.execute('SELECT * FROM Clientes')
            for linha in cursor.fetchall():
                print(f'{linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8]}')

    def Excluir_Cliente(self):
        while True:
            cpf = int(input('Digite o CPF do cliente que deseja excluir: '))
            break

        cursor.execute('SELECT * FROM Clientes WHERE cpf = ?', (cpf,))
        linha = cursor.fetchone()
        if linha is None:
            print('Cliente não encontrado!')
        else:
            cursor.execute('DELETE FROM Clientes WHERE cpf = ?', (cpf,))
            conexao.commit()
            print('Cliente excluído com sucesso!')


class Produto:
    def __init__(self, nome_produto, familia_produto, codigo):
        self.nome_produto = nome_produto
        self.familia_produto = familia_produto
        self.codigo = codigo

    def Cadastrar_Produto(self):
        cursor.execute('INSERT INTO Produtos(nome_produto, familia_produto, codigo) VALUES(?, ?, ?)',
                       (self.nome_produto, self.familia_produto, self.codigo))
        conexao.commit()
        print('Produto cadastrado com sucesso!')

    def Alterar_Produto(self):
        while True:
            codigo = int(input('Digite o código do produto que deseja alterar: '))
            break

        cursor.execute('SELECT * FROM Produtos WHERE codigo = ?', (codigo,))
        linha = cursor.fetchone()
        if linha is None:
            print('Produto não encontrado!')
        else:
            print(f'{linha[0], linha[1], linha[2]}')
            print('-' * 50)
            while True:
                print('Digite o campo que deseja alterar:')
                print('''
                1 - Nome do produto
                2 - Família do produto
                3 - Código do produto
                4 - Todas as informações
                ''')
                op = int(input('Digite a opção desejada: '))

                if op == 1:
                    nome_produto = input('Digite o novo nome do produto: ')
                    cursor.execute('UPDATE Produtos SET nome_produto = ? WHERE codigo = ?',
                                   (nome_produto, codigo))
                    conexao.commit()
                    print('Nome do produto alterado com sucesso!')
                    break

                elif op == 2:
                    familia_produto = input('Digite a nova família do produto: ')
                    cursor.execute('UPDATE Produtos SET familia_produto = ? WHERE codigo = ?',
                                   (familia_produto, codigo))
                    conexao.commit()
                    print('Família do produto alterado com sucesso!')
                    break

                elif op == 3:
                    codigo = input('Digite o novo código de barras: ')
                    cursor.execute('UPDATE Produtos SET codigo WHERE codigo = ?',
                                   (codigo, codigo))
                    conexao.commit()
                    print('Código de barras alterado com sucesso!')
                    break

                elif op == 4:
                    nome_produto = input('Digite o novo nome do produto: ')
                    familia_produto = input('Digite a nova família do produto: ')
                    codigo = input('Digite o novo código do  : ')
                    cursor.execute(
                        'UPDATE Produtos SET nome_produto = ?, familia_produto = ?, codigo = ? WHERE codigo = ?',
                        (nome_produto, familia_produto, codigo, codigo))
                    conexao.commit()
                    print('Informações alteradas com sucesso!')
                    break

                else:
                    print('Opção inválida!')

    def Listar_Produtos(self):
        cursor.execute('SELECT * FROM Produtos')
        for linha in cursor.fetchall():
            print(f'{linha[0], linha[1], linha[2], linha[3]}')

    def Excluir_Produto(self):
        while True:
            codigo = int(input('Digite o código de barras do produto que deseja excluir: '))
            break

        cursor.execute('SELECT * FROM Produtos WHERE codigo = ?', (codigo,))
        linha = cursor.fetchall()
        if linha is None:
            print('Produto não encontrado!')
        else:
            cursor.execute('DELETE FROM Produtos WHERE codigo = ?', (codigo,))
            conexao.commit()
            print('Produto excluído com sucesso!')


class Venda:
    def __init__(self, data_venda, codigo_barras, cpf, quantidade, valor_unitario, valor_total):
        self.data_venda = data_venda
        self.codigo_barras = codigo_barras
        self.cpf = cpf
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.valor_total = valor_total

    def Cadastrar_Venda(self):
        cursor.execute('INSERT INTO Vendas(data_venda, codigo_barras, cpf, quantidade, valor_unitario, '
                       'valor_total) VALUES(?, ?, ?, ?, ?, ?)', (self.data_venda, self.codigo_barras,
                                                                 self.cpf, self.quantidade,
                                                                 self.valor_unitario, self.valor_total))
        conexao.commit()
        print('Venda cadastrada com sucesso!')

    def AlterarVenda(self):
        while True:
            codigo_barras = int(input('Digite o codigo barras da venda que deseja alterar: '))
            break

        cursor.execute('SELECT * FROM Vendas WHERE codigo_barras = ?', (codigo_barras,))
        linha = cursor.fetchone()
        if linha is None:
            print('Venda não encontrada!')
        else:
            print(f'{linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6]}')
            print('-' * 50)
            while True:
                print('Digite o campo que deseja alterar:')
                print('''
                1 - Data da venda
                2 - Código de barras
                3 - CPF do cliente
                4 - Quantidade
                5 - Valor unitário
                6 - Valor total
                ''')
                op = int(input('Digite a opção desejada: '))

                if op == 1:
                    data_venda = input('Digite a nova data da venda: ')
                    cursor.execute('UPDATE Vendas SET data_venda = ? WHERE codigo_barras = ?',
                                   (data_venda, codigo_barras))
                    conexao.commit()
                    print('Data da venda alterada com sucesso!')
                    break

                elif op == 2:
                    codigo_barra = input('Digite o novo código de barras: ')
                    cursor.execute('UPDATE Vendas SET codigo_barras = ? WHERE codigo_barras = ?',
                                   (codigo_barra, codigo_barras))
                    conexao.commit()
                    print('Código de barras alterado com sucesso!')
                    break

                elif op == 3:
                    cpf = input('Digite o novo CPF do cliente: ')
                    cursor.execute('UPDATE Vendas SET cpf = ? WHERE codigo_barras = ?',
                                   (cpf, codigo_barras))
                    conexao.commit()
                    print('CPF do cliente alterado com sucesso!')
                    break

                elif op == 4:
                    quantidade = int(input('Digite a nova quantidade: '))
                    cursor.execute('UPDATE Vendas SET quantidade = ? WHERE codigo_barras = ?', (quantidade, codigo_barras))
                    conexao.commit()
                    print('Quantidade alterada com sucesso!')
                    break

                elif op == 5:
                    valor_unitario = float(input('Digite o novo valor unitário: '))
                    cursor.execute('UPDATE Vendas SET valor_unitario = ? WHERE codigo_barras = ?', (valor_unitario, codigo_barras))
                    conexao.commit()
                    print('Valor unitário alterado com sucesso!')
                    break

                elif op == 6:
                    valor_total = float(input('Digite o novo valor total: '))
                    cursor.execute('UPDATE Vendas SET valor_total = ? WHERE codigo_barras = ?', (valor_total, codigo_barras))
                    conexao.commit()
                    print('Valor total alterado com sucesso!')
                    break

                else:
                    print('Opção inválida!')

    def Listar_Vendas(self):
        cursor.execute('SELECT * FROM Vendas')
        linhas = cursor.fetchall()
        if linhas is None:
            print('Não há vendas cadastradas!')
        else:
            for linha in linhas:
                print(f'{linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6]}')

    def Excluir_Venda(self):
        while True:
            codigo_barras = int(input('Digite o código de barras da venda que deseja excluir: '))
            break
        cursor.execute('SELECT * FROM Vendas WHERE codigo_barras = ?', (codigo_barras,))
        linha = cursor.fetchone()
        if linha is None:
            print('Venda não encontrada!')
        else:
            print(f'{linha[0], linha[1], linha[2], linha[3], linha[4], linha[5]}')
            print('-' * 50)
            while True:
                op = input('Deseja realmente excluir esta venda? (S/N): ')
                if op.upper() == 'S':
                    cursor.execute('DELETE FROM Vendas WHERE codigo_barras = ?', (codigo_barras,))
                    conexao.commit()
                    print('Venda excluída com sucesso!')
                    break
                elif op.upper() == 'N':
                    break
                else:
                    print('Opção inválida!')
                    break


while True:
    print('-' * 50)
    print('''
    1   - Cadastrar cliente 
    2   - Alterar cliente 
    3   - Excluir cliente 
    4   - Cadastrar produto 
    5   - Alterar produto 
    6   - Excluir produto 
    7   - Cadastrar venda 
    8   - Alterar venda 
    9   - Excluir venda 
    10  - Listar clientes 
    11  - Listar produtos 
    12  - Listar vendas 
    13  - Sair do programa 
    ''')
    print('-' * 50)

    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        nome = input('Digite o nome do cliente: ')
        idade = int(input('Digite a idade do cliente: '))
        cpf = int(input('Digite o cpf do cliente: '))
        cep = input('Digite o cep do cliente: ')
        numero = int(input('Digite o numero do cliente: '))
        cliente = Cliente(nome, idade, cpf, cep, numero)
        cliente.Cadastrar_Cliente()

    elif opcao == 2:
        cliente = Cliente('', '', '', '', '')
        cliente.Alterar_Cliente()

    elif opcao == 3:
        cliente = Cliente('', '', '', '', '')
        cliente.Excluir_Cliente()

    elif opcao == 4:
        nome_produto = input('Digite o nome do produto: ')
        familia_produto = input('Digite a familia do produto: ')
        codigo_barras = (input('Digite o codigo de barras do produto: '))
        produto = Produto(nome_produto, familia_produto, codigo_barras)
        produto.Cadastrar_Produto()

    elif opcao == 5:
        produto = Produto('', '', '')
        produto.Alterar_Produto()

    elif opcao == 6:
        produto = Produto('', '', '')
        produto.Excluir_Produto()

    elif opcao == 7:
        data_venda = input('Digite a data da venda: ')
        codigo_barras = int(input('Digite o codigo do produto: '))
        cpf = input('Digite o cpf do cliente: ')
        quntidade = int(input('Digite a quantidade do produto: '))
        valor_unitario = float(input('Digite o valor unitario do produto: '))
        valor_total = float(input('Digite o valor total do produto: '))
        venda = Venda(data_venda, codigo_barras, cpf, quntidade, valor_unitario, valor_total)
        venda.Cadastrar_Venda()

    elif opcao == 8:
        venda = Venda('', '', '', '', '', '')
        venda.AlterarVenda()

    elif opcao == 9:
        venda = Venda('', '', '', '', '', '')
        venda.Excluir_Venda()

    elif opcao == 10:
        cliente = Cliente('', '', '', '', '')
        cliente.Listar_Clientes()

    elif opcao == 11:
        produto = Produto('', '', '')
        produto.Listar_Produtos()

    elif opcao == 12:
        venda = Venda('', '', '', '', '', '')
        venda.Listar_Vendas()

    elif opcao == 13:
        print('Saindo do sistema...')
        break

    else:
        print('Opção inválida!')
