#FuzzBuzz Exercise:

for i in range(0, 100):
    if i % 3 == 0:
        print("Fuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 & i % 5 == 0:
        print("FuzzBuzz")
    else:
        print(i)