import socket
from sys import stdout
from time import time

# CHAT SERVER
ip = "138.47.99.83"
port = 31337
# DELAY LIMIT
delayLimit = 0.045

# connect to server
stdout.write("[connecting to chat server]\n")
chat = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
chat.connect((ip,port))
stdout.write(".....\n")

data = chat.recv(4096).decode() # get first data
dataList = [] # TESTING
delays=[] # make list of delays
while( data.rstrip("\n") != "EOF" ): # while not EOF
    while(len(data)>1): # in case it was too fast
        stdout.write(data[0]); stdout.flush()
        dataList.append(data[0]) # TESTING
        delays.append(0)
        data = data[1:]
    dataList.append(data) #TESTING
    stdout.write(data) # print chat to stdout
    stdout.flush()

    t0 = time() # start time
    data = chat.recv(4096).decode() # wait for message
    t1 = time() # end time

    delta = round(t1-t0, 3) # find the delay

    delays.append(delta) # add to list of delays

chat.close()
stdout.write("\n[disconneting from chat server]\n")
stdout.flush()

stdout.write("Data:\n{}".format(dataList)) # TESTING
# i'll make this code better after it works
message1 = ""
message2 = ""
for delt in delays:
    if(delt > delayLimit): message1 += "1"
    else: message1 += "0"

for delt in delays:
    if(delt > delayLimit): message2 += "0"
    else: message2 += "1"

# TESTING
stdout.write("\nMessage Length: {}\nB1: {}\nB2: {}\n".format(len(message1),message1,message2))
stdout.flush()


decodedMessage = ["8-bit: ","7-bit: "]

for asciiBits in range(7,9): # tries 7 and 8 bit ascii
    stdout.write("\n\n{}-bit Binary (type1):\n".format(asciiBits))
    #if(len(message)%asciiBits == 0): # neither works :(
    for i in range(0,len(message1),asciiBits): # 0 to end of message, increments in 7s or 8s
        byte = message1[i:(i+asciiBits)] # isolate the byte
        stdout.write("Byte: {} ".format(byte)); stdout.flush() # TESTING
        if( (int(byte,2) >= 32) and (int(byte,2) <= 126) ): # if printable ascii character
            decodedMessage[8-asciiBits] += chr(int(byte,2)) # add to decoded message
            stdout.write("({})".format(chr(int(byte,2)))); stdout.flush() # TESTING
        else:
            pass
        stdout.write("\n"); stdout.flush()

# i will also fix this after it works. this tries swapping the 1s and 0s
for asciiBits in range(7,9): # tries 7 and 8 bit ascii
    stdout.write("\n\n{}-bit Binary (type2):\n".format(asciiBits))
    #if(len(message)%asciiBits == 0):
    for i in range(0,len(message2),asciiBits):
        byte = message2[i:(i+asciiBits)]
        stdout.write("Byte: {} ".format(byte))
        stdout.flush()
        if( (int(byte,2) >= 32) and (int(byte,2) <= 126) ):
            decodedMessage[8-asciiBits] += chr(int(byte,2))
            stdout.write("({})".format(chr(int(byte,2))))
            stdout.flush()
        else:
            pass
        stdout.write("\n"); stdout.flush()

# uncomment this when it works
#stdout.write("Covert message: {}\n".format(decodedMessage))
#stdout.flush()