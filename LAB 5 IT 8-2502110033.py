logs = [
    "P201, 24.98, DAY",
    "P202, 25.02, DAY",
    "P203, 24.85, DAY",
    "P204, 25.06, DAY",
    "P205, 24.99, DAY",
    "P206, 25.15, DAY",
    "P207, 24.92, DAY",
    "P208, 25.04, DAY",
    "P209, 24.80, DAY",
    "P210, 25.00, DAY"
]

accepted = []
rework = []
scrap = []
scrap_codes = []

def classify(d):
    if 24.95 <= d <= 25.05:
        return "ACCEPT"
    elif 24.90 <= d <= 25.10:
        return "REWORK"
    else:
        return "SCRAP"

for line in logs:
    code, dia, shift = line.split(",")

    code = code.strip()
    dia = float(dia.strip())

    result = classify(dia)

    if result == "ACCEPT":
        accepted.append(dia)

    elif result == "REWORK":
        rework.append(dia)

    else:
        scrap.append(dia)
        scrap_codes.append(code)

print("ACCEPTED:", accepted)
print("REWORK:", rework)
print("SCRAP:", scrap)

print("\nTOTAL COUNTS")
print("Accepted:", len(accepted))
print("Rework:", len(rework))
print("Scrap:", len(scrap))

if accepted:
    print("Accepted Average:",
          round(sum(accepted) / len(accepted), 2))
else:
    print("No accepted parts")

print("Scrapped Part Codes:", scrap_codes)
