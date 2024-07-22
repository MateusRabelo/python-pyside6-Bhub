import sqlite3

class Database:
    def __init__(self, name = 'system.db') -> None:

        self.name = name


    # start database connection
    def connect(self):
        self.connection = sqlite3.connect(self.name) # conectando no banco de dados


    # close database connection
    def close_connection(self):
        try:
            self.connection.close() # fechando a conexão
        except:
            pass


    # create a new table in the database
    def create_table_company(self):
        cursor = self.connection.cursor()
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS Empresas(
                CNPJ TEXT,
                NOME TEXT,
                LOGRADOURO TEXT,
                NUMERO TEXT,
                COMPLEMENTO TEXT,
                BAIRRO TEXT,
                MUNICIPIO TEXT,
                UF TEXT,
                CEP TEXT,
                TELEFONE TEXT,
                EMAIL TEXT,

                PRIMARY KEY(CNPJ)   
            );
        """)

    
    # insert the data into the database
    def register_company(self, fullDataSet):
        campos_tabela = ('CNPJ', 'NOME', 'LOGRADOURO', 'NUMERO', 'COMPLEMENTO', 'BAIRRO', 'MUNICIPIO', 'UF', 'CEP', 'TELEFONE', 'EMAIL')
        qntd = ("?,?,?,?,?,?,?,?,?,?,?")

        cursor = self.connection.cursor()

        try:
            cursor.execute(f"""
                INSERT INTO Empresas {campos_tabela}
                VALUES({qntd})
            """, fullDataSet)

            self.connection.commit()

            return ('Ok')

        except:
            return 'Error'


    # select all companies from database
    def select_all_companies(self):
        try:
            cursor = self.connection.cursor()

            cursor.execute("SELECT * FROM Empresas ORDER BY NOME")
            empresas = cursor.fetchall()

            return empresas
        except:
            return 'Error'
        
    
    # delete a specify company
    def delete_company(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Empresas WHERE CNPJ = '{id}'")

            self.connection.commit()

            return "Dados deletados com sucesso!"
        except:
            return "Erro ao deletar dados!"
        

    # update a company data
    def update_company(self, fullDataSet):
        cursor = self.connection.cursor()

        # fullDataSet é uma lista, e os valores receberão os elementos do index desta lista fullDataSet
        cursor.execute(f"""UPDATE Empresas set
                       
                       CNPJ = '{fullDataSet[0]}',
                       NOME = '{fullDataSet[1]}',
                       LOGRADOURO = '{fullDataSet[2]}',
                       NUMERO = '{fullDataSet[3]}',
                       COMPLEMENTO = '{fullDataSet[4]}',
                       BAIRRO = '{fullDataSet[5]}',
                       MUNICIPIO = '{fullDataSet[6]}',
                       UF = '{fullDataSet[7]}',
                       CEP = '{fullDataSet[8]}',
                       TELEFONE = '{fullDataSet[9]}',
                       EMAIL = '{fullDataSet[10]}'

                       WHERE CNPJ = '{fullDataSet[0]}'
                       """)
        
        self.connection.commit()