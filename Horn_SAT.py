
def horn_SAT(phi):
	# assuming that we have a list of horn clauses
	toMark = '1'
	while(True):
		last_toMark = toMark
		for Ci in phi:	#iterating through the horn clauses
			#each horn clause is of the form [[p1,p2,p3...pn],q]
			allOnes = True
			for i in range(len(Ci[0])):
				if Ci[0][i] == toMark:
					Ci[0][i] = '1'
				elif Ci[0][i] != '1':
					allOnes = False
			if allOnes == True and Ci[1] != '1':
				Ci[0] = '1'
				if Ci[1] == '0':
					return False
				else:
					toMark = Ci[1]
					Ci[1] = '1'
					break
		if toMark == last_toMark:
			break
	return True

def parse_phi(hf):
	fai = []
	for hc in hf:
		clause = [0,0]
		if '->' in hc:
			# p1&p2...&pn -> q form
			tmp_hc = hc.split('->')
			clause[1] = tmp_hc[-1]
			clause[0] = tmp_hc[0].split('&')
			fai.append(clause)
		else:
			if hc[0] != '!' and '&' not in hc:
				fai.append([['1'],hc])
			elif hc[0] == '!':
				#assuming that it is of the type !(p1&p2&...pn) , so it becomes p1&p2...&pn -> 0
        #though ( ) are assumed, but they are not allowed.
				fai.append([hc[1:].split('&'),'0'])
	return fai

def pprint(phi):
	for hc in phi:
		print(hc[0][0],end=' ')
		for Li in hc[0][1:]:
			print('&',Li,end = ' ')
		print('->',hc[1])


print("Input HORN Formula (one horn clause per line) [end with -1]")
hf = []
while(True):
	ip = input()
	ip = "".join(ip.split())
	if ip == '-1':
		break
	else:
		hf.append(ip)
phi = parse_phi(hf)
pprint(phi)
print('Horn Satisfiable:',horn_SAT(phi))
