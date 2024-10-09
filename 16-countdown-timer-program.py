import time as t
my_time = int(input("enter the nunber of seconds: "))

for x in range(my_time, 0, -1):
    seconds = x%60
    minutes = int(x/60)%60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    t.sleep(1)






print("Time is up")