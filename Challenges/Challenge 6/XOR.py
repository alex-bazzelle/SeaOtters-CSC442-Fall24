# File to implement Xor Crypto Program 6
import sys

# Gets the input data as a bytearray
data = bytearray(sys.stdin.buffer.read())

# Get the key as a bytearray
with open('key2-1', 'rb') as key_file:
    key = bytearray(key_file.read())
    

def xorData(dataSet, keySet):
    dataSize = len(data)
    keySize = len(key)
    xorSol = bytearray()
    
    # If both are the same size, xor them together then append to output the bytes
    if (dataSize != keySize):
        sys.stdout.write("Unmatching Size's")
    else:
        for i in range(dataSize):
            xorSol.append(dataSet[i]^keySet[i])
            
    # print("Data Size: {}".format(dataSize))
    # print("Key Size: {}".format(keySize))
    return xorSol
    
# Currently cant encrypt unless key is same size, not sure how to implement that
 
result = xorData(data,key)
sys.stdout.buffer.write(result)
