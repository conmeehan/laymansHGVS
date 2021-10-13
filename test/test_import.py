#!/usr/bin/env python

from laymansHGVS import laymansHGVS


if __name__ == "__main__":

    interpretation = laymansHGVS.interpret("Genome1(Gene1):c.25A>G")
    print(interpretation)

