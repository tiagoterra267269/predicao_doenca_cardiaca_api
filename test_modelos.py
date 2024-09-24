from model import Modelo
from machinelearning.modelo.carregador import Carregador
from machinelearning.modelo.avaliador import Avaliador
from machinelearning.modelo.pipeline import Pipeline
import pandas as pd
import joblib

modelo = Modelo()
carregador = Carregador()
avaliador = Avaliador()

# Parâmetros    
url_dados = "./MachineLearning/files/heart-disease.csv"
colunas = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal','target'] 

# Carga dos dados 
dataset = Carregador.carregar_dados(url_dados, colunas)

array = dataset.values
X = array[:,0:-1]
y = array[:,-1]

# Testar o modelo a partir do algotimo rescolhido
def test_modelo_svc():

    # Importando modelo de SVC
    svc_path = './modelo_doenca_cardiaca.pkl'
    modelo_svc = Modelo.carregar_modelo(svc_path)
    scaler = joblib.load('./scaler_doenca_cardiaca.pkl')
    rescaled_input = scaler.transform(X)

    # Obtendo as métricas do SVC
    acuracia_svc = Avaliador.avaliar(modelo_svc, rescaled_input, y)
    
    # Testando as métricas do SVC
    assert acuracia_svc >= 0.80