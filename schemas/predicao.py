from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime

class PredicaoSchema(BaseModel):
    """ Define uma requisção de predição
    """
    age: float = 1
    sex: float = 1
    cp: float = 1
    trestbps: float = 1
    chol: float = 1
    fbs: float = 1
    restecg: float = 1
    thalach: float = 1
    exang: float = 1
    oldpeak: float = 1
    slope: float = 1
    ca: float = 1
    thal: float = 1

class PredicaoViewSchema(BaseModel):
    """ Define o Predicao retornado
    """
    nome: str = "Predicao"

# class ListagemPredicaosSchema(BaseModel):
#     """ Define como uma listagem de Predicao será retornada.
#     """
#     Predicaos:List[PredicaoViewSchema]

def mapea_predicao(nome: str):
    """ Mapeia para fins de retorno
    """
    return {
        "nome": nome
    }

    return {"modelo": result}