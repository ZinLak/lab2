import re

def process_lexeme(lexeme):
    if not lexeme or len(lexeme) > max_buffer_len: return
    else:
        number = int(lexeme)
        if str(number).startswith('11'):
            process_number(number)

def process_number(number):
    global max_value; global lexeme_str; e = 2
    digits = [int(digit) for digit in str(number)]
    start_digits = "".join(map(str, digits))
    swapped_digits = ''
    for i in range(0, len(digits)-1, 2):
        if digits[i] == digits[i+1]:
            swapped_digits += str(digits[i]) + str(digits[i+1])
            if len(digits)-1 <= i+1:
                if all(elem == digits[0] for elem in digits):
                    swapped_digits += str(digits[-1])
        else:
            swapped_digits += str(digits[i+1]) + '0'*e + str(digits[i])
            digits[i], digits[i+1] = digits[i+1], digits[i]
    if len(digits) % 2 == 1:
        swapped_digits += str(digits[-1])
    swapped_digits = int(swapped_digits)
    if max_value < swapped_digits:
        max_value = swapped_digits
        lexeme_str = start_digits

def convert_number_to_words(number):
    d_db = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}
    words = [d_db[digit] for digit in str(number)]
    result = ' '.join(words)
    return result

max_value = float('-inf')
work_buffer = ''
buffer_len = 1
max_buffer_len = 100
razd = [' ', ',', ';', ':', '?', '!', '&', '*', '.', '\n']

with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    lexemes = re.findall(r'\b\d+\b', text)
    for lexeme in lexemes:
        process_lexeme(lexeme)

if max_value != float('-inf'): print('\nИсходное число:', lexeme_str, '\nОбработанное число:', max_value,'\nОтвет:', convert_number_to_words(max_value))
else: print('\nЛексем в файле не осталось или лексемы не удовлетворяют условию (в данном случае проверьте файл и(или) замените text.txt на другой). \nПрограмма завершает работу.')