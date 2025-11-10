text = input("Введите текст: ")
word = input("Введите слово для поиска: ")
words = text.lower().split()
word_lower = word.lower()
count = words.count(word_lower)

print(f"Текст: '{text}'")
print(f"Искомое слово: '{word}'")
print(f"Количество вхождений: {count}")