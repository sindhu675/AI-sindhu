# Vacuum Cleaner Problem

# A = Left room, B = Right room
A = "Dirty"
B = "Dirty"

location = "A"

print("Initial State:")
print("Room A:", A, "Room B:", B)

# Clean Room A
if location == "A":
    if A == "Dirty":
        print("Vacuum cleaning Room A")
        A = "Clean"
    location = "B"

# Clean Room B
if location == "B":
    if B == "Dirty":
        print("Vacuum cleaning Room B")
        B = "Clean"

print("Final State:")
print("Room A:", A, "Room B:", B)
