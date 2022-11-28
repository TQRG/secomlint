from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='secomlint',
    version='0.1.1',    
    description='A linter for security commit messages',
    url='https://github.com/tqrg/secomlint',
    author='Sofia Reis',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email='sofiareis1994@gmail.com',
    license='MIT',
    packages=['secomlint'],
    include_package_data=True,
    package_data={'secomlint': ['entities/patterns.jsonl', 'config/rules.yml']},
    install_requires=[
        'spacy',
        'pandas',
        'pyyaml'
],
    entry_points={
        'console_scripts': [
            'secomlint = secomlint.__main__:main'
        ]
    },
)