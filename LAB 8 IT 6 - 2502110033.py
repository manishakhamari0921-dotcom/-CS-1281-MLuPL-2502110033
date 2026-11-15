# Automated self-testing program

def parse_line(line):

    parts = line.split(",")

    if len(parts) != 3:
        raise ValueError("Expected 3 fields")

    code, quantity, material = parts

    if not code.startswith("PART-"):
        raise ValueError("Invalid part code")

    quantity = int(quantity)

    if quantity <= 0:
        raise ValueError("Invalid quantity")

    if not material.strip():
        raise ValueError("Missing material")

    return code, quantity, material.strip()


def run_tests():

    hostile = [
        "",
        "PART-101,10,Steel",
        "INVALID,20,Iron",
        "PART-102,-5,Copper",
        "PART-103,abc,Wood",
        "PART-104,0,Plastic",
        "PART-105,10",
        "PART-106,10,"
    ]

    print("\n========== AUTOMATED TESTING ==========")

    passed = 0
    failed = 0

    for i, line in enumerate(hostile, 1):

        try:
            parse_line(line)

            # Only the valid second input should pass
            if i == 2:
                print("Test", i, ": PASS")
                passed += 1
            else:
                print("Test", i, ": FAIL")
                failed += 1

        except (ValueError, TypeError):
            if i == 2:
                print("Test", i, ": FAIL")
                failed += 1
            else:
                print("Test", i, ": PASS")
                passed += 1

    print("\n========== TEST SUMMARY ==========")
    print("Passed:", passed)
    print("Failed:", failed)
    print("Total:", len(hostile))


if __name__ == "__main__":
    run_tests()
