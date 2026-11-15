line = "P201, 24.97, NIGHT"

code, dia, shift = line.split(",")

code = code.strip()
dia = float(dia.strip())
shift = shift.strip()

print("Part Code =", code)
print("Diameter =", dia)
print("Shift =", shift)

print("After adding 0.01 =", dia + 0.01)
