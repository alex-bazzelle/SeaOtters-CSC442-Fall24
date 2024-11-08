import datetime
import sys
import hashlib
#######################
timeDelta = 0
#######################
# march 10th 2am -> 1am
# nov 3rd 2am -> 3am


date_format = "%Y-%m-%d %H:%M:%S"
current = datetime.datetime.now() # takes system time
#debugging currentTime - sets system time 
#current = datetime.datetime.strptime("2017-4-23 18:2:30", date_format)
#current = datetime.datetime(2015,1,1,0,0,0)
current = current - datetime.timedelta(hours=timeDelta, minutes=0) # adjust for DST

#reads epoch date input and converts to datetime obj
#epoch = "%s-%s-%s %s:%s:%s" % (int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))
#epoch = datetime.datetime.strptime(epoch, date_format)
epoch = datetime.datetime(2001,2,3,4,5,6)

#subtracts for timestamp
difference = current - epoch

# accounts for intervals
secondDelta = 0
if(current.second > epoch.second): secondDelta = current.second-epoch.second
if(current.second < epoch.second): secondDelta = 60 - (epoch.second - current.second)
diff_sec = difference.total_seconds() - secondDelta

def condense_hash(hash):
    foundCount = 0
    final_string = ""
    for letter in hash:
        if not letter.isdigit() and foundCount < 2:
            #print ("letter found! ", i)
            final_string += letter
            foundCount += 1
    foundCount = 0
    for number in reversed(hash):
        if number.isdigit() and foundCount < 2:
            #print ("number found! ", i)
            final_string += number
            foundCount += 1
    
    return final_string

# get hash
diff_sec_int = int(diff_sec); diff_sec_str = str(diff_sec_int)
hash1 = hashlib.md5(diff_sec_str.encode()).hexdigest()
hash2 = hashlib.md5(hash1.encode()).hexdigest()
print("Full Hash: {}".format(hash2))

# CUSTOM CODE HERE
y = hash2[(len(hash2)//2)-1] + hash2[(len(hash2)//2)]
print ("Code: {}{}".format(condense_hash(hash2),y))
