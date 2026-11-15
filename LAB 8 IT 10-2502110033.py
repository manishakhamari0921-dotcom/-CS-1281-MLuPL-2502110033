# Hardened parser with report and rejects table

records = [
    "PART-101,10,Steel",
    "PART-102,20,Iron",
    "INVALID,30,Copper",
    "PART-103,-5,Aluminium",
    "PART-104,15,Plastic",
    "PART-105,abc,Wood"
]

accepted = []
rejects = []

for line in records:
    try:
        parts = line.split(",")

        if len(parts) != 3:
            raise ValueError("Expected 3 fields")

        code, qty, material = parts

        if not code.startswith("PART-"):
            raise ValueError("Invalid part code")

        qty = int(qty)

        if qty <= 0:
            raise ValueError("Quantity must be positive")

        if not material.strip():
            raise ValueError("Missing material")

        accepted.append((code, qty, material.strip()))

    except ValueError as e:
        rejects.append((line, str(e)))

    except TypeError as e:
        rejects.append((line, str(e)))


# Calculate average safely
if len(accepted) > 0:
    average = sum(r[1] for r in accepted) / len(accepted)
else:
    average = 0


# Print report
print("\n========== PRODUCTION REPORT ==========")
print("Total accepted:", len(accepted))
print("Total rejected:", len(rejects))
print("Average quantity:", average)

print("\nAccepted Records:")
print("{:<15} {:<12} {}".format("Part Code", "Quantity", "Material"))

for r in accepted:
    print("{:<15} {:<12} {}".format(r[0], r[1], r[2]))


# Print rejects table
print("\n========== REJECTS TABLE ==========")
print("{:<35} {}".format("Bad Line", "Reason"))

for bad_line, reason in rejects:
    print("{:<35} {}".format(bad_line, reason))
