import numpy as np
from sklearn.linear_model import LinearRegression

class Linear():
    def __init__(self):
        super().__init__()
    def initModel(self):
        self.model = LinearRegression()
    def fit(self, x, y):
        self.model.fit(x, y)
        
