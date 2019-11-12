import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pysmile", # Replace with your own username
    version="0.0.1",
    author="Yaroslav Goncharov",
    author_email="maplegend@mail.ru",
    description="Pygame wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maplegend/pysmile",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)