from alphabet import *

# Reverse returns its argument string reversed unicode characters left to right.
def Reverse(keyword):
	#cast the arabic keyword type to be a list.
	keyword_as_list = list(keyword)
	#address the first character and the final one to i , j respectively.
	i , j = 0 , len(keyword_as_list) - 1
	#stop when i reaches the middle of the list to gain less time complexity
	while i < (len(keyword_as_list)/2):
		#reverse the list endings respectively till reach the middle of the list
		keyword_as_list[i],keyword_as_list[j] = keyword_as_list[j],keyword_as_list[i]
		#increase i and decrease j by 1 
		i,j = i+1,j-1
	#rejoin keyword characters to be one string of characters
	keyword_as_list = str(''.join(keyword_as_list))
	return keyword_as_list


# SmartLength returns the length of the given string
# without considering the Arabic Vowels (Tashkeel).
def SmartLength(keyword):
	# len() use int as return value, so we'd better follow for compatibility

	r = list(keyword)
	l=[]
	for i in range(len(r)):
		if r[i] in tashkeel_list:
			continue	
		else:
			l.append(r[i])
	return len(l)


# RemoveTashkeel returns its argument as string without Arabic vowels (Tashkeel).
def RemoveTashkeel(keyword) :
	r = list(keyword)
	
	l=[]
	for i in range(len(r)):
		
		if r[i] in tashkeel_list:
			continue	
		else:
			l.append(r[i])
	return "".join(l)


# RemoveTatweel returns its argument as rune-wise string without Arabic Tatweel character.
def RemoveTatweel(s) :
	r = list(s)
	l=[]
	for i in range (len(r)) :
		if TATWEEL.unicodee in r[i]:
			continue
		else:
			l.append(r[i])

	return "".join(l)

# getHarf gets the correspondent Harf for the given Arabic char
def getHarf(char) :
	for s in alphabet :
		if s.equals(char) :
			return s

	return Harf(unicodee= char, isolated= char, medium= char, final= char)

def getCharGlyph(previousChar, currentChar, nextChar ):
	glyph      = currentChar
	previousIn = False     # in the Arabic Alphabet or not
	nextIn     = False     # in the Arabic Alphabet or not

	for s in alphabet :
		if s.equals(previousChar) : # previousChar in the Arabic Alphabet ?
			previousIn = True
		
		if s.equals(nextChar) : # nextChar in the Arabic Alphabet ?
			nextIn = True
		
	for s in alphabet :

		if not s.equals(currentChar):  # currentChar in the Arabic Alphabet ?
			continue

		if previousIn and nextIn : # between two Arabic Alphabet, return the medium glyph
			for s in beggining_after :
				if s.equals(previousChar) :
					return getHarf(currentChar).beggining
			
			return getHarf(currentChar).medium
		
		if nextIn : # beginning (because the previous is not in the Arabic Alphabet)
			return getHarf(currentChar).beggining
		
		if previousIn : # final (because the next is not in the Arabic Alphabet)
			for s in  beggining_after :
				if s.equals(previousChar) :
					return getHarf(currentChar).isolated
				
			return getHarf(currentChar).final
		
		if not previousIn and not nextIn :
			return getHarf(currentChar).isolated
		
	return glyph


# ToGlyph returns the glyph representation of the given text
def ToGlyph(text ) :

	runes   = list(text)
	length  = len(runes)
	newText = []

	for i in range(length):
		current = runes[i]
		# get the previous char
		if (i - 1) < 0 :
			prev = 0
		else:
			prev = runes[i-1]

		# get the next char
		if (i + 1) <= length-1 :
			next = runes[i+1]
		else:
			next = 0

		# get the current char representation or return the same if unnecessary
		glyph = getCharGlyph(prev, current, next)

		# append the new char representation to the newText
		newText.append(glyph)

	return "".join(newText)

#RemoveAllNonAlphabetChars deletes all characters which are not included in Arabic Alphabet
def RemoveAllNonArabicChars(text ) :
	text_aslist = list(text)
	newText=[]
	
	for i in range(len(text_aslist)) :
		for s in alphabet:
			if text_aslist[i] == s.unicodee :
				newText.append(text_aslist[i])
		
	return "".join(newText)


