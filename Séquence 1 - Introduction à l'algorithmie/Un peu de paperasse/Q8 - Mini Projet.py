from random import randint as rand

plays: list[str] = ['pierre', 'feuille', 'ciseaux', 'lézard', 'spock']
wins: dict = {
    'pierre': ['ciseaux', 'lézard'],
    'feuille': ['pierre', 'spock'],
    'ciseaux': ['feuille', 'lézard'],
    'lézard': ['feuille', 'spock'],
    'spock': ['ciseaux', 'pierre']
}

player: str = input(f'Choisir parmis {plays}: ').lower()

while player not in plays:
    print('Entrée invalide')
    player = input(f'Choisir parmis {plays}: ').lower()

print()
print(f'Joueur: {player}')

computer = plays[rand(0, len(plays)-1)]
print(f'Ordinateur: {computer}\n')

if player == computer:
    print('Égalité')
elif computer in wins[player]:
    print('Le joueur gagne')
else:
    print('L\'ordinateur gagne')
