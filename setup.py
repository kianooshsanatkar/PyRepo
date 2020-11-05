import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyrepo",
    version="0.0.1",
    author="Kianoosh Sanatkar",
    author_email="kianoosh.personalblog@gmail.com",
    description="A simple repository",
    long_description="An implementation of repository pattern in python suitable for sqlAlchemy and MongoEngine implementation",
    url="https://github.com/kianooshsanatkar/pyrepo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
