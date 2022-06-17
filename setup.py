from setuptools import setup, find_namespace_packages

with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="crescent-ext-docstrings",
    version="0.1.0",
    description="A docstring parser for hikari-crescent.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    license="MPL-2.0",
    packages=["crescent.ext.docstrings"],
    include_package_data=True,
    install_requires=[
        'docstring-parser >= "0.14.1"',
        'hikari-crescent >= "0.2.0"',
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8"
        "Programming Language :: Python :: 3.9"
        "Programming Language :: Python :: 3.10"
    ],
)
