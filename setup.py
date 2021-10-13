import setuptools
import re
from distutils.core import setup

with open('README.md') as fh:
    long_description = fh.read()

with open('laymansHGVS/__init__.py') as fh:
    info = fh.read()
    version = re.search('^__version__\s*=\s*"(.*)"',
                        info, re.M).group(1)

setup(
    name='laymansHGVS',
    packages=['laymansHGVS'],
    version=version,
    license="AGPLv3",
    description="Tool to convert HGVS variant strings into layman friendly "
                "descriptions",
    author='Conor Meehan',
    url="https://github.com/conmeehan/laymansHGVS",
    download_url=f"https://github.com/conmeehan/archive/v{version}.tar.gz",
    keywords=["Genomics", "Antimicrobial resistance", "Antibiotic",
              "Standardization", "Variant", "HGVS"],
    python_requires='>=3.5',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['pyparsing'],
    entry_points={
        'console_scripts': [
            'explain_HGVS = laymansHGVS.laymansHGVS:cli'
            ],
        },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
        ],
    zip_safe=True,
    )
