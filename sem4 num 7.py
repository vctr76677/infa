import string
file_path = '/usr/share/licenses/python/LICENSE'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
for p in string.punctuation:
    text = text.replace(p, ' ')
words = text.lower().split()

word_dict = {}
for w in words:
    word_dict[w] = word_dict.get(w, 0) + 1
dict_copy = word_dict.copy()
top_10_words = []
for _ in range(min(10, len(dict_copy))):
    max_word = None
    max_count = -1
    for word, count in dict_copy.items():
        if count > max_count:
            max_count = count
            max_word = word       
    if max_word is not None:
        top_10_words.append((max_word, max_count))
        del dict_copy[max_word]
print("10 самых часто употребляемых слов:")
for word, count in top_10_words:
    print(f"'{word}': {count} раз(а)")