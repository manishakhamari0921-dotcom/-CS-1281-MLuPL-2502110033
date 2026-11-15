accepted = []
rework = 0
scrap = 0

for i in range(10):
    d = float(input("Enter diameter: "))

    if 9.5 <= d <= 10.5:
        accepted.append(d)

    elif 9.0 <= d <= 11.0:
        rework += 1

    else:
        scrap += 1

total = len(accepted)

boxes = total // 4
loose = total % 4

print("\nEND OF SHIFT REPORT")
print("Accepted:", total)
print("Rework:", rework)
print("Scrap:", scrap)
print("Full boxes:", boxes)
print("Loose parts:", loose)
print("Accepted diameters:", accepted)
