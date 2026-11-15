
# IT12 - Rough Cut: Three Jigs

# Jig 1: Inspect component diameter
def inspect(dia):
    if dia < 10 or dia > 40:
        return "Out of Spec"
    elif dia < 20:
        return "Small"
    elif dia < 30:
        return "Medium"
    else:
        return "Large"


# Jig 2: Count component labels
def tally(labels):
    counts = {}

    for label in labels:
        counts[label] = counts.get(label, 0) + 1

    return counts


# Jig 3: Generate shift report
def report(shift, counts):
    total = sum(counts.values())

    return (
        f"Shift {shift} | "
        f"Total Parts: {total} | "
        f"Details: {counts}"
    )


# Test each function independently
if __name__ == "__main__":

    # Test 1: Inspect
    print("JIG 1 - INSPECTION")
    print(inspect(15))
    print(inspect(25))
    print(inspect(35))
    print(inspect(45))

    # Test 2: Tally
    print("\nJIG 2 - TALLY")
    labels = ["Small", "Medium", "Small",
              "Large", "Medium", "Small"]
    counts = tally(labels)
    print(counts)

    # Test 3: Report
    print("\nJIG 3 - REPORT")
    print(report("A", counts))
