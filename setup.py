from setuptools import setup, find_packages

setup(
    name='pipinit',
    version='1.0.0',
    description='npm init for Python',
    url='',
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
