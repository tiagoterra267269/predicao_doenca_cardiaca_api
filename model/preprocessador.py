import joblib
import pandas as pd

class PreProcessador:

    def preparar_entrada(predicaoSchema):
        """ Preparara os dados de acordo com o predicaoSchema (PredicaoViewSchema)

        Args:
            Objeto PredicaoViewSchema contendo as entradas

        Returns:
            Retorna o array de entrada a ser utilizado posteriormente para escala
        """
        data = {'age':  [predicaoSchema.age],
                'sex': [predicaoSchema.sex],
                'cp': [predicaoSchema.cp],
                'trestbps': [predicaoSchema.trestbps],
                'chol':  [predicaoSchema.chol],
                'fbs': [predicaoSchema.fbs],
                'restecg': [predicaoSchema.restecg],
                'thalach': [predicaoSchema.thalach],
                'exang':  [predicaoSchema.exang],
                'oldpeak': [predicaoSchema.oldpeak],
                'slope': [predicaoSchema.slope],
                'ca': [predicaoSchema.ca],
                'thal': [predicaoSchema.thal]
                }

        # constrói o DataFrame
        atributos = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
        
        entrada = pd.DataFrame(data, columns=atributos)

        array_entrada = entrada.values

        return array_entrada[:,0:13].astype(float)

    def preparar_form(form):
        """ Prepara os dados recebidos do front para serem usados no modelo. """

        X_input = np.array([form.age, 
                            form.sex, 
                            form.cp, 
                            form.trestbps, 
                            form.chol,
                            form.fbs, 
                            form.restecg, 
                            form.thalach,
                            form.exang,
                            form.oldpeak, 
                            form.slope, 
                            form.ca,
                            form.thal
                        ])

        # Faremos o reshape para que o modelo entenda que estamos passando
        X_input = X_input.reshape(1, -1)

        return X_input

    def reescalar_dados(X_entrada):
        """ Reescala os dados a serem processados. """

        # obtenção de dados e transação por scala
        scaler = joblib.load('./scaler_doenca_cardiaca.pkl')

        rescaledEntradaX = scaler.transform(X_entrada)

        return rescaledEntradaX
