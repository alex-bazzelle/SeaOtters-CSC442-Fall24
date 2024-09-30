import sys

abc = "abcdefghijklmnopqrstuvwxyz"
mode = sys.argv[1] # -e or -d
key = sys.argv[2] # key
key = key.lower() # key case doesnt matter

while(True):
	try:
		if mode == "-e": # encryption
			text = input()
			cipher = ""
			for i in range(0,len(text)): # for each char to encrypt
				letter = abc[(abc.index(text[i].lower()) + abc.index(key[i%len(key)]))%26] # letter = (Pi + Ki)%26
				if text[i].upper() == text[i]: # if it's uppercase
					letter = letter.upper() # make the encrypted text uppercase
				cipher += letter # add to encrypted text
			sys.stdout.write(f"{cipher}\n")

		if mode == "-d":
			cipher = input()
			text = ""
			for i in range (0,len(cipher)): # for each char to decrypt
				letter = abc[(26 + abc.index(cipher[i].lower()) - abc.index(key[i%len(key)]))%26] # letter = (26 + Ci - Ki)%26
				if cipher[i].upper() == cipher[i]: # if it's uppercase
					letter = letter.upper() # make decrypted text uppercase
				text += letter # add to decrypted text
			sys.stdout.write(f"{text}\n")
	except KeyboardInterrupt:
		sys.stdout.write(f"\n")
		break
