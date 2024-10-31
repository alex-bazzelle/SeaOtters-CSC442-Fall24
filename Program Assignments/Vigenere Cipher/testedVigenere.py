import sys

abc = "abcdefghijklmnopqrstuvwxyz"
mode = sys.argv[1] # -e or -d
key = sys.argv[2] # key
key = key.lower() # key case doesnt matter

while(True):
	try:
		text = input() # get message to encrypt or decrypt
		result = "" # reset the result

		for i in range(0,len(text)): # for each char
			if text[i].isalpha(): # make sure it's alphabet
				if mode == "-e": # if encrypting, letter = (Pi + Ki)%26
					letter = abc[(abc.index(text[i].lower()) + abc.index(key[i%len(key)]))%26]
				elif mode == "-d": # if decrypting, letter = (26 + Ci - Ki)%26
					letter = abc[(26 + abc.index(text[i].lower()) - abc.index(key[i%len(key)]))%26]
				
				if text[i].upper() == text[i]: # if it's uppercase
					letter = letter.upper() # make the result letter uppercase
			else: letter = text[i] # if not alphabet, just add it
			result += letter # add to result
		sys.stdout.write(f"{result}\n")

	except KeyboardInterrupt:
		sys.stdout.write(f"\n")
		break
