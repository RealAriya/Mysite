import random

x = random.randint(1,100)

if x%2 == 0:
    print(f"{x} is even.")
elif x == 0:
    print("Error")
else:
    print(f"{x} is odd.")


