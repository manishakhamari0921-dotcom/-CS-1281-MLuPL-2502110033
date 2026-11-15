
# IT10 - Refactor Lab 04

# Function 1: Inspect component
def inspect(dia):
    if dia < 10 or dia > 40:
        return "Out of Spec"
    elif dia < 20:
        return "Small"
    elif dia < 30:
        return "Medium"
    else:
        return "Large"


# Function 2: Count labels
def tally(labels):
    counts = {}

    for label in labels:
        counts[label] = counts.get(label, 0) + 1

    return counts


# Function 3: Generate report
def report(shift, counts):
    total = sum(counts.values())

    return (
        f"Shift {shift} | "
        f"Total Parts: {total} | "
        f"Details: {counts}"
    )


# Main program
def main():

    diameters = [15, 22, 35, 18, 27, 45, 32]

    labels = []

    for dia in diameters:
        labels.append(inspect(dia))

    counts = tally(labels)

    print(report("A", counts))


if __name__ == "__main__":
    main()
