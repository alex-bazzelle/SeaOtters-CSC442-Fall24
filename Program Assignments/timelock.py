import datetime
import time
import sys
import hashlib

date_format = "%Y-%m-%d %H:%M:%S"

sys_current = datetime.datetime.now() #takes system time
#debugging variables - sets system time 
sys_test = datetime.datetime.strptime("2013-5-6 7:43:25", date_format)
sys_test = sys_test - datetime.timedelta(hours=1, minutes=0)

#reads epoch date input and converts to datetime obj
epoch_date = "%s-%s-%s %s:%s:%s" % (int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))
print (epoch_date)
epoch_date = datetime.datetime.strptime(epoch_date, date_format)

#subtracts for timestamp
difference = sys_test - epoch_date
print (difference)

#gets number of seconds passed
diff_sec = difference.total_seconds()
print (diff_sec)

#gets hash of difference
#Have been trying different combos of numbers and 'big' or 'little'
diff_sec_int = int(diff_sec)
hashed_date = hashlib.md5(diff_sec_int.to_bytes(7, 'big', signed=True)).hexdigest()

print ("hashed date: ", hashed_date)
