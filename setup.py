from distutils.core import setup
setup(
  name = 'regrex',         # How you named your package folder (MyLib)
  packages = ['regrex'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'regrex made easy with regrex !',   # Give a short description about your library
  long_description=str(open('README.md', 'r').read()),
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