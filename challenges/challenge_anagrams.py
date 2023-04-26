def is_anagram(first_string, second_string):
    first_string_sorted = quick_sort(list(first_string.lower()))
    second_string_sorted = quick_sort(list(second_string.lower()))

    return first_string_sorted == second_string_sorted


def quick_sort(string):
    if len(string) <= 1:
        return string

    pivo = string[0]
    menores = []
    maiores = []

    for letter in string[1:]:
        if letter <= pivo:
            menores.append(letter)
        else:
            maiores.append(letter)

        return quick_sort(menores) + [pivo] + quick_sort(maiores)
