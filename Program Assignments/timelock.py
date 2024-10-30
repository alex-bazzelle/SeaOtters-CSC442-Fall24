import datetime
import time
import sys
import hashlib

date_format = "%Y-%m-%d %H:%M:%S"

sys_current = datetime.datetime.now()
sys_test = datetime.datetime.strptime("2013-5-6 7:43:25", date_format)
sys_test = sys_test - datetime.timedelta(hours=1, minutes=0)

epoch_date = "%s-%s-%s %s:%s:%s" % (int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))
print (epoch_date)
epoch_date = datetime.datetime.strptime(epoch_date, date_format)

difference = sys_test - epoch_date
print (difference)

diff_sec = difference.total_seconds()
print (diff_sec)

diff_sec_int = int(diff_sec)
hashed_date = hashlib.md5(diff_sec_int.to_bytes(7, 'big', signed=True)).hexdigest()

print ("hashed date: ", hashed_date)