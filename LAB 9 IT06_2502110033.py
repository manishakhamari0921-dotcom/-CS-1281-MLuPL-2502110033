import os
import csv
from datetime import datetime

data_folder = "data"
output_folder = "output"

os.makedirs(data_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)


# Process one file
def process_file(filename):

    accepted = []
    rejects = []

    filepath = os.path.join(data_folder, filename)

    with open(filepath, "r") as file:
        lines = file.readlines()

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

    total = sum(row[1] for row in accepted)

    average = total / len(accepted) if accepted else 0

    # Individual report
    report_name = filename.replace(".txt", "_report.txt")
    report_path = os.path.join(output_folder, report_name)

    with open(report_path, "w") as file:

        file.write("PRODUCTION REPORT\n")
        file.write("====================\n")

        file.write("File: " + filename + "\n")
        file.write("Records: " + str(len(lines)) + "\n")
        file.write("Accepted: " + str(len(accepted)) + "\n")
        file.write("Rejected: " + str(len(rejects)) + "\n")
        file.write("Total quantity: " + str(total) + "\n")
        file.write("Average quantity: " + str(average) + "\n")

        file.write("\nACCEPTED RECORDS\n")

        for row in accepted:
            file.write(str(row) + "\n")

    return len(lines), len(accepted), len(rejects), total


# BATCH PROCESSING
total_records = 0
total_accepted = 0
total_rejected = 0
total_quantity = 0

history = []

for filename in os.listdir(data_folder):

    if filename.endswith(".txt") and filename != "report.txt":

        result = process_file(filename)

        records, accepted, rejected, quantity = result

        total_records += records
        total_accepted += accepted
        total_rejected += rejected
        total_quantity += quantity

        history.append([
            filename,
            records,
            accepted,
            rejected
        ])

        print("Processed:", filename)


# COMBINED PLANT SUMMARY
with open(os.path.join(output_folder, "plant_summary.txt"), "w") as file:

    file.write("COMBINED PLANT SUMMARY\n")
    file.write("========================\n")

    file.write("Total records: " + str(total_records) + "\n")
    file.write("Total accepted: " + str(total_accepted) + "\n")
    file.write("Total rejected: " + str(total_rejected) + "\n")
    file.write("Total quantity: " + str(total_quantity) + "\n")


# APPEND RUN HISTORY
history_file = os.path.join(output_folder, "run_history.csv")

file_exists = os.path.exists(history_file)

with open(history_file, "a", newline="") as file:

    writer = csv.writer(file)

    if not file_exists:
        writer.writerow([
            "Timestamp",
            "Filename",
            "Records",
            "Accepted",
            "Rejected"
        ])

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for row in history:
        writer.writerow([timestamp] + row)


print("\n========== BATCH COMPLETED ==========")
print("Total records:", total_records)
print("Accepted:", total_accepted)
print("Rejected:", total_rejected)
print("Total quantity:", total_quantity)

print("\nReports saved in output folder.")
print("Run history updated successfully.")
