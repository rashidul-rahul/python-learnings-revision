def insertion_sort(data):
    data_len = len(data)
    for i in range(1, data_len):
        item = data[i]
        j = i - 1
        while j >= 0 and data[j] > item:
            print(j)
            data[j+1] = data[j]
            j = j-1

        data[j+1] = item
        print("----")

    return data


print(insertion_sort([5,4,3,2,1]))
print("second one")
print(insertion_sort([1,2,3,4,5]))

"""
1. list with nth time numbers need to sort with intertion
2. check an list item with previous items to find the best place to fit and move right every previous item before we found the best place
3. update the value on fit place with the item
4. if the array range is over return the sorted list or return to number 2 
"""
