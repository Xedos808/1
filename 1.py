def main(number, words_string):
    words = words_string.split('; ')
    filtered_words = [word.upper() for word in words if len(word) % number != 0]
    result = ' - '.join(filtered_words)
    return result


number = int(input("Введите число: "))
string = input("Введите строку слов: ")
print(main(number, string))