from sklearn.preprocessing import PolynomialFeatures

class Transformer():
    def __init__(self):
        super().__init__()
    def initTransformer(self, degree, includebias):
        self.transformer = PolynomialFeatures(degree=degree, include_bias=includebias)
    def transform(self, x):
        self.transformer.fit(x)    
        x_ = self.transformer.transform(x)
        return x_    