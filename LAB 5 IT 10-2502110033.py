logs = [
    "P201, 24.98, DAY",
    "P202, 25.02, DAY",
    "P203, 24.95, DAY",
    "P204, 25.06, DAY",
    "P205, 24.99, DAY",
    "P206, 25.01, DAY",
    "P207, 24.97, DAY",
    "P208, 25.04, DAY",
    "P209, 24.93, DAY",
    "P210, 25.00, DAY"
]

def get_diameter(line):
    fields = line.split(",")
    return float(fields[1].strip())

diameters = [get_diameter(x) for x in logs]

print("Diameter List:", diameters)
print("Total Parts:", len(diameters))
print("Average:", round(sum(diameters) / len(diameters), 2))
print("Minimum:", min(diameters))
print("Maximum:", max(diameters))
