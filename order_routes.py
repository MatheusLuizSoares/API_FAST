from fastapi import APIRouter, HTTPException, Depends
from dependencies import pegar_sessao, verificar_token
from sqlalchemy.orm import Session
from models import Pedido
from schemas import PedidoSchema

## ESSE é o meu prefixo do meu router, ou seja, todas as rotas que eu criar aqui dentro do auth_router vão começar com /pedidos
order_router = APIRouter(prefix="/pedidos", tags=["pedidos"], dependencies=[Depends(verificar_token)])

## ESSE é o meu endpoint, ou seja, a rota completa para acessar essa função vai ser /pedidos/lista
@order_router.get("/")
async def pedidos():
    return {"message": "Voçe acessou a rota de pedidos"}

## order_router.post("/pedido") é o endpoint para criar um novo pedido. Ele recebe um objeto do tipo PedidoSchema no corpo da requisição e uma sessão do banco de dados como dependência. A função cria um novo pedido usando os dados fornecidos, adiciona o pedido à sessão do banco de dados, comita a transação e retorna uma mensagem de sucesso com o ID do novo pedido.
@order_router.post("/pedido")
async def criar_pedido( pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):

    novo_pedido = Pedido( usuario_id = pedido_schema.usuario,valor_total = pedido_schema.valor_total )

    session.add(novo_pedido)
    session.commit()
    session.refresh(novo_pedido)

    return {"msg": f"Pedido criado com sucesso, ID: {novo_pedido.id}"}


@order_router.post("/pedido/cancelar/{id_pedido}")
async def cancelar_pedido(id_pedido: int, session: Session = Depends(pegar_sessao)):
    pedido = session.query(Pedido).filter(Pedido.id == id_pedido).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    pedido.status == "cancelado"
    session.commit()
    return {"msg": f"Pedido cancelado com sucesso, ID: {id_pedido}"}    
    