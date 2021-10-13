[![Build Status](https://github.com/fmaguire/laymansHGVS/actions/workflows/test_package.yml/badge.svg)](https://github.com/fmaguire/laymansHGVS/actions/workflows/test_package.yml)

# laymansHGVS
Program to take a [HGVS-nomenclature variant](https://varnomen.hgvs.org/) and create a laymans sentence explaining what is occurring

The grammar importing function relies heavily on the grammar.py module code created by [Mutalyzer](https://github.com/mutalyzer/mutalyzer)

## Installation 

This package requires [pyparsing](https://github.com/pyparsing/pyparsing) and can be installed using pip:

    git clone https://github.com/conmeehan/laymansHGVS
    pip install laymansHGVS

## Usage

This installs a simple command line script called `explain_HGVS` that takes a
single argument string containing a valid HGVS formatted variant and 
explains it.
    
    explain_HGVS --variant "Genome1(Gene1):c.25A>G"
    >>> This is a subst found in Genome1 at position 25 where the reference has a A and the sample has a G


