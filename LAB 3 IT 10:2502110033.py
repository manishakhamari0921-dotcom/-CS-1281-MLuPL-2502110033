count = {
    "ACCEPT": 0,
    "REWORK": 0,
    "SCRAP": 0
}

for i in range(1, 11):
    d = float(input("Enter diameter: "))

    if d >= 9.5 and d <= 10.5:
        result = "ACCEPT"

    elif d >= 9.0 and d <= 11.0:
        result = "REWORK"

    else:
        result = "SCRAP"

    print(result)
    count[result] += 1

print("\nFINAL REPORT")
print("ACCEPT:", count["ACCEPT"])
print("REWORK:", count["REWORK"])
print("SCRAP:", count["SCRAP"])
