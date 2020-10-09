# Regress
Get up and running with regress

------------
 Install using pip

`pip install regress`

 Or, if you have using pip3
 
`pip3 install regress`


------------
### Usage 

Linear regression model

`from regress.linear_model import Linear`
`linearmodel = Linear()`

Polynomial regression model

`from regress.polynomial_model import Polynomial`
`linearmodel = Polynomial()`

Data preprocessing

`from regress.preprocess import preprocess`
`x = preprocess([1, 2, 3])`

Model statistics

`from regress.statistics import score, intercept, coef`
`print(score(linearmodel, x, y))`
`print(intercept(linearmodel)`
`print(coef(linearmodel))`

Transform

`from regress.transform import Transform`
`transformer = Transform()`
`tansformer.initTransformer(2, false)`
`x_ = transformer.transform(x)`

Predict

`from regress.prediction import Predict`
`print(Predict(linearmodel, val))`
 

------------


&copy; Rushan 2020