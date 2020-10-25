from setuptools import setup, find_packages


setup(
    name="bib_merge",
    description="Merge bib files automatically.",
    author="Ziniu Li",
    author_email="liziniu1997@gmail.com",
    python_requires=">=3.6",
    license="MIT",
    install_requires=['bibtexparser'],
    packages=find_packages(
        exclude=["build", "dist", "*.egg-info"]
    ),
    entry_points={
        'console_scripts': ['bib-merge=bib_merge.scripts.cli:main'],
    }
)
