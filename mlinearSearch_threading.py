import random
import threading
import time

size = 1_000_000
threads_count = 4
elements = []
threads = []


def linearSearch(array, target):
    for element in elements:
        if element == target:
            print(f"Element {element} found at index {elements.index(element)}")


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

# making thread objects
for i in range(threads_count):
    start = int(size * (i / threads_count))
    end = int(size * ((i + 1) / threads_count) - 1)
    threads.append(threading.Thread(target=linearSearch, args=(elements[start:end], target,)))

# running threads
start_time = time.time()
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
end_time = time.time()
