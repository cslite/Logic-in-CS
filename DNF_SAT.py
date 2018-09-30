#polynomial time algorithm for checking satisfiability of a DNF

def isSatisfiableDNF(phi):
	#assuming that phi is a list of clauses which are ORed in expression
	for Ci in phi:
		if(isSatisfiableConForm(Ci)):
			return True
	return False

def negate(p):		#this function will negate a given literal
	#assuming a literal is of the form !p  or  p
	if p[0] == '!':
		return p[1:]
	else:
		return '!' + p

def isSatisfiableConForm(C):
	#assuming that C is a list of Literals which are ANDed in the expression
	db = set()
	for Li in C:
		db.add(Li)
		if negate(Li) in db:
			return False
	return True

def parse_phi(inStr):
	fai = []
	clauses = inStr.split('|')
	for c in clauses:
		clause = c.split('&')
		fai.append(clause)
	return fai

inp = input("Enter a DNF Expression: ")
inp = "".join(inp.split())	#to remove un-necessary white spaces in between
fai = parse_phi(inp)
print(fai)
print(isSatisfiableDNF(fai))
