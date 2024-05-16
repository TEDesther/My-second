number=1

for i in range(1000):
    new=number+i
    if (new%2 == 0 and new%3 == 0 and new%5 == 0 and new%7 == 0):
        print(new)