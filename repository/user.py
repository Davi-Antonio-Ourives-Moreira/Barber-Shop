import psycopg2 as ps

class Banco_Feeds(object):
    def __init__(self) -> None:
        self.user = "postgres"
        self.password = "postgres"
        self.host = "localhost"
        self.dbname = "Barbearia"
        self.port = 5432

        self.conectar = ps.connect(user=self.user,
                                   password=self.password,
                                   host=self.host,
                                   dbname=self.dbname,
                                   port=self.port)
        
        self.cursor = self.conectar.cursor()

    def Adicionar_Feed(self, nome_pessoa, email_pessoa, mensagem_pessoa):
        self.cursor.execute("INSERT INTO feedbacks(nome_pessoa_feed, email_pessoa_feed, mensagem_pessoa_feed) VALUES(%s,%s,%s)", (nome_pessoa, email_pessoa, mensagem_pessoa))

        self.conectar.commit()
    
    def Ver_Feeds(self):
        self.cursor.execute("SELECT * FROM feedbacks")

        feeds = list(self.cursor.fetchall())

        return feeds