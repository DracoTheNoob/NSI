def caesar(text: str, offset: int) -> str:
    assert -25 <= offset <= 25 and offset != 0

    alphabet: str = 'abcdefghijklmnopqrstuvwxyz'
    result: str = ''

    for character in text:
        if character not in alphabet:
            result += character
        else:
            index: int = list(alphabet).index(character)
            index += offset

            while index < 0:
                index += 26

            while index > 25:
                index -= 26

            result += alphabet[index]

    return result
