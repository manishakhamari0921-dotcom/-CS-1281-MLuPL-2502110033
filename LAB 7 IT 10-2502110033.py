
# IT10 - The Guarded Machine (Version 2)

class GuardedMachine:

    def __init__(self, machine_name, rpm_limit):
        self.__machine_name = machine_name
        self.__rpm_limit = rpm_limit
        self.__total_parts = 0
        self.__active = False

    # Validated operating method
    def run_machine(self, rpm, parts):

        if not isinstance(rpm, (int, float)):
            return "Error: RPM must be numeric."

        if not isinstance(parts, int) or isinstance(parts, bool):
            return "Error: Parts must be an integer."

        if rpm < 500 or rpm > self.__rpm_limit:
            return "Warning: RPM limit exceeded or too low."

        if parts <= 0:
            return "Error: Invalid production quantity."

        self.__active = True
        self.__total_parts += parts
        self.__active = False

        return "Machine operated successfully."

    # Getter method
    def status(self):
        return (
            f"Machine: {self.__machine_name}\n"
            f"RPM Limit: {self.__rpm_limit}\n"
            f"Total Parts: {self.__total_parts}\n"
            f"Active: {self.__active}"
        )


# Create machine
machine = GuardedMachine("Hydraulic Press", 2500)

# Test valid and invalid commands
print(machine.run_machine(1200, 50))
print(machine.run_machine(3000, 20))
print(machine.run_machine(1500, -10))

# Display status
print("\nMACHINE STATUS")
print(machine.status())

# Demonstrate bypass
machine._GuardedMachine__rpm_limit = 4000

print("\nAfter bypassing the guard:")
print(machine.run_machine(3500, 30))
print(machine.status())
