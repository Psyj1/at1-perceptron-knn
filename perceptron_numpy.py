import numpy as np

class PerceptronNumPy:
    def __init__(self, pesos, bias):
        # Converte as listas de entrada em arrays NumPy do tipo float
        self.pesos = np.array(pesos, dtype=float)
        self.bias = float(bias)

    def predict_single(self, entradas):
        """
        Realiza a predição para uma única amostra.
        """
        entradas_arr = np.array(entradas, dtype=float)

        # Produto escalar vetorizado
        z = np.dot(entradas_arr, self.pesos) + self.bias

        # Função degrau simples
        return 1 if z >= 0 else 0

    