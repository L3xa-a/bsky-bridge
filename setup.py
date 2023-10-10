from setuptools import setup, find_packages

setup(
    name="bsky-bridge",
    version="1.0.0",
    description="A Python interface for interacting with the BlueSky social network's API.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="Axel Merlo",
    author_email="contact@axelm.fr",
    url="https://github.com/4xe1/bsky-bridge",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
