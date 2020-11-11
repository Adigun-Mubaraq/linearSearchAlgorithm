def linearSearch(myarray, target):
    for index in range(len(myarray)):
        if myarray[index] == target:
            return index
    return -1


fruits = [1, 2, 5, 7, 10]
key = 5
print("The index of your search is " +str(linearSearch(fruits, key)))
