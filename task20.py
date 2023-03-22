# Задача 20 про Скрабл
word = input("Введите слово на русском или английском языке: ").upper()
my_dict = {'AEIOULNSTR': 1, 'DG': 2, 'BCMP': 3, 'FHVWY': 4, 'K': 5, 'JX': 8, 'QZ': 10,
           'АВЕИНОРСТ': 1, 'ДКЛМПУ': 2, 'БГЁЬЯ': 3, 'ЙЫ': 4, 'ЖЗХЦЧ': 5, 'ШЭЮ': 8, 'ФЩЪ': 10}

sum = 0
for letter in word:
    for key, value in my_dict.items():
        if letter in key:
            sum += int(value)
print(f"Количество баллов за слово: {sum}")
