import os
import re
import numpy
import joblib
import logging
import jsonify
import pandas as pd
from flask_cors import CORS
from datetime import datetime
from urllib.parse import unquote
from typing import Optional, List
from flask import redirect, request
from datetime import datetime, timedelta
from flask_openapi3 import OpenAPI, Info, Tag
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import Normalizer
from model import Modelo
from model import PreProcessador
from schemas.modelo import ListagemModelosSchema, ModeloViewSchema, \
    mapea_modelo
from schemas.error import ErrorSchema
from schemas.predicao import PredicaoSchema, PredicaoViewSchema, \
    mapea_predicao

# ========================================================================================================
# Configura log
# ========================================================================================================
logging.basicConfig(filename='modelo.log', encoding='utf-8', level=logging.DEBUG)

# ========================================================================================================
# Predição API
# ========================================================================================================
info = Info(title="Modelo de Predição API", version="1.0.0",
    description="")
app = OpenAPI(__name__, info=info)

CORS(app)

# ========================================================================================================
# Cria uma pasta para armazenar o arquivo de modelo
# ========================================================================================================
UPLOAD_DESTINO = 'uploads'
app.config['UPLOAD_DESTINO'] = UPLOAD_DESTINO
if not os.path.exists(UPLOAD_DESTINO):
    os.makedirs(UPLOAD_DESTINO)

# ========================================================================================================
# Tags
# ========================================================================================================
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")

modelo_tag = Tag(name="Modelo", description="""Endpoints para predição de modelo""")

# ========================================================================================================
# Endpoints
# ========================================================================================================
@app.post('/upload', tags=[modelo_tag], responses={"200": ModeloViewSchema, "409": 
    ErrorSchema, "400": ErrorSchema})
def upload_file():
    """  Faz o upload do arquivo de modelo: o arquivo será sobreescrito sempre que o endpoint
        for acionado
    """    
    try:

        if 'file' not in request.files:
            return jsonify({"error" : "Nenhum arquivo foi enviado"}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({"error": "Nenhum arquivo foi selecionado"}), 400
        
        # Caminho completo onde o arquivo será salvo
        file_path = os.path.join(app.config['UPLOAD_DESTINO'], 'modelo_doenca_cardiaca.pkl')
    
        # Salva o arquivo, sobrescrevendo se já existir
        file.save(file_path)

        return mapea_modelo(file.filename) , 200

    except IntegrityError as e:
        logging.warning(e)
        error_msg = "usuario de mesmo nome já salvo na base :/"
        return {"message": error_msg}, 409
    except Exception as e:
        logging.warning(e)
        error_msg = "Não foi possível salvar novo item :/"
        return {"message": error_msg}, 400

@app.post('/predizer', tags=[modelo_tag], responses={"200": PredicaoViewSchema, "409": 
    ErrorSchema, "400": ErrorSchema})
def predizer(form: PredicaoSchema):
    """ 
        Realiza a predição de acordo com os paraâmetros informados
    """    
    try:
        # Checa existência do modelo
        if not os.path.exists(app.config['UPLOAD_DESTINO'] + '/' + 'modelo_doenca_cardiaca.pkl'):
            return {"message": "Não há um modelo carregado, faça o upload do modelo para executar a predição!"}, 400

        # load do modelo  
        modelo = Modelo.carregar_modelo(app.config['UPLOAD_DESTINO'] + '/' + 'modelo_doenca_cardiaca.pkl')

        # prepara o array de entrada
        X_entrada = PreProcessador.preparar_entrada(form)

        # reescala os dados para predição
        rescaledEntradaX = PreProcessador.reescalar_dados(X_entrada)

        # predição do modelo
        saida = Modelo.predizer(modelo, rescaledEntradaX)

        # mapeamento
        return mapea_predicao(saida[0]), 200

    except IntegrityError as e:
        logging.warning(e)
        error_msg = "usuario de mesmo nome já salvo na base :/"
        return {"message": error_msg}, 409
    except Exception as e:
        logging.warning(e)
        error_msg = "Não foi possível salvar novo item :/"
        return {"message": error_msg}, 400