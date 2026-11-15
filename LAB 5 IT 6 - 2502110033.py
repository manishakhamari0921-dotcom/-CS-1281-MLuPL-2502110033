day_logs = [
    "P201, 24.98, DAY",
    "P202, 25.15, DAY",
    "P203, 24.85, DAY",
    "P204, 25.02, DAY",
    "P205, 25.20, DAY"
]

night_logs = [
    "P201, 25.15, NIGHT",
    "P202, 24.99, NIGHT",
    "P206, 24.80, NIGHT",
    "P207, 25.03, NIGHT",
    "P208, 25.01, NIGHT"
]

def process_shift(logs):
    accepted = 0
    scrap_codes = set()

    for line in logs:
        code, dia, shift = line.split(",")

        code = code.strip()
        dia = float(dia.strip())

        if 24.95 <= dia <= 25.05:
            accepted += 1

        elif dia < 24.90 or dia > 25.10:
            scrap_codes.add(code)

    rate = (accepted / len(logs)) * 100

    return rate, scrap_codes

day_rate, day_scrap = process_shift(day_logs)
night_rate, night_scrap = process_shift(night_logs)

print("DAY SHIFT ACCEPT RATE:", day_rate, "%")
print("NIGHT SHIFT ACCEPT RATE:", night_rate, "%")

print("\nCOMMON SCRAP CODES:")
print(day_scrap.intersection(night_scrap))

print("\nDAY ONLY SCRAP:")
print(day_scrap.difference(night_scrap))

print("\nNIGHT ONLY SCRAP:")
print(night_scrap.difference(day_scrap))
