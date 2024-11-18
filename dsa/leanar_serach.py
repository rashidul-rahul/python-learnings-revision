def leaner_search(full_data, number):
    n = len(full_data)
    for i in range(n):
        if full_data[i] == number:
            return i
    return -1


def test_leaner_search():
    test_cases = [
        {
            "name": "Simple case 1",
            "input": [[3,5,1,6,8], 6],
            "expected": 3
        },
        {
            "name": "Simple case 1",
            "input": [[3,5,1,6,8], 4],
            "expected": -1
        }
    ]

    for case in test_cases:
        assert case["expected"] == leaner_search(case["input"][0], case["input"][1]), case["name"]
