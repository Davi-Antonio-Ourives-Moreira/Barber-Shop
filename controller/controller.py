import flask
from service import FeedBack
from repository import Banco_Feeds

app = flask.Flask(__name__)

app.secret_key = "GeeksForGeeks"

@app.get("/")
def home():
    banco_feeds = Banco_Feeds()

    leitura_feeds = banco_feeds.Ver_Feeds()

    primeiro_feed = leitura_feeds.pop(0)

    return flask.render_template("index.html",
                                 pasta_imagens="static",
                                 imagem_logo="logo-barbearia2.png",
                                 imagem_tesoura="corte_cabelo.png",
                                 imagem_navalha="corte_barba.png",
                                 imagem_tesoura_navalha="combo.png",
                                 imagem_avatar_depoimentos="avatar.png",
                                 informacoes_primeiro_feed=primeiro_feed,
                                 informacoes_feeds_restantes=leitura_feeds
                                 )

@app.post("/feedback")
def feedback():
    nome = str(flask.request.form["input_nome_feedback"])
    email = str(flask.request.form["input_email_feedback"])
    mensagem = str(flask.request.form["input_mensagem_feedback"])

    feed = FeedBack(nome_feed=nome,
                    email_feed=email,
                    mensagem_feed=mensagem
                    )
    
    return feed.Analisar_Feedback()
