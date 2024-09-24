from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime

class ModeloViewSchema(BaseModel):
    """ Define o Modelo retornado
    """
    nome: str = "Modelo"

class ListagemModelosSchema(BaseModel):
    """ Define como uma listagem de Modelos será retornada.
    """
    Modelos:List[ModeloViewSchema]

def mapea_modelo(nome: str):
    """ 

    
    """
    return {
        "nome": nome
    }

    return {"modelo": result}