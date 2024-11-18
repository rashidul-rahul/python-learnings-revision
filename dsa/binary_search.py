def binary_search(num_list, num):
    total_len = len(num_list)
    start_indx = 0
    end_indx = total_len - 1

    if start_indx == end_indx:
        if num_list[0] == num:
            return 0
        else:
            return -1

    while start_indx <= end_indx:
        mid = (end_indx + start_indx) // 2  # integer division
        if num_list[mid] == num:
            return mid
        if num_list[mid] < num:
            start_indx = mid + 1
        else:
            end_indx = mid - 1

    return -1


def test_binary_search():
    test_cases = [
        {
            "name": "Simple test case 1",
            "value": [[2,6,7,8,10,15,18,20,35,67,77,80], 20],
            "expected": 7
        },
        {
            "name": "Simple test case 1",
            "value": [[2,6,7,8,10,15,18,20,35,67,77,80], 78],
            "expected": -1
        },
    ]

    for case in test_cases:
        assert case["expected"] == binary_search(case["value"][0], case["value"][1]), case["name"]
