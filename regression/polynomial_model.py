import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

class Polynomial():
    def __init__(self):
        super().__init__(self)
    def initModel(self):
        self.model = LinearRegression(fit_intercept=False)
    def fit(self, x, y):
        self.model.fit(x, y)