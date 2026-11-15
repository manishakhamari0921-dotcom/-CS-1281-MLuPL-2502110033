import random

def inspect(d):
    if 24.95 <= d <= 25.05:
        return "ACCEPT"
    elif 24.90 <= d <= 25.10:
        return "REWORK"
    else:
        return "SCRAP"

a = 0
r = 0
s = 0

for i in range(10):
    d = round(random.uniform(24.90, 25.10), 2)

    result = inspect(d)
    print(d, ":", result)

    if result == "ACCEPT":
        a += 1
    elif result == "REWORK":
        r += 1
    else:
        s += 1

print("\nSHIFT REPORT")
print("Accepted:", a)
print("Rework:", r)
print("Scrap:", s)
