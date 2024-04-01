number: str = input('Numéro de carte: ')
number = number.replace(' ', '')

even: list[str] = [char for char in number[1:len(number):2]]
odd: list[str] = [char for char in number[0:len(number):2]]

print(f'Nombres de rang pair  : {even}')
print(f'Nombres de rang impair: {odd}')
