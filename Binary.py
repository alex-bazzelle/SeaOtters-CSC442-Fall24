import sys

binary = "" # Store the binary
answer = "" # Store the answer
inc = 8     # Incrament Length for loop

for line in sys.stdin:      # for the lines in the file
    binary += line.strip()  # adds each line removing spaces

if len(binary) % 7 == 0:    # Assume length is divisable by 8 unless it is divisable by 7
    inc = 7

for i in range(0, len(binary), inc): # starting at 0, loop the length, inctamenting by inc
    answer += chr(int(binary[i:i+inc], 2))

sys.stdout.write(answer + "\n") #write the answer to terminal and move to next line