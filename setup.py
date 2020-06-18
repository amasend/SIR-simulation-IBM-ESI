import setuptools


with open('VERSION.txt', 'r') as f:
    version = f.read()

with open("README.md", "r") as fh:
    long_description = fh.read()

PROJECT_URLS = {
    'Source Code': 'https://github.com/amasend/SIR-simulation-IBM-ESI'
}

setuptools.setup(
    name="sir-simulation",
    version=version,
    author="Piotr Bator",
    author_email="piotr.bator@zse.krakow.pl",
    description="Virus simulation with dashboard base on SIR model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'plotly==4.8.1',
        'dash==1.12.0',
        'pandas==1.0.3',
        'requests==2.23.0',
        'sphinx==3.0.3'
    ],
    url="https://github.com/amasend/SIR-simulation-IBM-ESI",
    packages=setuptools.find_packages(exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8"
)
