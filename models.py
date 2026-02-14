from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float,ForeignKey
from sqlalchemy.orm import  declarative_base
# cria a conexão com o banco de dados, nesse caso, um banco de dados SQLite chamado "banco.db"
db = create_engine("sqlite:///banco.db")

# cria a base para as classes de modelo, que serão usadas para definir as tabelas do banco de dados
Base = declarative_base()
# criar as classes/tabelas do banco 
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key=True, index=True)
    nome = Column("nome", String, index=True)
    email = Column("email", String, unique=True, index=True, nullable=False)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean, default=True)
    admin = Column("admin", Boolean, default=False)

#usuario
#pedido
#itenspedido
                  