dictionary = {}
q = input("Czy chcesz dodać nowe dane? (t/n):")
r = 0
while q == "t":
    r += 1
    n = input("Podaj imię:")
    a = input("Podaj wiek:")
    h = input("Podaj wzrost:")
    dictionary[r] = {}
    dictionary[r].update({"Record": r, "Name": n, "Age": a, "Height": h})
    for r, data in dictionary.items():
        print()
        for value in data:
            print(value, data[value])
    print()
    q = input("Czy chcesz dodać nowe dane?")
print("Oto Twoje dane:")
for r, data in dictionary.items():
    print()
    for value in data:
        print(value, data[value])
print()
