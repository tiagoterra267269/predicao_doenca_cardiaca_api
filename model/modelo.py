import joblib
import pickle

class Modelo:

    def carregar_modelo(fullpath):
        """ Carrega o modelo caso seja um arquivo válido (.pkl)
        Args:
            fullpath (_type_): nome do arquivo com seu caminho completo
        Raises:
            Exception: Ocorre quando o path for nulo
            Exception: Ocorrer quando formato de arqivo não encontrado
        Returns:
            _type_: retorna uma instância do modelo treinado carregado
        """
        if (fullpath is None): 
            raise Exception("Caminho inválido!")
        elif not (fullpath.endswith('.pkl')):
            raise Exception("Formato de arquivo não suportado!")

        return joblib.load(fullpath)

    def predizer(model, dadosdeentrada):
        """ Realixa ma predição de acordo com o modelo treinado  e os dados de entrada
        Returns:
            Retorna o resultado da predição 
        """
        return model.predict(dadosdeentrada)