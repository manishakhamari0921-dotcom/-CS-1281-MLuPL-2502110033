total = int(input("Enter total parts: "))
size = int(input("Enter box size: "))

boxes, loose = divmod(total, size)

print("Number of boxes:", boxes)
print("Remaining parts:", loose)

audit = (boxes * size) + loose

print("Audit result:", audit == total)
