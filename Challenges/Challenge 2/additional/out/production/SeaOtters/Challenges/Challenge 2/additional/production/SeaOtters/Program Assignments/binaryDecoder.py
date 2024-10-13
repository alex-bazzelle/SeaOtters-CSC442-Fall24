import sys

binary = ""

for line in sys.stdin:
    binary += line.strip()

answer = ""

if len(binary) % 8 == 0:
    for i in range(0, len(binary), 8):
        answer += chr(int(binary[i:i+8], 2))
else:
    for i in range(0, len(binary), 7):
        answer += chr(int(binary[i:i+7], 2))

sys.stdout.write(answer)
