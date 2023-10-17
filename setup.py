from setuptools import setup, find_packages

import app

setup(
  name='my_test_package',
  version=app.__version__,
  author=app.__author__,
  url='https://databricks.com',
  author_email='john.doe@databricks.com',
  description='my test wheel',
  packages=find_packages(include=['app']),
  entry_points={
    'group_1': 'run=app.entrypoint:main'
  },
  install_requires=[
    'setuptools'
  ]
)