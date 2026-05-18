import random
import threading
import time

size = 1_000_000
threads_count = 4

elements = []
threads = []
result = [size, 0]


def minMax(array):
    min = size
    max = 0
    for i in array:
        if i < min:
            min = i
        if i > max:
            max = i

    result[0] = min
    result[1] = max


for i in range(size):
    elements.append(random.randint(0, size))

for i in range(threads_count):
    start = size * (i // threads_count)
    end = size * ((i + 1) // threads_count) - 1
    threads.append(threading.Thread(target=minMax, args=(elements[start:end],)))

print("Min/Max Search without Threading")
start_time = time.time()
minMax(elements)
end_time = time.time()
print(
    f"Minimum: {result[0]}\nMaximum: {result[1]}\nTime Required: {end_time - start_time}\n\n"
)

print("Min/Max with Threading")
start_time = time.time()

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

end_time = time.time()
print(
    f"Minimum: {result[0]}\nMaximum: {result[1]}\nTime Required: {end_time - start_time}\n\n"
)
