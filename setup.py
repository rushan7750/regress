from distutils.core import setup
desc = """
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


&copy; Rushan 2020"""
setup(
  name = 'regrex',         # How you named your package folder (MyLib)
  packages = ['regrex'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'regrex made easy with regrex !',   # Give a short description about your library
  long_description=desc,
  long_description_content_type='text/markdown',
  author = 'rushan7750',                   # Type in your name
  author_email = 'shanrsjmax@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/rushan7750/regress',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/rushan7750/regress/archive/0.1.tar.gz',    # I explain this later on
  keywords = ['regress', 'simple', 'regrex'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'skikit-learn',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)