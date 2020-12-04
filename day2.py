from collections import Counter

def test_check_password():
    db = {'1-3 a': 'abcde',
              '1-3 b': 'cdefg',
              '2-9 c': 'ccccccccc'}

    valid_count = 0
    for policy, password in db.items():
        if check_password(policy, password):
            valid_count += 1

    assert valid_count == 2


def check_password(policy, password) -> bool:
    char_count, c = policy.split(" ")
    min_cc, max_cc = char_count.split("-")
    cc = Counter(password)[c]
    if int(min_cc) <= cc <= int(max_cc):
        return True
    else:
        return False


if __name__ == "__main__":
    test_check_password()
    valid_passwords = 0
    with open("day2.txt") as raw_entries:
        for raw_line in raw_entries:
            policy, password = raw_line.strip().split(": ")
            if check_password(policy, password):
                valid_passwords += 1


    print(f"{valid_passwords} valid passwords")