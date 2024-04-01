def ask_number(text: str, length: int) -> str:
    answer: str = input(text)

    while len(answer) != length:
        answer = input(text)

    return answer


gender: str = ask_number('sexe: ', 1)
year: str = ask_number('année de naissance (deux derniers chiffres): ', 2)
month: str = ask_number('mois de naissance: ', 2)
place: str = ask_number('lieu de naissance: ', 5)
order: str = ask_number('numéro d\'ordre: ', 3)
