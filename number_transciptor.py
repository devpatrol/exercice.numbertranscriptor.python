# -*- encoding : utf-8 -*-

## Pour l'implémentation du Number Transcriptor
## Par Brel_Re



_CHARACTERS_ = {
	'+': 'plus ',
	'-': 'minus ',
	'/': 'divided by ',
	'*': 'times ',
	'=': 'equal to ',
	'**': 'power ',
	')': None,
	'(': None,
	'.':'dot',
	}

_OPERATORS_ = {'+', '-', '/', '*', '=', '**', '.',}

below_20 = [
	'', 'one ', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven ', 'eight ', 'nine ',
	'ten ', 'eleven ', 'twelve ', 'thirteen ', 'fourteen ', 'fifteen ', 'sixteen ', 'seventeen ', 'eighteen ', 'nineteen '
]
tens = ['', '', 'twenty ', 'thirty ', 'fourty ', 'fifty ', 'sixty ', 'seventy ', 'eighty ', 'ninety ']
thousands = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'hextillion', 'heptillion', 'octillion', 'nonallion', 'décallion ']



def missing_operands(string:str="", i:int=None) -> bool:
	'''
		Check if an operator has both its operands and check if there isn't any misplaced dot in the mathematical expression
	'''
	if string[i] in _OPERATORS_:
		if string[i:i+2] == '**':
			if not(string[i-1].isdigit() and string[i+2].isdigit()) and not(string[i-1]==')' or string[i+2]=='('):
				raise SyntaxError(f"Missing operands for operator '**' at position {i}.")
		elif string[i-1:i+1] == '**':
			if not(string[i-2].isdigit() and string[i+1].isdigit()) and not(string[i-2]==')' or string[i+1]=='('):
				raise SyntaxError(f"Missing operands for operator '**' at position {i}.")
		elif string[i] == '.':
			if not(string[i-1].isdigit() and string[i+1].isdigit()):
				raise SyntaxError(f"Invalid dot use at position {i+1}.")
		else:
			if not(string[i-1].isdigit() and string[i+1].isdigit()) and not(string[i-1]==')' or string[i+1]=='('):
				raise SyntaxError(f"Missing operands for operator '{string[i]}' at position {i+1}.")

	return True



def well_formed(string:str="") -> dict:
	'''
		Check if a mathematical expression's syntax is good or not
	'''
	brackets, openings = {}, []

	for i in enumerate(string):
		if i[1] not in _CHARACTERS_ and not i[1].isdigit():
			raise ValueError(f"Unknown character '{i[1]}' at position {i[0]+1}.")
		else:
			if i[1]=='(' :
				openings.append(i)
			if i[1]==')':
				if not openings:
					raise SyntaxError(f"Bracket at position {i[0]+1} was not opened.")
				else:
					if openings[-1][0] + 1 == i[0]:
						raise SyntaxError(f"There's nothing between brackets at position {i[0]} and {i[0]+1}.")
					else:
						brackets[openings[-1][0]] = i[0]
						del openings[-1]
			if string[i[0]] in _OPERATORS_:
				missing_operands(string, i[0])

	if openings:
		raise SyntaxError(f"Bracket at position {openings[-1][0]+1} was not closed.")

	return brackets


def translate_fidelly(string:str="") -> str:
	"""
		Transform a given number from digits to words by replacing each digit to its word value
	"""
	result = ''
	for i in string:
		result += below_20[int(i)]
	return result
	
def translate_3_digit(number:str=0) -> str:
	"""
		Return the world equivalence of a number made of three digits
	"""
	number = int(number)%1000

	result = below_20[int(number/100)]
	if number>=100:
		if int(number/100)>1:
			result +='hundreds '
		else:
			result += 'hundred '
	else:
		pass

	number = number%100
	if number >= 20:
		result += tens[int(number/10)] + below_20[number%10]
	else:
		result += below_20[number]
	return result

def translate_float(string:str="") -> str:
	"""
		Transform a floating number given in digits to words
	"""
	dot = string.rindex('.')
	full = string[:dot]
	dec = string[dot+1:]

	return translate_int(full) + 'dot ' + translate_fidelly(dec)


def translate_int(string:str="") -> str:
	"""
		Transform an integer number given in digits to words
	"""

	div = [string[c-3:c] for c in range(len(string), 0, -3) if c-3 >= 0]	
	if len(string)%3 != 0:
		div.append(string[0:len(string)%3])
	div.reverse()
	#div = list(map(int, div))

	result = ''
	for i in range(len(div)):
		result += translate_3_digit(div[i]) + thousands[len(div)-i-1]
		if int(div[i]) > 1 and i < len(div)-1:
			result += 's '
		else:
			result += ' '
			
	return result+' '


def translate(string:str='') -> str:
	"""
		Translate recursevely the given mathematical string to a litteral expression
	"""
	result, j, i = "", 0, 0
	brackets = well_formed(string)
	
	while i < len(string):
		if string[i] == '(':
			result += translate(string[i+1:brackets[i]]) + ' ' 
			i = brackets[i]+1
			if i >= len(string):
				break
			if string[i-1] == ')' and string[i] == '(':
				result += 'factor of '
				result += translate(string[i+1:brackets[i]]) + ' '
				i = brackets[i]+1
			
			if string[i-1] == ')' and string[i].isdigit():
				result += 'factor of '

			if i >= len(string):
				break
		
		if string[i] in _OPERATORS_:
			if string[i:i+2] == '**':
				result += 'power '
				i += 2
			else:
				result += _CHARACTERS_[string[i]]
				i +=1
			if i >= len(string):
				break

		if string[i].isdigit():
			j = i
			while i+1 < len(string) and (string[i+1].isdigit() or string[i+1] == '.'):
				i += 1
				if i >= len(string):
					break
			if i >= len(string):
				break
			nb = string[j:i+1].count('.')
			if nb > 1:
				raise ValueError(f"The number beginning at {i+1} in not floating.")
			if nb == 1:
				result += translate_float(string[j:i+1])+' '
			else:
				result += translate_int(string[j:i+1])+' '
			i += 1
			if i >= len(string):
				break
			
			if string[i] == '(':
				result += 'factor of '

	return result.replace('  ', ' ')

print(translate(input("Plz, enter some random mathematical expression: ").replace(' ', '')))
