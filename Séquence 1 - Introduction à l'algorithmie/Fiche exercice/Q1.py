def maximum(n1: int, n2: int, n3: int) -> int:
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2

    return n3
