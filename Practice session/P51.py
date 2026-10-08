import time
loc=time.localtime()
print("Current time:\n",loc.tm_hour,":",loc.tm_min,":",loc.tm_sec)
print("Current date:\n",loc.tm_mday,"/",loc.tm_mon,"/",loc.tm_year)
#or do it using strftime()
print("Current time:\n",time.strftime("%H:%M:%S", loc))
print("Current date:\n",time.strftime("%d/%m/%Y", loc))
#strftime() can also be used to format the date and time in a more readable way. For example, you can use the following format codes:
#%A - Full weekday name (e.g. Monday)
#%B - Full month name (e.g. January)
#%d - Day of the month (01-31)
#%m - Month as a zero-padded decimal number (01-12)
#%Y - Year with century (e.g. 2023)