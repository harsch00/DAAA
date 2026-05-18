import random
import time

size = 1_000_000
elements = []

# input and validation
while True:
    try:
        target = int(input("Enter target: "))
        break
    except ValueError:
        print("\nNot an integer!\n")

# random filling
for i in range(size):
    elements.append(random.randint(0, size))

# linear search
start_time = time.time()
for i in range(size):
    if elements[i] == target:
        print(f"Element {elements[i]} found at index {i}")
        break
end_time = time.time()

print(f"Time Required: {end_time - start_time}")
