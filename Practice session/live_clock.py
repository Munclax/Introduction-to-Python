import time
while True:
  loc=time.localtime()
  print(time.strftime("%H:%M:%S",loc),end="\r")
  time.sleep(1)
  
