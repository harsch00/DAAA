while True:
    string = input("Enter the string: ")
    if not string.isalpha():
        print("pls enter only alphabets")
    else:
        break


def permutations(string):
    length = len(string)

    if length <= 1:
        return [string]
    
    result=[] 

    for i in range(length):
        remaining = string[:i] + string[i+1:]

        for j in permutations(remaining):
            result.append(string[i] + j)

    return result
    

print(permutations(string))
