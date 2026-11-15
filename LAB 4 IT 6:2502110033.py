import random

attempts = 0
good = 0
target = 5
maximum = 500

while good != target and attempts < maximum:

    d = round(random.uniform(24.90, 25.10), 2)
    attempts += 1

    print("Part", attempts, ":", d)

    if 24.95 <= d <= 25.05:
        print("ACCEPT")
        good += 1
    elif 24.90 <= d <= 25.10:
        print("REWORK")
        good = 0
    else:
        print("SCRAP")
        good = 0

print("\nPRODUCTION REPORT")
print("Total attempts:", attempts)
print("Consecutive good parts:", good)

if good == target:
    print("SUCCESS - TARGET COMPLETED")
else:
    print("SAFETY LIMIT REACHED")
