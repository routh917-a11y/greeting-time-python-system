import time
timestamp= time.strftime('%H:%M:%S')
print(timestamp)
timestamp1= time.strftime('%H')
print(timestamp1)
timestamp2= time.strftime('%M')
print(timestamp2)
timestamp3= time.strftime('%S')
print(timestamp3)

if (0<int(timestamp1)<12) :
    print("good morning bhaiya")

elif (12<int(timestamp1)<16):
  print("good afternoon bhaiya")

else:
     print("good evening")     