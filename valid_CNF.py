#Algorithm to check whether a given CNF is valid (that is TRUE for all rows of the Truth Table)

#suppose there are n Clauses with max. m literals in each clause, then complexity will be O(n*(m^2))
def isValidCNF(phi):
	#assuming that phi is a list of clauses which are ANDed in expression
	for Ci in phi:
		if(not isValidDisClause(Ci)):
			#if atleast one of the Ci is not valid, then the phi is not valid
			return False
	return True

def isValidDisClause(C):	#suppose there are m literals in a Clause, then complexity will be O(m^2)
	#assuming that C is a list of Literals which are ORed in the expression
	for i in range(len(C)):
		Li = C[i]		#assuming Li is of the form !p  or  p
		Lj = 0
		if Li[0] == '!':
			Lj = Li[1:]
		else:
			Lj = '!'+Li
		for j in range(i+1,len(C)):
			if(C[j] == Lj):
				return True
	return False

def parse_phi(inStr):
	fai = []
	clauses = inStr.split('&')
	for c in clauses:
		clause = c.split('|')
		fai.append(clause)
	return fai

inp = input("Enter a CNF Expression: ")
inp = "".join(inp.split())	#to remove un-necessary white spaces in between
fai = parse_phi(inp)
print(fai)
print(isValidCNF(fai))
