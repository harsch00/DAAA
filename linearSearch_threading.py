import random
import threading
import time

size = 1_000_000
threads_count = 4
elements = []
threads = []

stop_signal = False
signal_lock = threading.Lock()

def linearSearch(array, target):
    global stop_signal

    for element in array:
        with signal_lock:
            if stop_signal:
                return

        if element == target:
            with signal_lock:
                if not stop_signal:
                    print(f"Element {element} found at index {elements.index(element)}")
                    stop_signal = True
            return

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
