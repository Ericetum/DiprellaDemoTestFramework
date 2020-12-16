from setuptools import setup, find_packages


def get_dependencies():
    with open("dependencies.txt", "r") as deps:
        deps = tuple(map(lambda dep: dep.strip(), deps.readlines()))

    return deps


setup(
    name="Diprella Simple Testing Framework",
    version="1.0.0",
    author="Alla Chudakova",
    author_email="alliks1@gmail.com",
    packages=find_packages(),
    install_requires=get_dependencies()
)
