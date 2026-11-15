
# shoptools.py

# Inspect component diameter
def inspect(dia):

    if dia < 10 or dia > 40:
        return "Out of Spec"
    elif dia < 20:
        return "Small"
    elif dia < 30:
        return "Medium"
    else:
        return "Large"


# Count component labels
def tally(labels):

    counts = {}

    for label in labels:
        counts[label] = counts.get(label, 0) + 1

    return counts


# Generate shift report
def report(shift, counts):

    total = sum(counts.values())

    return (
        f"Shift {shift} | "
        f"Total Parts: {total} | "
        f"Details: {counts}"
# main.py

import shoptools

# Production measurements
diameters = [15, 22, 35, 18, 27, 45, 32]

# Inspect all components
labels = []

for dia in diameters:
    labels.append(shoptools.inspect(dia))

# Count component categories
counts = shoptools.tally(labels)

# Generate final shift report
result = shoptools.report("A", counts)

print("PRODUCTION REPORT")
print(result)

    )
