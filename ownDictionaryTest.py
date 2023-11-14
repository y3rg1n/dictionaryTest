userData = {}
r = 0

while (True):
    print()
    print("1. Add data")
    print("2. Search for data")
    print("3. Delete data")
    print("4. Show data")
    print("5. End")
    q = input("Please choose:")

    if (q == "1"):
        r += 1
        n = input("Input name:")
        a = input("Input age:")
        h = input("Input height:")
        userData[r] = {}
        userData[r].update({"Record": r, "Name": n, "Age": a, "Height": h})

    elif (q == "2"):
        k = input("Type what are you looking for?")
        if k in userData:
            print("YES!")
        else:
            print("No data found.")

    elif (q == "3"):
        print()

    elif (q == "4"):
        for r, data in userData.items():
            print()
            for value in data:
                print(value + ":", data[value])
        print()

    elif (q == "5"):
        break

