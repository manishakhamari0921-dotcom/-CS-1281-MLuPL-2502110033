# Custom exception example

class SpecViolation(Exception):
    pass


# Operating method
def process_job(code, quantity, material):

    if not code.startswith("PART-"):
        raise SpecViolation("Invalid part code")

    if quantity <= 0:
        raise SpecViolation("Quantity must be positive")

    if material.strip() == "":
        raise SpecViolation("Material is missing")

    return "Job processed successfully"


# Driving program
jobs = [
    ("PART-101", 10, "Steel"),
    ("INVALID", 20, "Iron"),
    ("PART-103", -5, "Copper"),
    ("PART-104", 15, "Aluminium")
]

for job in jobs:

    try:
        result = process_job(job[0], job[1], job[2])
        print(job, ":", result)

    except SpecViolation as e:
        print(job, ": REJECTED -", e)

print("\nMachine processing completed.")
