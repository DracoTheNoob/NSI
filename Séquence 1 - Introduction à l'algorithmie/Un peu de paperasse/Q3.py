number: str = input('Numéro de sécurité sociale: ')
split: list[str] = [number[:len(number)-2], number[len(number)-2:]]

control_key: int = 97 - (int(split[0]) % 97)

print(str(control_key) == split[1])
