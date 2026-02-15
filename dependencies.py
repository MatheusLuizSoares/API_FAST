from models import db
from sqlalchemy.orm import sessionmaker

def pegar_sessao():
    Session = sessionmaker(bind=db)
    session = Session()
    yield session
    session.close()



##yield é uma palavra-chave do Python que é usada para criar um gerador. Um gerador é uma função que pode ser pausada e retomada, permitindo que você produza uma sequência de valores ao longo do tempo, em vez de calcular todos os valores de uma vez e armazená-los na memória. No contexto do FastAPI, o uso de yield em uma função de dependência permite que você crie um recurso (como uma sessão de banco de dados) que pode ser usado em várias rotas e, em seguida, seja limpo automaticamente quando não for mais necessário.