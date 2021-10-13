class ProteinLayman():
	"""
	Parses all version of the protein HGVS into a single sentence explanation
	NOTE: does not handle the following:
	alleles or multiple changes in one variant (e.g. p.[Ser44Arg;Trp46Arg])
	silent mutations (e.g. NP_003997.1:p.Cys188=)
	insertions that are only numbered or unknown and no amino acid listed (e.g. p.Arg78_Gly79ins23 or NP_003997.1:p.(Ser332_Ser333insX))
	repeats (e.g. p.Ala2[10])
	frameshifts (e.g. p.Arg97ProfsTer23)
	"""
	
	def __init__(self):
		"""
		Initialise the class and get the grammar dictionary
		"""
	#__init__
	
	@staticmethod
	def convertAAName(AA):
		"""
		Convert a 3 letter amino acid code into a full name amino acid
		
		@arg AA: The input 3 letter amino acid code
		@type variant: String
		
		@return: The full amino acid name
		@rtype: String
		"""
		AAconvert = {'ter': 'Stop codon', '*': 'Stop codon', 'ala': 'Alanine', 'arg': 'Arginine', 'asn': 'Asparagine', 'asp': 'Aspartate', 'cys': 'Cysteine', 'gln': 'Glutamine', 'glu': 'Glutamate', 'gly': 'Glycine', 'his': 'Histidine','ile': 'Isoleucine', 'leu': 'Leucine',  'lys': 'Lysine', 'met': 'Methionine', 'phe': 'Phenylalanine', 'pro': 'Proline', 'ser': 'Serine', 'thr': 'Threonine', 'trp': 'Tryptophan', 'tyr': 'Tyrosine', 'val':'Valine'}
		return (AAconvert[AA])
	#convertAAName
	
	def deletion(self,raw):
		"""
		Create the output for deletions
		
		@arg AA: the raw grammar for a deletion
		@type variant: Dictionary
		
		@return: The sentence explaining the deletion
		@rtype: String
		"""
		
		varName="deletion"
		
		AA1=self.convertAAName(raw['Args'][0].lower())
		
		if 'EndLoc' in raw:
			AA2=self.convertAAName(raw['Args'][1].lower())
			return (" a "+varName+" beginning at position "+raw['StartLoc'][1]+" where the reference has a "+AA1+" and finishing at position "+raw['EndLoc'][1]+" where the reference has a "+AA2)

		else:
			return (" a "+varName+" at position "+raw['Main']+" where the reference has a "+AA1)
	#deletion

	def insertion(self,raw):
		"""
		Create the output for insertions
		
		@arg AA: the raw grammar for a deletion
		@type variant: Dictionary
		
		@return: The sentence explaining the insertion
		@rtype: String
		"""
		
		varName="insertion"
		
		AA1=self.convertAAName(raw['Args'][0].lower())
		AA2=self.convertAAName(raw['Args'][1].lower())
		AA3=raw['Args'][2]
		insAAs=""
		for iAA in AA3:
			insAAs+=self.convertAAName(iAA.lower())+" "
		
		return (" an "+varName+" of "+insAAs+"beginning at position "+raw['StartLoc'][1]+" where the reference has a "+AA1+" and finishing at position "+raw['EndLoc'][1]+" where the reference has a "+AA2)
	#insertion
	
	def deletion_insertion(self,raw):
		"""
		Create the output for combined deletions and insertions
		
		@arg AA: the raw grammar for a combined deletions and insertions
		@type variant: Dictionary
		
		@return: The sentence explaining the combined deletions and insertions
		@rtype: String
		"""
		
		varName="combined deletion and insertion"
		
		AA1=self.convertAAName(raw['Args'][0].lower())
		if 'EndLoc' in raw:
			AA2=self.convertAAName(raw['Args'][1].lower())
			AA3=raw['Args'][2]
			insAAs=""
			for iAA in AA3:
				insAAs+=self.convertAAName(iAA.lower())+" "
			return (" an "+varName+" of "+insAAs+"replacing position "+raw['StartLoc'][1]+" where the reference has a "+AA1+" and finishing at position "+raw['EndLoc'][1]+" where the reference has a "+AA2)

		else:
			AA2=raw['Args'][1]
			insAAs=""
			for iAA in AA2:
				insAAs+=self.convertAAName(iAA.lower())+" "
				
			return (" an "+varName+" of "+insAAs+"replacing position "+raw['StartLoc'][1]+" where the reference has a "+AA1)
	
		
	#deletion_insertion
	
	
	def substitution(self,raw):
		"""
		Create the output for substitutions
		
		@arg AA: the raw grammar for a substitution
		@type variant: Dictionary
		
		@return: The sentence explaining the substitution
		@rtype: String
		"""
		
		varName="substitution"
		
		AA1=self.convertAAName(raw['Args'][0].lower())
		AA2=self.convertAAName(raw['Args'][1].lower())
		return (" a "+varName+" at position "+raw['Main']+" where the reference has a "+AA1+" and the sample has a "+AA2)
	#subst
	
	def interpret(self, variant):
		"""
		Parse the input dictionary into the various variant types and structure the sentence accordingly
		
		@arg variant: The input dictionary that needs to be parsed.
		@type variant: dictionary
		
		@return: The sentence explaining the variant
		@rtype: String
		
		"""
		
		output=""
		
		#Pull the variant apart into the protein details (name and accession) and the raw changes
		if 'LrgAcc' in variant:
			protName=variant['LrgAcc']+"."+variant['LRGProteinID']
			output+="In "+protName+" there is"
		elif 'RefSeqAcc' in variant:
			protName=variant['RefSeqAcc']+"."+variant['Version']
			output+="In "+protName+" there is"
		else:
			output+="There is"	
			
			
		raw=variant['RawVar']
		varType=raw['MutationType']
		
		if varType == 'subst':
			output+=(self.substitution(raw))
		elif varType == 'del':
			output+=(self.deletion(raw))
		elif varType == 'ins':
			output+=(self.insertion(raw))
		elif varType == 'delins':
			output+=(self.deletion_insertion(raw))	
		return(output)
		#return ("This is a type found in protein at position X where the reference has a Y and the sample has a Z")
	
	#parse
#Grammar