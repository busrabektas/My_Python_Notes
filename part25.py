import time

print(time.ctime(0)) # convert a time expressed in seconds since epoch to a readable string
#                    epoch = when your computer thinks time began (reference point)

print(time.time())  # return current seconds since epoch

print(time.ctime(time.time())) # current time

time_object = time.localtime() # current time
print(time_object)
print(time.strftime("%B %d %Y %H:%M:%S ",time_object)) # month,day,year,hours,minutes,seconds

time_string = "20 April,2020"
time_object=time.strptime(time_string,"%d %B,%Y")
print(time_object)

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
print(time.mktime(time_tuple))
print(time.asctime(time_tuple))