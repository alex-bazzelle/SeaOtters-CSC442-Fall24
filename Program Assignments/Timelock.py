import sys

# Just setup the inputs for later use
# I believe we have to get the time elapsed from 0000 00 00 00 00 in minutes for each and sub the current from the old
# that way we get the minute difference between. to determine the daylight savings im not so sure how it should
# be done

CURRENT_TIME = "2017 03 23 18 02 06"

input = sys.stdin.readline().strip()
cleanInput = input.strip('"')

# Year Month Day Hour Minute Second
# YY MM DD HH mm SS
splitInput = cleanInput.split()
splitCurrent = CURRENT_TIME.strip('"').split()


for x in splitInput:
    print("TestInput = {}".format(x))
for x in splitCurrent:
    print("Test Current = {}".format(x))

    