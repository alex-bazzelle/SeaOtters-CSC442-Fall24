import datetime
import time
import sys
import hashlib

date_format = "%Y-%m-%d %H:%M:%S"

current = datetime.datetime.now() #takes system time
#debugging currentTime - sets system time 
current = datetime.datetime.strptime("2013-5-6 7:43:25", date_format)
current = current - datetime.timedelta(hours=1, minutes=0)

#reads epoch date input and converts to datetime obj
epoch = "%s-%s-%s %s:%s:%s" % (int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))
print (epoch)
epoch = datetime.datetime.strptime(epoch, date_format)

#subtracts for timestamp
difference = current - epoch
print (difference)

#gets number of seconds passed
diff_sec = difference.total_seconds() - (current.second + 1) #accounts for the intervals
print (diff_sec)

#gets hash of difference
#Have been trying different combos of numbers and 'big' or 'little'
# was supposed to encode it as a string, round to the start of the interval, and hash it twice
diff_sec_int = int(diff_sec)
diff_sec_str = str(diff_sec_int)
hash1 = hashlib.md5(diff_sec_str.encode()).hexdigest()
hash2 = hashlib.md5(hash1.encode()).hexdigest()
#hashed_date = hashlib.md5(diff_sec_int.to_bytes(7, 'big', signed=True)).hexdigest()
print("hash1: {}".format(hash1))
print("hash2: {}".format(hash2))
#print ("hashed date: ", hashed_date)
