
# shoptools.py

class Machine:

    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.total_parts = 0
        self.job_count = 0
        self.busy = False

    # Check machine availability
    def is_free(self):
        return not self.busy

    # Execute production job
    def run_job(self, rpm, quantity):

        if self.busy:
            return False

        if rpm < 500 or rpm > self.limit or quantity <= 0:
            return False

        self.busy = True

        self.total_parts += quantity
        self.job_count += 1

        self.busy = False

        return True

    # Machine report
    def status(self):
        return {
            "Name": self.name,
            "Parts Produced": self.total_parts,
            "Jobs Completed": self.job_count,
            "Availability": self.is_free()
            
# main.py

from shoptools import Machine

# Create three machines
fleet = [
    Machine("CNC-A", 3000),
    Machine("CNC-B", 2800),
    Machine("CNC-C", 3200)
]

# Production job data
jobs = [
    (1200, 12),
    (1800, 8),
    (1500, 15),
    (900, 6),
    (2200, 10),
    (1100, 9),
    (2500, 14),
    (1700, 7),
    (2000, 13)
]

# Allocate jobs to the least-loaded free machine
for rpm, quantity in jobs:

    available = [
        machine for machine in fleet
        if machine.is_free()
    ]

    if available:

        selected = min(
            available,
            key=lambda machine: machine.total_parts
        )

        if selected.run_job(rpm, quantity):
            print(
                f"{quantity} parts allocated to "
                f"{selected.name}"
            )

    else:
        print("No machine available.")


# Individual machine reports
print("\nMACHINE REPORTS")

for machine in fleet:
    print(machine.status())


# Calculate total plant production
plant_total = sum(
    machine.total_parts for machine in fleet
)

print("\nTotal Plant Production:", plant_total)


# Identify busiest machine
busiest = max(
    fleet,
    key=lambda machine: machine.total_parts
)

print("Busiest Machine:", busiest.name)
print("Production:", busiest.total_parts)

        }
