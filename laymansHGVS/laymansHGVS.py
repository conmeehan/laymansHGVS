#!/usr/bin/env python

from laymansHGVS.grammar import Grammar
from laymansHGVS.proteinlayman import ProteinLayman
import argparse

"""
Author: Conor Meehan

Script to take a HGVS variant and create a laymans sentence explaining what
is occurring

@arg variant: The HGVS formatted variant (ensure there are "" around the
variant. e.g. "p.(Glu125_Ala132delinsGlyLeuHisArgPheIleValLeu)")

@return: Laymans sentence

python laymansHGVS.py --variant HGVSvariant

"""

def interpret(variant):
    # Create a grammer object to parse the variant into its sections
    grammar = Grammar()
    # Obtain the parsed variant as a dictionary
    pd = grammar.parse(variant).asDict()

    if not pd:
        # Parsing went wrong.
        raise ValueError("Variant could not be parsed")


    # Based on the reference type, process it either as genomic or protein
    if pd['RefType'] == 'g' or pd['RefType'] == 'c':
        mut_type = pd['RawVar']['MutationType']
        acc = pd['RefSeqAcc']
        loc = pd['RawVar']['StartLoc']['PtLoc'][0]['Main']
        ref = pd['RawVar']['Arg1']
        alt = pd['RawVar']['Arg2']

        interpretation = f"This is a {mut_type} found in {acc} at position " \
                         f"{loc} where the reference has a {ref} and the " \
                         f"sample has a {alt}"

    elif pd['RefType'] == 'p':
        proteinInterpreter = ProteinLayman()
        interpretation = proteinInterpreter.interpret(pd)
    else:
        raise ValueError(f"Variant reference type not recognised: {pd['RefType']}")

    return interpretation


def cli():
    # parse the inputs
    parser = argparse.ArgumentParser(description="Script to take a HGVS "
                                                 "variant and create a "
                                                 "laymans sentence explaining "
                                                 "what is occurring")
    parser.add_argument('--variant', required=True,
                        help='The HGVS formatted variant')

    args = parser.parse_args()

    interpretation = interpret(args.variant)

    print(interpretation)


if __name__ == "__main__":
    main()
