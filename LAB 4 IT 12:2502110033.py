import random

print("Machine Production Report")

for part in range(1, 11):
    diameter = random.uniform(24.90, 25.10)

    print("Part:", part,
          "Diameter:", format(diameter, ".2f"))
