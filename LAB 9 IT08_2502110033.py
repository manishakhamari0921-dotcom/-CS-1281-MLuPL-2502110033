import re

# Regex pattern for parsing records
pattern = r"^\s*(PART-\d{3})\s*,\s*(\d+)\s*,\s*([A-Za-z]+)\s*$"


def parse_line(line):

    match = re.match(pattern, line)

    if not match:
        raise ValueError("Invalid record format")

    code = match.group(1)
    quantity = int(match.group(2))
    material = match.group(3)

    if quantity <= 0:
        raise ValueError("Quantity must be positive")

    return code, quantity, material


records = [
    "PART-101,10,Steel",
    " PART-102 , 20 , Iron ",
    "PART-103,15,Copper",
    "INVALID,20,Steel",
    "PART-104,-5,Wood",
    "PART-105,30,Plastic"
]

print("REGEX PARSING RESULTS")

for line in records:

    try:
        result = parse_line(line)
        print("VALID:", result)

    except ValueError as e:
        print("INVALID:", line, "-", e)


# Old split-based parsing:
# parts = line.split(",")
# This version is retained for comparison.
