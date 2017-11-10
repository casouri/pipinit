from setuptools import setup, find_packages

setup(
    name='pipinit',
    version='1.0.2',
    description='npm init for Python',
    long_description='''# pipinit
npm init for python

# install

```pip install pipinit```

# Usage

```$ pipinit
$ Name of the project(project):
$ Current version(1.0.0):
$ Short description:
$ URL:
$ Author:
$ Author email:
$ License(MIT):
$ Python requires(>=3):
```
    ''',
    url='https://github.com/casouri/pipinit',
    author='Yuan Fu',
    author_email='yuan.k.fu@gmail.com',
    license='MIT',
    py_modules=['__init__'],
    packages=find_packages(),
    python_requires='>=3',
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pipinit=__init__:cli
        ''')
