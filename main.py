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