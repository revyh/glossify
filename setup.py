"""Setup script for Glossify."""

from setuptools import setup, find_packages

setup(
    name="glossify",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pymupdf>=1.19.0",
        "spacy>=3.1.0",
        "typer>=0.4.0",
        "pydantic>=1.9.0",
        "python-dotenv>=0.19.0",
    ],
    entry_points={
        "console_scripts": [
            "glossify=glossify.cli:main",
        ],
    },
    python_requires=">=3.8",
    description="PDF Translation Assistant",
    keywords="pdf, translation, language, cefr",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
)
