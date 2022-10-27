from random import *
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

def check_yes_no(word):
    while True:
        if word.lower() == 'да':
            return True
        elif word.lower() == 'нет':
            return False
        else:
            word = input('Ответ неправильный, повторите: да/нет -->')

count_passwords = int(input('Введите количество паролей для генерации: '))
len_one_passwodr = int(input('Длина одного пароля:'))
need_digits = check_yes_no(input('Включать ли цифры 0123456789? да/нет -->'))
need_upper = check_yes_no(input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? да/нет -->'))
need_lower = check_yes_no(input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? да/нет -->'))
need_punctuation = check_yes_no(input('Включать ли символы !#$%&*+-=?@^_  ? да/нет -->'))
need_no_symbols = check_yes_no(input('Исключать ли неоднозначные символы il1Lo0O  ? да/нет -->'))

list_chars = []
temp_chars = ''

if need_digits:
    temp_chars += digits
if need_upper:
    temp_chars += uppercase_letters
if need_lower:
    temp_chars += lowercase_letters
if need_punctuation:
    temp_chars += punctuation

for _ in range(count_passwords):
    chars = ''
    lenth = len_one_passwodr
    while lenth:
        temp = choice(temp_chars)
        if need_no_symbols:
            if temp in 'il1Lo0O':
                continue
        chars += temp
        lenth -= 1
    list_chars.append(chars)

print()
print(*list_chars, sep='\n')
