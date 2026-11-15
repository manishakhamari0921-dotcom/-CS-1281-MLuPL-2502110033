
# IT12 - The Drawing (Version 2)

class IndustrialMachine:

    def __init__(self, machine_id, capacity, rpm):
        self.machine_id = machine_id
        self.capacity = capacity
        self.rpm = rpm
        self.production = 0

    # Display machine nameplate
    def __str__(self):
        return (
            f"Machine ID: {self.machine_id}\n"
            f"Capacity: {self.capacity} units/hour\n"
            f"Rated RPM: {self.rpm}\n"
            f"Production: {self.production} units"
        )

    # Produce components
    def produce(self, hours):
        quantity = self.capacity * hours
        self.production += quantity
        return quantity


# Create two machine objects
m1 = IndustrialMachine("IM-101", 20, 1500)
m2 = IndustrialMachine("IM-102", 30, 2000)

# Operate both machines
print("Machine 1 produced:", m1.produce(3))
print("Machine 2 produced:", m2.produce(2))

# Display nameplates
print("\nMACHINE DETAILS")
print(m1)

print()
print(m2)

# Check independent states
print("\nINDEPENDENCE TEST")

m1.produce(1)

print("Machine 1 production:", m1.production)
print("Machine 2 production:", m2.production)
