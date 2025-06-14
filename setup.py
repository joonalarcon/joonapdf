from setuptools import setup, find_packages
from pathlib import Path

# Leer README.md para la descripción larga
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="joonapdf",
    version="0.1.0",
    description="Convierte archivos .docx a PDF usando LibreOffice",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jonathan Alarcon",
    author_email="joona.palarconss@gmail.com",
    url="https://github.com/joonalarcon/joonapdf",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "joonapdf=joonapdf.cli:main",
        ],
    },
    install_requires=[],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

