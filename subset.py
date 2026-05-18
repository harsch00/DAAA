from quickSort import quickSort

while True:
    try:
        raw_set = [int(x) for x in input("Enter set elements space separated: ").split(' ')]
        sum = int(input("Enter the intended sum value: "))
        break
    except ValueError:
        print("Pls enter only integer values!")

set = quickSort(raw_set)
del raw_set

def subsets(arr, target):
    result = []

    def backtrack(index, current_sum, current_subset):
        if current_sum == target:
            result.append(list(current_subset))
            return

        if current_sum > target or index >= len(arr):
            return

        current_subset.append(arr[index])
        backtrack(index + 1, current_sum + arr[index], current_subset)
        current_subset.pop()

        backtrack(index + 1, current_sum, current_subset)

    backtrack(0, 0, [])
    return result

print(subsets(set, sum))
