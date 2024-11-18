"""
Optimize bubble sort
"""


def bubble_sort(data):
    data_len = len(data)
    for i in range(data_len):
        swapped = False
        if i > data_len:
            return data
        for j in range(0, data_len - i - 1):
            print(j)
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
        if not swapped:
            break

    return data


a = [1, 2, 4, 3, 5]
print(bubble_sort(a))
