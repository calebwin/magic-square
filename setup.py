import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="magic-square",
    version="0.0.1",
    author="Caleb Winston",
    author_email="calebhwin@gmail.com",
    description="A data structure for magic squares",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/calebwin/magic-square",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
