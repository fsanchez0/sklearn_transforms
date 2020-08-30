from sklearn.base import BaseEstimator, TransformerMixin


# Deben tener fit y transform
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos copia del dataframe 'X' de entrada
        data = X.copy()
        # Retornamos un nuevo dataframe de las columnas
        return data.drop(labels=self.columns, axis='columns')

   
class DropNa(BaseEstimator, TransformerMixin):
    def __init__(self):
        print("Instanciada!")

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primero copiamos el dataframe de datos de entrada 'X'
        data = X.copy()
        # Devolvemos un nuevo dataframe de datos sin los nulos
        return data.dropna()
