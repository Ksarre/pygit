from setuptools import find_packages, setup

setup(
    name="pygit",
    version="1.0",
    packages=find_packages(),
    description="A personal learning cli tool that mimics git source control locally",
    entry_points={"console_scripts": ["pygit = base.cli:main"]},
    exclude=["test"],
)
