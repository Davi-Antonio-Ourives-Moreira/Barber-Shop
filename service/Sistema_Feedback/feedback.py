import flask
import re
from repository import Banco_Feeds
from Error import (
                   Todos_Campos_Nao_Preencidos, 
                   Campo_Nome_Nao_Preencido, 
                   Campo_Email_Nao_Preencido, 
                   Campo_Mensagem_Nao_Preencido, 
                   Campo_Nome_Email_Nao_Preencido, 
                   Campo_Email_Mensagem_Nao_Preencido,
                   Campo_Nome_Mensagem_Nao_Preencido
                   )

class FeedBack(object):
    def __init__(self, nome_feed, email_feed, mensagem_feed) -> None:
        self.input_nome_feed = nome_feed
        self.input_email_feed = email_feed
        self.input_mensagem_feed = mensagem_feed

        self.regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

        self.verificar_email = (lambda email: bool(re.search(self.regex, email)))

    def Analisar_Feedback(self):
        try:
            if self.input_nome_feed == "" and (self.input_email_feed == "" or self.verificar_email(self.input_email_feed) == False) and self.input_mensagem_feed == "":
                raise Todos_Campos_Nao_Preencidos
            
            elif self.input_nome_feed == "" and (self.input_email_feed == "" or self.verificar_email(self.input_email_feed) == False) and not self.input_mensagem_feed == "":
                raise Campo_Nome_Email_Nao_Preencido
            
            elif self.input_mensagem_feed == "" and (self.input_email_feed == "" or self.verificar_email(self.input_email_feed) == False) and not self.input_nome_feed == "":
                raise Campo_Email_Mensagem_Nao_Preencido
            
            elif self.input_nome_feed == "" and self.input_mensagem_feed == "" and (not self.input_email_feed == "" and self.verificar_email(self.input_email_feed) == True):
                raise Campo_Nome_Mensagem_Nao_Preencido

            elif self.input_nome_feed == "":
                raise Campo_Nome_Nao_Preencido

            elif self.input_email_feed == "" or self.verificar_email(self.input_email_feed) == False:
                raise Campo_Email_Nao_Preencido
            
            elif self.input_mensagem_feed == "":
                raise Campo_Mensagem_Nao_Preencido
        
        except Todos_Campos_Nao_Preencidos:
            return self.Informar_Erro("todos_campos_errados")
        
        except Campo_Nome_Email_Nao_Preencido:
            return self.Informar_Erro("campo_nome_email_errados")
        
        except Campo_Email_Mensagem_Nao_Preencido:
            return self.Informar_Erro("campo_email_mensagem_errados")
        
        except Campo_Nome_Mensagem_Nao_Preencido:
            return self.Informar_Erro("campo_nome_mensagem_errados")
        
        except Campo_Nome_Nao_Preencido:
            return self.Informar_Erro("nome_errado")
        
        except Campo_Email_Nao_Preencido:
            return self.Informar_Erro("email_errado")
        
        except Campo_Mensagem_Nao_Preencido:
            return self.Informar_Erro("mensagem_errada")
        
        else:
            # banco_feed = Banco_Feeds()

            # banco_feed.Adicionar_Feed(nome_pessoa=self.input_nome_feed,
            #                           email_pessoa=self.input_email_feed,
            #                           mensagem_pessoa=self.input_mensagem_feed
            #                           )

            return self.Avisar_Feedback_Corretamente()
            
        
    def Informar_Erro(self, tipo_erro):
        # informar erro
        flask.flash("erro")

        # informar tipo do erro
        flask.flash(tipo_erro)

        # passar os dados anteriores dos input
        flask.flash(self.input_nome_feed)
        flask.flash(self.input_email_feed)  
        flask.flash(self.input_mensagem_feed)

        return flask.redirect("/") 

    def Avisar_Feedback_Corretamente(self):
        flask.flash("todos_campos_corretamente")

        return flask.redirect("/")


