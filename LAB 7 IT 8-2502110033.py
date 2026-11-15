
# IT8 - The Machine Runs a Batch (Version 2)

class ProductionMachine:

    def __init__(self, name, rpm_limit):
        self.name = name
        self.rpm_limit = rpm_limit
        self.total_parts = 0
        self.accepted = 0
        self.rejected = 0

    # Process an individual job
    def process_job(self, job_no, rpm, quantity):

        if rpm < 500 or rpm > self.rpm_limit:
            self.rejected += 1
            return f"Job {job_no}: Rejected (RPM error)"

        if quantity <= 0:
            self.rejected += 1
            return f"Job {job_no}: Rejected (Quantity error)"

        self.total_parts += quantity
        self.accepted += 1

        return f"Job {job_no}: Completed successfully"

    # Machine report
    def status(self):
        return {
            "Machine": self.name,
            "Accepted Jobs": self.accepted,
            "Rejected Jobs": self.rejected,
            "Production": self.total_parts
        }


# Ten production log entries
logs = [
    "01,1200,8",
    "02,1800,6",
    "03,3200,5",
    "04,900,10",
    "05,2400,7",
    "06,400,4",
    "07,1500,9",
    "08,2800,3",
    "09,2000,12",
    "10,1000,5"
]


# Create machine object
press = ProductionMachine("Hydraulic-Press", 3000)

# Process all jobs
print("PRODUCTION BATCH\n")

for record in logs:

    job, speed, quantity = record.split(",")

    message = press.process_job(
        int(job),
        int(speed),
        int(quantity)
    )

    print(message)


# Display final report
print("\nFINAL SHIFT REPORT")
print(press.status())
