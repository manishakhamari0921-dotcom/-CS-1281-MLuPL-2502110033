import os
import csv

os.makedirs("data", exist_ok=True)

input_file = "data/shift_log.txt"

# Create sample input if missing
if not os.path.exists(input_file):

    sample = [
        "PART-101,10,Steel",
        "PART-102,20,Iron",
        "INVALID,30,Copper",
        "PART-103,-5,Wood",
        "PART-104,15,Plastic"
    ]

    with open(input_file, "w") as f:
        f.write("\n".join(sample))


accepted = []
rejects = []

# READ
with open(input_file, "r") as file:
    lines = file.readlines()


# PARSE AND VALIDATE
for line in lines:

    line = line.strip()

    try:
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

        accepted.append([code, quantity, material.strip()])

    except (ValueError, TypeError) as e:
        rejects.append([line, str(e)])


# AGGREGATE
total_quantity = sum(row[1] for row in accepted)

average = (
    total_quantity / len(accepted)
    if accepted else 0
)


# WRITE HUMAN REPORT
with open("data/report.txt", "w") as file:

    file.write("PRODUCTION REPORT\n")
    file.write("========================\n")

    file.write("Total records: " + str(len(lines)) + "\n")
    file.write("Accepted: " + str(len(accepted)) + "\n")
    file.write("Rejected: " + str(len(rejects)) + "\n")

    file.write("Total quantity: " + str(total_quantity) + "\n")
    file.write("Average quantity: " + str(average) + "\n")

    file.write("\nACCEPTED RECORDS\n")

    for row in accepted:
        file.write(str(row) + "\n")


# WRITE REJECTS CSV
with open("data/rejects.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Bad Line", "Reason"])
    writer.writerows(rejects)


print("Pipeline completed successfully!")
print("Report saved in data/report.txt")
print("Rejects saved in data/rejects.csv")
