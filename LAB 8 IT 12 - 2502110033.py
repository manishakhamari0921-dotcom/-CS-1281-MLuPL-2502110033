# Eight hostile inputs for testing the parser

hostile = [
    "",
    "PART-101,10,Steel,Extra",
    "PART-102,-5,Iron",
    "PART-103,abc,Copper",
    "PART-104,0,Aluminium",
    "INVALID,10,Steel",
    "PART-105,10",
    "PART-106,10,"
]

def parse_line(line):
    parts = line.split(",")

    if len(parts) != 3:
        raise ValueError("Expected 3 fields")

    code, quantity, material = parts

    if not code.startswith("PART-"):
        raise ValueError("Invalid part code")

    quantity = int(quantity)

    if quantity <= 0:
        raise ValueError("Quantity must be positive")

    if not material.strip():
        raise ValueError("Material is missing")

    return code, quantity, material.strip()


print("HOSTILE INPUT TESTING")

for line in hostile:
    try:
        print("Testing:", repr(line))
        print("Result:", parse_line(line))
    except ValueError as e:
        print("Rejected:", e)
    except TypeError as e:
        print("Rejected:", e)
