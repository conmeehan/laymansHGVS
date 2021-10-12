#! /usr/bin/env python
from parsers.grammar import Grammar
from parsers.proteinlayman import ProteinLayman
import argparse

"""
Author: Conor Meehan

Script to take a HGVS variant and create a laymans sentence explaining what is occurring

@arg variant: The HGVS formatted variant (ensure there are "" around the variant. e.g. "p.(Glu125_Ala132delinsGlyLeuHisArgPheIleValLeu)")
		
@return: Laymans sentence

python laymansHGVS.py --variant HGVSvariant

"""	

#parse the inputs
parser = argparse.ArgumentParser(description= 'Script to take a HGVS variant and create a laymans sentence explaining what is occurring')
parser.add_argument('--variant', required=True, help='The HGVS formatted variant')

args = parser.parse_args()

#Create a grammer object to parse the variant into its sections
grammar = Grammar()
#Obtain the parsed variant as a dictionary
pd = grammar.parse(args.variant).asDict()


#Based on the reference type, process it either as genomic or protein
if pd['RefType']=='g' or pd['RefType']=='c':
	print("This is a "+pd['RawVar']['MutationType']+" found in "+pd['RefSeqAcc']+" at position "+pd['RawVar']['StartLoc']['PtLoc'][0]['Main']+" where the reference has a "+pd['RawVar']['Arg1']+" and the sample has a "+pd['RawVar']['Arg2'])
elif pd['RefType']=='p':
	proteinInterpreter = ProteinLayman()
	interpretation = proteinInterpreter.interpret(pd)
	print(interpretation)
else:
	print("Variant reference type not recognised: "+pd['RefType'])
	
if not pd:
	# Parsing went wrong.
	print("error with parsing")
	
	