from random import randint as rand

answer: str = input('Entrez un nombre (1-500): ')

while not answer.isdigit() or int(answer) > 500:
    print('Entrée invalide')
    answer = input('Entrez un nombre (1-500): ')

n: int = int(answer)

generated: list[int] = []

while len(generated) < n:
    number: int = rand(0, 500)

    while number in generated:
        number = rand(0, 500)

    generated.append(number)

print('\n', generated)
