def removePun(word):
	c = ",.?!;:"
	new_list = list(word)

	for count in range(0,len(word)):
		for countt in range(0,len(c)):
			if c[countt] in word[count]:
				new_list[count] = ""
	"".join(new_list)
	new_word = ""

	for let in new_list:
		new_word += let

	return new_word

def decode(s):
	if s == "":
		return ""
	else:
		return chr(ord(s[0])-5) + decode(s[1:])

def encode(s):
	if s == "":
		return ""
	else:
		return chr(ord(s[0])+5)+ encode(s[1:])

def stringList(str1):
	return str1.split()

def encodeM(lst, cnt = 0):
	last_elem = lst[-1]
	if lst[cnt] == last_elem:
		return encode(lst[cnt])
	else:
		return [encode(lst[cnt])] + [encodeM(lst,cnt+1)]

def decodeM(lst, cnt = 0):
	last_elem = lst[-1]
	if lst[cnt] == last_elem:
		return decode(lst[cnt])
	else:
		return [decode(lst[cnt])] + [decodeM(lst,cnt+1)]

def main(s):
	slst=removePun(s)
	eList = encodeM(stringList(slst))
	dList = decodeM(eList)
	print("Given string =>", s)
	print("Punctuation removed =>", slst)
	print("List Encoded =>", eList)
	print("List Decoded =>", dList)
	print ("Encoded Message =>",' '.join(eList))