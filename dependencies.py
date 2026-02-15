from models import db
from sqlalchemy.orm import sessionmaker

def pegar_sessao():
  try:
    Session = sessionmaker(bind=db)
    session = Session()
    yield session
  finally:
    session.close()

##definir a função pegar_sessao, que é uma função de dependência do FastAPI. Essa função cria uma sessão do banco de dados usando o SQLAlchemy e a retorna para ser usada em outras partes do código. O uso de yield permite que a sessão seja criada e usada em várias rotas, e depois seja fechada automaticamente quando não for mais necessária.

##yield é uma palavra-chave do Python que é usada para criar um gerador. Um gerador é uma função que pode ser pausada e retomada, permitindo que você produza uma sequência de valores ao longo do tempo, em vez de calcular todos os valores de uma vez e armazená-los na memória. No contexto do FastAPI, o uso de yield em uma função de dependência permite que você crie um recurso (como uma sessão de banco de dados) que pode ser usado em várias rotas e, em seguida, seja limpo automaticamente quando não for mais necessário.