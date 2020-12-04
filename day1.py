from typing import Tuple, List


def test_find_entries_that_sum_to():
    test_list = [1721, 979, 366, 299, 675, 1456]
    e1, e2 = find_entries_that_sum_to(test_list, sum_to=2020)
    assert e1*e2 == 514579


def find_entries_that_sum_to(entries:List, sum_to:int=2020) -> Tuple:
    """
    """
    for i, e1 in enumerate(entries):
        expected_e2 = sum_to - e1
        if expected_e2 in entries[i:]:
            return e1, expected_e2

    return None, None


if __name__ == "__main__":
    #test_find_entries_that_sum_to()
    with open("day1.txt") as raw_entries:
        entries = [int(e) for e in raw_entries.readlines()]
        e1, e2 = find_entries_that_sum_to(entries)
        if e1 and e2:
            print(e1*e2)
        else:
            print("Failed to find correct entries.")