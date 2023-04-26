def is_anagram(first_string, second_string):
    string_1 = quick_sort(first_string.lower())
    string_2 = quick_sort(second_string.lower())

    first_string_sorted = "".join(string_1)
    second_string_sorted = "".join(string_2)
    is_anagram = first_string_sorted == second_string_sorted
    
    return (first_string_sorted, second_string_sorted, is_anagram)


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
