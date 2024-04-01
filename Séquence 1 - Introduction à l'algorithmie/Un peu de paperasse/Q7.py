number: str = input('Numéro de carte: ')
number = number.replace(' ', '')
print()

even: list[str] = [char for char in number[1:len(number):2]]
odd: list[str] = [char for char in number[0:len(number):2]]

print(f'Nombres de rang pair  : {even}')
print(f'Nombres de rang impair: {odd}')
print()

even_sum: int = 0

for digit in even:
    even_sum += int(digit)

print(f'Somme des nombres de rang pair  : {even_sum}')

odd_sum: int = 0

for digit in odd:
    digit = int(digit)

    if digit >= 5:
        odd_sum += 1 + (2 * digit - 10)
    else:
        odd_sum += 2*digit

print(f'Somme des nombres de rang impair: {odd_sum}')
print()

print(f'Validité: {(even_sum + odd_sum) % 10 == 0}')
