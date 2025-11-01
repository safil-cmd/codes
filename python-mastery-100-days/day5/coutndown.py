import time
start = int(input("Enter the number for countdown:"))
print("\n------countdown begins now!-------")
while start >= 0:
    print(start)
    time.sleep(1)
    start -=1
print("\n-----countdown ends------")