def grid(size: int) -> None:
    assert 3 <= size <= 20

    base: str = '+' + '-'*(size-2) + '+'
    content: str = base + '\n'

    for i in range(size-2):
        content += '|' + '#' * (size-2-i-1) + ' ' + '#'*i + '|\n'

    content += base

    print(content)
