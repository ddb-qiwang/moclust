import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="moclust",
    version="0.0.1",
    author="yuanmusu",
    author_email="yuanmusu@pku.edu.cn",
    description="A small example package",
    long_description=A deep learning-based clustering method for single-cell multi-omics data,
    long_description_content_type="text/markdown",
    url="https://github.com/ddb-qiwang/MoClust",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
    install_requires =[
        "scanpy >= 1.6.0",
        "numpy >= 1.21.6",
        "pandas >= 1.3.5",
        "torch == 1.10.2",
        "scikit-learn >= 1.0.2",
        "scipy >= 1.4.1",
        "seaborn >= 0.9.0",
        "tabulate == 0.8.9",
        "pydantic == 1.10.2",
        "typing >= 3.5.0",
)