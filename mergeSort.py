import threading

while True:
    try:
        elements = [int(x) for x in input("Enter array elements space separated: ").split(' ')]
        break
    except ValueError:
        print("Pls enter integer values!")

def worker(side, data, results):
    results[side] = mergeSort(data)

def mergeSort(array):
    length = len(array)

    if length == 1:
        return array
    
    middle = length//2

    left = array[:middle]
    right = array[middle:]
    
    results = [None, None, []]

    t_left = threading.Thread(target=worker, args=(0, left, results))
    t_right = threading.Thread(target=worker, args=(1, right, results))

    t_left.start()
    t_right.start()

    t_left.join()
    t_right.join()

    i=j=0
    while i < len(results[0]) and j < len(results[1]):
        if results[0][i] < results[1][j]:
            results[2].append(results[0][i])
            i+=1
        else:
            results[2].append(results[1][j])
            j+=1

    results[2].extend(results[0][i:])
    results[2].extend(results[1][j:])

    return results[2]
    

print(mergeSort(elements))
