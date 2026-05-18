import threading

def worker(side, data, results):
    results[side] = quickSort(data)


def quickSort(array):
    if len(array) <= 1:
        return array

    pivot = array.pop()
    lesser = []
    greater = []

    for element in array:
        if element <= pivot:
            lesser.append(element)
        else:
            greater.append(element)

    results = [None, None]
    t_lesser = threading.Thread(target=worker, args=(0, lesser, results))
    t_greater = threading.Thread(target=worker, args=(1, greater, results))

    t_lesser.start()
    t_greater.start()

    t_lesser.join()
    t_greater.join()

    return results[0] + [pivot] + results[1]

if __name__ == "__main__":
    while True:
        try:
            elements = [int(i) for i in input("Enter elements space separated: ").split(' ')]
            break
        except ValueError:
            print("Pls enter integer values separated by space!")

    print(quickSort(elements))
