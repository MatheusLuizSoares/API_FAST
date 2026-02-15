from pydantic import BaseModel
from typing import Optional


class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: Optional[bool] = True
    admin: Optional[bool] = False

    class Config:
        from_attributes = True

class PedidoSchema(BaseModel):

    usuario: int
    valor_total: float

    class Config:
        from_attributes = True

class loginSchema(BaseModel):
    email: str
    senha: str

    class Config:
        from_attributes = True