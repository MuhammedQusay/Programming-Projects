import time

x = None

while not isinstance(x, int) or x <= 0:
    try:
        x = int(input("Enter your num (positive integer): "))
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

for i in range(x , 0 , -1):
    sec = i %60
    min = int((i // 60) %60)
    hor = int((i // 3600) %24)
    day = int(i // 86400)
    print(f"{day:02}:{hor:02}:{min:02}:{sec:02}")
    time.sleep(1)
