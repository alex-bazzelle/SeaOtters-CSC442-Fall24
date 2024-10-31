import socket
from sys import stdout
from time import time

##########################
ip = "138.47.99.83"
port = 31337

delayLimit = 0.05

byteSize = 8
##########################

# connect to server
stdout.write("[connecting to chat server]\n\n")
chat = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
chat.connect((ip,port))

# get delays
delays = []
data = chat.recv(4096).decode() # get first data
while( data.rstrip("\n") != "EOF" ): # while not EOF
    stdout.write(data); stdout.flush() # print chat to stdout

    while(len(data)>1): # if delay was effectively 0
        delays.append(0) # then fix that
        data = data[1:]
    
    t0 = time() # start time
    data = chat.recv(4096).decode() # wait for message
    t1 = time() # end time

    delta = round(t1-t0, 3) # find the delay
    delays.append(delta) # add to list of delays

# disconnect from server
stdout.write("\n[disconneting from chat server]\n"); stdout.flush()
chat.close()

# try both combinations
message = ["",""]
for delt in delays:
    message[0] += "1" if delt>delayLimit else "0"
    message[1] += "0" if delt>delayLimit else "1"

# decode the message
decodedMessage = ["",""]; byte = ["",""]; finalMessage = ""
for version in range (0,2): # for each version
    for i in range(0,len(message[version]),byteSize): # for each byte
        byte[version] = message[version][i:(i+byteSize)] # isolate the byte
        if( 32 <= int(byte[version],2) <= 126 ): # if printable ascii character
            decodedMessage[version] += chr(int(byte[version],2)) # then add to decoded message
            if decodedMessage[version].endswith("EOF"): # if EOF
                finalMessage = decodedMessage[version][:-3] # then make final message
                break # and stop decoding

if finalMessage == "": # if no EOF
    finalMessage = "ERROR DECODING. CURRENT MESSAGE: " # say error and what you DID get
    finalMessage += decodedMessage[0] if len(decodedMessage[0])>len(decodedMessage[1]) else decodedMessage[1]

# print decoded message
stdout.write("{}\n".format(finalMessage))
stdout.flush()
