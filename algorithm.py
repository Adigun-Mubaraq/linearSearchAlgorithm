def linearSearch(myarray, target):
    for index in range(len(myarray)):
        if myarray[index] == target:
            return index
    return -1


fruits = [1, 2, 5, 7, 10]
key = 2
index = linearSearch(fruits, key)
if (index == -1):
    print("Element is not found")
else:
    print("Your Search Index is "+str(index))
