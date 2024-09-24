import pandas as pd

class Carregador:

    def carregar_dados(url: str, atributos: list): 
        """ Cria um DataFrame à partir de um arquivo CSV
        Args:
            url: caminho completo do csv
            list: lista de atributos do csv
        Returns:
            Retorna um DataFrame contendo os dados do csv lido
        """

        return pd.read_csv(url, names=atributos, header=0,
                        skiprows=0, delimiter=',')