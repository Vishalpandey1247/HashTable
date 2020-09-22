from setuptools import setup

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name = 'hash-table',
    version = '0.0.4',
    author="Vishal Pandey",
    author_email="vp85623@gmail.com",
    description = "this package is used to store data in numbers hash table.", 
    url="https://github.com/Vishalpandey1247/HashTable",
    long_description_content_type="text/markdown",
    py_modules = ['HashTable'],
    package_dir = {'': 'src'},
    install_requires=[], 
    extras_require = {
       "dev":[
       "pytest>=3.7",
       ]
    },
    classifiers=[
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: MIT License",
       "Natural Language :: English",
       "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)