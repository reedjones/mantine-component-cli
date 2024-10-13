from setuptools import setup, find_packages

setup(
    name="mantine-component-cli",
    version="0.1.0",
    description="A CLI tool for managing mantine UI components with Typer and Rich",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Reed Jones",
    author_email="reed.jones@example.com",
    url="https://github.com/reedjones/mantine-component-cli",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "typer[all]",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "mantine-component-cli=mantine_ui:app",
        ],
    },
    classifiers=[        "Development Status :: 3 - Alpha",        "Intended Audience :: Developers",        "License :: OSI Approved :: MIT License",        "Programming Language :: Python :: 3",        "Programming Language :: Python :: 3.7",        "Programming Language :: Python :: 3.8",        "Programming Language :: Python :: 3.9",        "Programming Language :: Python :: 3.10",        "Operating System :: OS Independent",        "Topic :: Software Development :: Libraries :: Application Frameworks",        "Environment :: Console",    ],
    python_requires=">=3.7",
)