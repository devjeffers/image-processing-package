from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="meu_primeiro_pacote",
    version="0.0.1",
    author="Jefferson",
    author_email="devsfull.jefferson@gmail.com",
    description="Pacote de testes da aula de criação de pacote de imagens com Python.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/devjeffers",
    packages=find_packages(),
    install_requires=requirements,
    python_requires =">=3.1"
)