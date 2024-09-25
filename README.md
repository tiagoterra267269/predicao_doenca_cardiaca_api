# Predição de Doença Cardíaca


## Descrição
Esta API realiza a predição da possibilidade de um paciente ter uma doença cardíaca com base em dados clínicos. O modelo de machine learning foi treinado utilizando informações sobre idade, sexo, tipo de dor no peito, pressão arterial, entre outros fatores. A API faz uso de algoritmos de aprendizado de máquina para fornecer uma predição rápida e precisa.

## Objetivo
Prever a chance de um paciente apresentar uma doença cardíaca, fornecendo informações úteis para auxiliar profissionais de saúde na tomada de decisões.

## Como usar

1. Clone o repositório:

  git clone [https://github.com/seu-usuario/nome-do-projeto.git](https://github.com/tiagoterra267269/predicao_doenca_cardiaca_api.git)

2. Instale as dependências: Certifique-se de ter o Python 3.7+ instalado. Para instalar as dependências do projeto, execute:

  pip install -r requirements.txt

3. Executar a API:

  python app.py

4. Você pode acessar o endpoint /predict por postman ou curl, e verificar via swagger.

## Como o modelo foi treinado
O modelo foi treinado com um conjunto de dados de aproximadamente 300 registros, com as seguintes features:

- **idade** (age)
- **sexo** (sex)
- **tipo de dor no peito** (cp)
- **pressão arterial em repouso** (trestbps)
- **colesterol** (col)
- **açúcar no sangue** (fbs)
- **eletrocardiograma em repouso** (restecg)
- **frequência cardíaca máxima** (thalach)
- **angina induzida por exercício** (exang)
- **depressão do segmento ST** (oldpeak)
- **inclinação do segmento ST** (slope)
- **número de vasos principais** (ca)
- **talassemia (thal)**
  
A melhor performance foi alcançada com o algoritmo SVM após otimização de hiperparâmetros.

## Como o modelo foi treinado
