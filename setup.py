from setuptools import setup, find_packages

classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3"
]

setup(
    name="aiocodeforces",
    version="1.0",
    package=find_packages(),
    author="Julian Park",
    author_email="jpark9013@gmail.com",
    description="An asyncio wrapper for the CodeForces API",
    keywords="asyncio wrapper codeforces api",
    url="https://github.com/jpark9013/aiocodeforces",
    license="MIT",
    install_requires=["aiohttp"]
)
