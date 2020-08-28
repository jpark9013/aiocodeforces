from setuptools import setup, find_packages

classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3"
]

setup(
    name="aiocodeforces",
    version="1.0.9",
    packages=find_packages(),
    author="Julian Park",
    author_email="jpark9013@gmail.com",
    description="An asyncio wrapper for the CodeForces API",
    url="https://github.com/jpark9013/aiocodeforces",
    license="MIT",
    keywords=["codeforces", "asyncio", "wrapper", "aiocodeforces"],
    install_requires=["aiohttp"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ]
)
