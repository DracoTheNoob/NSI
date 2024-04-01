for code in ['298070312000570', '104097511101260', '207101305505388']:
    number: str = code
    split: list[str] = [number[:len(number)-2], number[len(number)-2:]]

    control_key: int = 97 - (int(split[0]) % 97)

    print(f'{code} -> {str(control_key) == split[1]}')
