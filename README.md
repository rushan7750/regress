# regrex
Get up and running with regrex

------------
 Install using pip

`pip install regrex`

 Or, if you have using pip3
 
`pip3 install regrex`


------------
### Usage 

Linear regrex model

`from regrex.linear_model import Linear`
`linearmodel = Linear()`

Polynomial regrex model

`from regrex.polynomial_model import Polynomial`
`linearmodel = Polynomial()`

Data preprocessing

`from regrex.preprocess import preprocess`
`x = preprocess([1, 2, 3])`

Model statistics

`from regrex.statistics import score, intercept, coef`
`print(score(linearmodel, x, y))`
`print(intercept(linearmodel)`
`print(coef(linearmodel))`

Transform

`from regrex.transform import Transform`
`transformer = Transform()`
`tansformer.initTransformer(2, false)`
`x_ = transformer.transform(x)`

Predict

`from regrex.prediction import Predict`
`print(Predict(linearmodel, val))`
 

------------


&copy; Rushan 2020