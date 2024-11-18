def selection_sort(data):
    data_len = len(data)
    for i in range(data_len):
        for j in range(i, data_len):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]

    return data


def test_sorting():
    test_cases = [
        {
            "name": "Simple case 1",
            "input": [10, 2, 8, 7, 3],
            "expect": [2, 3, 7, 8, 10]
        }
    ]

    for case in test_cases:
        assert case["expect"] == selection_sort(case["input"]), case["name"]
