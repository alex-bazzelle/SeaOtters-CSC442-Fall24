import datetime
import sys
import hashlib

date_format = "%Y-%m-%d %H:%M:%S"

current = datetime.datetime.now() #takes system time
#debugging currentTime - sets system time 
#current = datetime.datetime.strptime("2017-4-23 18:2:30", date_format)
current = current - datetime.timedelta(hours=1, minutes=0)

#reads epoch date input and converts to datetime obj
epoch = "%s-%s-%s %s:%s:%s" % (int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))
epoch = datetime.datetime.strptime(epoch, date_format)

#subtracts for timestamp
difference = current - epoch

#gets number of seconds passed
diff_sec = difference.total_seconds() - (current.second + 1) #accounts for the intervals

def condense_hash(hash):
    j = 0
    final_string = ""
    for i in hash:
        if not i.isdigit() and j < 2:
            #print ("letter found! ", i)
            final_string += i
            j += 1
    j = 0
    for i in reversed(hash):
        if i.isdigit() and j < 2:
            #print ("number found! ", i)
            final_string += i
            j += 1
    
    return final_string

#gets hash of difference
#Have been trying different combos of numbers and 'big' or 'little'
# was supposed to encode it as a string, round to the start of the interval, and hash it twice
diff_sec_int = int(diff_sec)
diff_sec_str = str(diff_sec_int)
hash1 = hashlib.md5(diff_sec_str.encode()).hexdigest()
hash2 = hashlib.md5(hash1.encode()).hexdigest()
#hashed_date = hashlib.md5(diff_sec_int.to_bytes(7, 'big', signed=True)).hexdigest()
#print("hash1: {}".format(hash1))
#print("hash2: {}".format(hash2))
#print ("hashed date: ", hashed_date)
print (condense_hash(hash2))
