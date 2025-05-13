#FuzzBuzz Exercise:

def FuzzBuzz(Start, Ende):
    for i in range(Start, Ende):
        if i % 3 == 0 and i % 5 == 0:
            print("FuzzBuzz")
        elif i % 3 == 0:
            print("Fuzz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

FuzzBuzz(1, 1000)