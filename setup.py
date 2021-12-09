import os

import setuptools
from setuptools import setup

# Get version and release info, which is all stored in shablona/version.py

ver_file = os.path.join('StockNLP', 'version.py')

with open(ver_file) as f:
        
   v = exec(f.read())


# Give setuptools a hint to complain if it's too old a version

# 24.2.0 added the python_requires option

# Should match pyproject.toml

# SETUP_REQUIRES = ['setuptools >= 24.2.0']
#
# # This enables setuptools to install wheel on-the-fly
#
# SETUP_REQUIRES += ['wheel'] if 'bdist_wheel' in sys.argv else []


setup(name='StockNLP', version=1.0,
     description='Stock prediction based on sentiment analysis',
     description_content_type='text/markdown; \
                               charset=UTF-8; variant=GFM',
     long_description=open('README.md', 'r').read(),
     long_description_content_type='text/markdown; \
                                    charset=UTF-8; variant=GFM',
     url='https://github.com/StockNLP/StockNLP',
     license='Apache',
     author='Yash Patel, Moses Prasad Varghese, Aditya Challa, Nelson, Samartha Ramkumar',
     python_requires="~=3.9",
     install_requires=[
         "alpha-vantage==2.3.1"
         "numpy==1.21.4",
         "pandas==1.3.4",
         "keras==2.7.0", 
         "tensorflow==2.7.0",
         "scikit-learn==0.23.1",
         "keras-tuner==1.0.1",
         "plotly==5.4.0",
         "pyyaml==6.0",
         "scipy==1.7.3",
         "nltk==3.6.5"
         "decorator==5.1.0"
         "psaw==0.1.0"
         "streamlit==1.2.0"
         "tabulate==0.8.9"
         "tweepy==4.4.0"
         "vader==0.0.3"
         "yfinance==0.1.67"
         "requests==2.26.0"
       ],
       packages=setuptools.find_packages())

classifiers = ("Programming Language :: Python :: 3",
               "License :: OSI Approved :: Apache License",
               "Operating System :: OS Independent")
