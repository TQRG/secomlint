from setuptools import setup

setup(
    name='secomlint',
    version='0.1.0',    
    description='A linter for security commit messages',
    url='https://github.com/tqrg/secomlint',
    author='Sofia Reis',
    author_email='sofiareis1994@gmail.com',
    packages=['secomlint'],
    install_requires=['spacy'],
    entry_points={
        'console_scripts': [
            'secomlint = secomlint.__main__:hello'
        ]
    },
)