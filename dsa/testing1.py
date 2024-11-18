def average(L):
    if not L:
        return None
    if not isinstance(L, list):
        return None
    return sum(L)/len(L)


def test_average():
    test_cases = [
        {
            "name": "Simple case 1",
            "input": [1,2,3],
            "expected": 2.0
        },
        {
            "name": "Simple case 2",
            "input": [100],
            "expected": 100.0
        },
        {
            "name": "Simple case 2",
            "input": [],
            "expected": None
        },
        {
            "name": "Simple case 3",
            "input": "sdf",
            "expected": None
        }
    ]

    for case in test_cases:
        assert case["expected"] == average(case["input"]), case["name"]
