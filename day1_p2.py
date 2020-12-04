from typing import Tuple, List


def test_find_entries_that_sum_to():
    test_list = [1721, 979, 366, 299, 675, 1456]
    e1, e2, e3 = find_entries_that_sum_to(test_list, sum_to=2020)
    assert e1*e2*e3 == 241861950


def find_entries_that_sum_to(entries:List, sum_to:int=2020) -> Tuple:
    """
    Find 3 entries that sum to `sum_to`
    """
    for i, e1 in enumerate(entries):
        for j, e2 in enumerate(entries[i:]):
            expected_e3 = sum_to - e1 - e2
            if expected_e3 in entries[i+j:]:
                return e1, e2, expected_e3

    return None, None, None


if __name__ == "__main__":
    #test_find_entries_that_sum_to()
    with open("day1.txt") as raw_entries:
        entries = [int(e) for e in raw_entries.readlines()]
        e1, e2, e3 = find_entries_that_sum_to(entries)
        if e1 and e2 and e3:
            print(e1*e2*e3)
        else:
            print("Failed to find correct entries.")