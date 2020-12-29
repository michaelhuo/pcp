def find_sum_of_two(A, val):
    if not A:
        return False
    size = len(A)
    if size < 2:
        return False
    hash_set = set()
    for n in A:
        m = val - n
        if m in hash_set:
            return True
        hash_set.add(n)
    return False;
