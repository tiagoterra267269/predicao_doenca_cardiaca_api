from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from model.modelo import Modelo

class Avaliador:

    def avaliar(model, X_test, Y_test):
        """ Realiza uma avaliação (acurácia) do modelo
        Args:
            model: modelo a ser avaliado
            X_test: contém os dados de entrada do modelo
            Y_test: rótulo a ser utilizado na acurácia
        Returns:
            Retorna o valor de acurácia do modelo
        """

        predicoes = Modelo.predizer(model, X_test)

        return accuracy_score(Y_test, predicoes)