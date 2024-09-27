import sys

alphabetLower = { # The full lower case aplphabet 
    "a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25
}
reverseLower = {v:k for k, v in alphabetLower.items()} # The reverse of the lower case alphabet

alphabetUpper = { # The full upper case aplphabet 
    "A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25
}
reverseUpper = {v:k for k, v in alphabetUpper.items()} # The reverse of the upper case alphabet

mode = sys.argv[1] # -e or -d
initalKey = sys.argv[2].lower() # what the key is and lower casing it for simplicity

while(True): 
    try:
        text = input() # gets the new text to be scramble or unscrable 
        key = "" # clears the key so it can be matched to length of the new text
        answer = "" # clears the return answer for everytime before ^C

        while len(key) < len(text):    # The 2 while loops make it so the key  
            key += initalKey           # is the same length as the input text
        while len(key) != len(text):   # key = "key"    text = "12345"
            key = key[:-1]             # key = "keyke"  text = "12345"

        if mode == "-e": # -e is encryption
            for i in range(0, len(text)):
                if not text[i].isalpha(): # determines if the string is in the alphabet or not 
                    answer += text[i]     # adds the non alphabet string to the answer
                elif text[i].islower():   # determines which library to use for each letter
                    answer += reverseLower[(alphabetLower[text[i]] + alphabetLower[key[i]]) % 26]
                else: 
                    answer += reverseUpper[(alphabetUpper[text[i]] + alphabetLower[key[i]]) % 26]

        if mode == "-d": # -d is decryption
            for i in range(0, len(text)):
                if not text[i].isalpha(): # determines if the string is in the alphabet or not
                    answer += text[i]     # adds the non alphabet string to the answer 
                elif text[i].islower():   # determines which library to use for each letter
                    answer += reverseLower[(26 + alphabetLower[text[i]] - alphabetLower[key[i]]) % 26]
                else:
                    answer += reverseUpper[(26 + alphabetUpper[text[i]] - alphabetLower[key[i]]) % 26]

        sys.stdout.write(f"{answer}\n")   

    except KeyboardInterrupt:
        sys.stdout.write(f"\n")
        break