from fastapi import APIRouter, HTTPException, Depends
from dependencies import pegar_sessao
from sqlalchemy.orm import Session
from models import Pedido
from schemas import PedidoSchema

## ESSE é o meu prefixo do meu router, ou seja, todas as rotas que eu criar aqui dentro do auth_router vão começar com /pedidos
order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

## ESSE é o meu endpoint, ou seja, a rota completa para acessar essa função vai ser /pedidos/lista
@order_router.get("/")
async def pedidos():
    return {"message": "Voçe acessou a rota de pedidos"}


@order_router.post("/pedido")
async def criar_pedido(
    pedido_schema: PedidoSchema,
    session: Session = Depends(pegar_sessao)
):

    novo_pedido = Pedido(
        usuario_id = pedido_schema.usuario,
        valor_total = pedido_schema.valor_total
    )

    session.add(novo_pedido)
    session.commit()
    session.refresh(novo_pedido)

    return {"msg": f"Pedido criado com sucesso, ID: {novo_pedido.id}"}
