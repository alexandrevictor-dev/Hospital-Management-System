import sys #importa biblioteca que mexe com o sistema operacional do PC
import mysql.connector # Importa o driver oficial do MySQL, 'traduz' do python para MySQL
from mysql.connector import pooling #importa especificamente o módulo para connection pool

class DatabaseManager: #Define classe do gerenciador do banco
    _pool = None #declara a variável para guardar a connection pool, o '_' serve para avisar que 
    #é uma variável privada, ninguém deve mexer nela de fora desse arquivo. Começa None porque ainda está vazia

    @classmethod
    def initialize_pool(cls, host='localhost', user='root', password='', database='hospital_management', pool_size=5):
        # Inicializa a connection pool uma única vez ao executar o programa
        if cls._pool is None:
            try:
                cls._pool = pooling.MySQLConnectionPool(
                    pool_name='hospital_pool',
                    pool_size=pool_size,
                    host=host,
                    user=user,
                    password=password,
                    database=database
                )
                print('[SUCESSO] Connection Pool foi inicializado.')
            except mysql.connector.Error as err:
                print(f'[ERRO] Falha crítica ao tentar conectar no banco de dados: {err}')
                print('Verifique se o MySQL está ligado no XAMPP')
                print('Certifique-se de que o banco de dados foi criado!')  
                sys.exit(1)  

    @classmethod
    def get_connection(cls):
        #Retira uma conexão ativa de dentro da connection pool
        if cls._pool is None:
            raise Exception('A connection pool não foi inicializada. Chame a initialize_pool() primeiro.')
        try:
            return cls._pool.get_connection()
        except mysql.connector.Error as err:
            print(f'[ERRO] Não foi possível obter uma conexão da pool: {err}')
            return None