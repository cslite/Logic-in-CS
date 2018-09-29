#CHECKING A STRING FOR MATCHING BRACKETS

brdb = {'[':']',
		'{':'}',
		'(':')',
		'<':'>'}

def match(s):
	stack = []
	for c in s:
		if c in ['{','(','[','<']:
			stack.append(c)
		elif c in ['}',')',']','>']:
			if len(stack) == 0 or brdb[stack[-1]] != c:
				return False
			else:
				stack.pop()
		# print(stack)
	if len(stack) == 0:		return True
	else:					return False

s = input("Enter a String: ")
if(match(s)):	print("Brackets match!")
else:			print("Brackets don't match!")
