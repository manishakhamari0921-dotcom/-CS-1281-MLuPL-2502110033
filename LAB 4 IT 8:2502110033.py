import random

mode = input("Enter HALT or SKIP: ").upper()

a = 0
r = 0
s = 0
i = 0

if mode == "HALT" or mode == "SKIP":

    while i < 10:
        d = round(random.uniform(24.90, 25.10), 2)
        i += 1

        print("\nDiameter:", d)

        if 24.95 <= d <= 25.05:
            print("ACCEPT")
            a += 1

        elif 24.90 <= d <= 25.10:
            print("REWORK")
            r += 1

        else:
            print("SCRAP")
            s += 1

            if mode == "HALT":
                break
            else:
                continue

    print("\nFINAL REPORT")
    print("Inspected:", i)
    print("Accept:", a)
    print("Rework:", r)
    print("Scrap:", s)

else:
    print("Invalid mode")
