import os

os.makedirs("data", exist_ok=True)

records = [
    "PART-101,10,Steel",
    "PART-102,20,Iron",
    "PART-103,15,Copper",
    "PART-104,25,Aluminium",
    "PART-105,30,Plastic",
    "PART-106,12,Wood",
    "PART-107,18,Steel",
    "PART-108,22,Iron",
    "PART-109,16,Copper",
    "PART-110,14,Aluminium",
    "INVALID,20,Steel",
    "PART-111,-5,Iron",
    "PART-112,abc,Copper",
    "PART-113,19,Wood",
    "PART-114,28,Plastic"
]

with open("data/shift_log.txt", "w") as file:

    for record in records:
        file.write(record + "\n")

print("Shift log created successfully!")

# Read the file
with open("data/shift_log.txt", "r") as file:
    lines = file.readlines()

print("Total lines:", len(lines))
print("\nShift Log Records:")

for line in lines:
    print(line.strip())
