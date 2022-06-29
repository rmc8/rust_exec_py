from typing import List
from setuptools import setup


def get_requires(**kwargs) -> List[str]:
    with open("./requirements.txt", **kwargs) as f:
        txt: str = f.read()
        return txt.splitlines()


# DOC: https://docs.python.org/ja/3/distutils/setupscript.html
setup(
    name="rsexec",
    version="2022.06.29",
    description="",
    author="rmc8",
    author_email="k@rmc-8.com",
    url="https://github.com/rmc8/py_template_repository",
    packages=["rsexec"],
    install_requires=get_requires(),
    entry_points={
        "console_scripts": [
            "rse = rsexec.__main__:main",
        ]
    }
)
