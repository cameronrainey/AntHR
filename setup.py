from setuptools import setup, find_packages

__author__ = "Cameron Rainey"
__email__ = "cameron.s.rainey@gmail.com"




setup(
    name="anthr",
    version="development",
    description="Ant+ Hear Rate Logger",
    author=__author__,
    author_email=__email__,
    packages=find_packages(include=["anthr", "anthr.*"]),
    install_requires=[
        "black",
        "click",
    #    'ant @ git+https://github.com/cameronrainey/python-ant.git@0.1.1#egg=ant',
        'ant @ git+https://github.com/cameronrainey/openant.git@v0.4.1.1#egg=ant',
    ],
    entry_points= {
        "console_scripts": ["anthr=anthr.cli:cli"]
    },
    classifiers=[
        "Intended Audience :: Science/Research",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
    ],
)