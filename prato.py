import sqlite3

class Prato:
    def __init__(self):
        self.conexao = self.criar_conexao()

    def criar_conexao(self):
        # Estabelecendo conexão e criando tabela
        conexao = sqlite3.connect("restaurante_db.db")
        consulta = conexao.cursor()
        tabela = """
        CREATE TABLE IF NOT EXISTS pratos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100),
        preco FLOAT,
        descricao VARCHAR(1000)
        );
        """
        consulta.execute(tabela)
        return conexao

    def cadastrarPrato(self, nome, preco, descricao):
        # Inserindo novo prato no banco de dados
        sql = "INSERT INTO pratos (nome, preco, descricao) VALUES (?, ?, ?)"
        campos = (nome, preco, descricao)
        consulta = self.conexao.cursor()
        consulta.execute(sql, campos)
        self.conexao.commit()
        print(consulta.rowcount, "Linha(s) inserida(s) com sucesso.")

    def consultarPratos(self):
        # Consultando todos os pratos
        sql = "SELECT * FROM pratos"
        consulta = self.conexao.cursor()
        consulta.execute(sql)
        resultado = consulta.fetchall()
        if resultado:
            for prato in resultado:
                print(f"ID: {prato[0]}")
                print(f"Nome: {prato[1]}")
                print(f"Preço: {prato[2]}")
                print(f"Descrição: {prato[3]}\n")
        else:
            print("Nenhum prato cadastrado.")

    def deletarPrato(self, id):
        # Deletando prato pelo ID
        sql = "DELETE FROM pratos WHERE id = ?"
        consulta = self.conexao.cursor()
        consulta.execute(sql, (id,))
        self.conexao.commit()
        if consulta.rowcount > 0:
            print(f"Prato com ID {id} excluído com sucesso.")
        else:
            print(f"Prato não encontrado.")

    def atualizarPrato(self, id, nome, preco, descricao):
        # Atualizando dados de um prato
        sql = "UPDATE pratos SET nome = ?, preco = ?, descricao = ? WHERE id = ?"
        campos = (nome,preco, descricao,id)
        consulta = self.conexao.cursor()
        consulta.execute(sql, campos)
        self.conexao.commit()
        if consulta.rowcount > 0:
            print(f"Prato com ID {id} atualizado com sucesso.")
        else:
            print(f"Prato não encontrado.")

    def consultarPratoIndividual(self, id):
        # Consultando um prato específico pelo ID
        sql = "SELECT * FROM pratos WHERE id = ?"
        consulta = self.conexao.cursor()
        consulta.execute(sql, (id,))
        resultado = consulta.fetchone()
        if resultado:
            print(f"ID: {resultado[0]}")
            print(f"Nome: {resultado[1]}")
            print(f"Preço: {resultado[2]}")
            print(f"Descrição: {resultado[3]}\n")
        else:
            print("Prato não encontrado.")

    def fechar_conexao(self):
        # Fechando a conexão ao final
        if self.conexao:
            self.conexao.close()
