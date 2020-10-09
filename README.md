# regression
Get up and running with regression

------------
 Install using pip

`pip install regression`

 Or, if you have using pip3
 
`pip3 install regression`


------------
### Usage 

Linear regressionion model

`from regression.linear_model import Linear`
`linearmodel = Linear()`

Polynomial regressionion model

`from regression.polynomial_model import Polynomial`
`linearmodel = Polynomial()`

Data preprocessing

`from regression.preprocess import preprocess`
`x = preprocess([1, 2, 3])`

Model statistics

`from regression.statistics import score, intercept, coef`
`print(score(linearmodel, x, y))`
`print(intercept(linearmodel)`
`print(coef(linearmodel))`

Transform

`from regression.transform import Transform`
`transformer = Transform()`
`tansformer.initTransformer(2, false)`
`x_ = transformer.transform(x)`

Predict

`from regression.prediction import Predict`
`print(Predict(linearmodel, val))`
 

------------


&copy; Rushan 2020