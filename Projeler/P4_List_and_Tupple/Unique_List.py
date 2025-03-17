# Bir liste içindeki tekrar eden elemanları kaldıran program 

word_list = []
unique_list = []
def remove_duplicate(liste):
    return list(dict.fromkeys(liste))

i = 0
while i < 5:
    word = input("Enter the word: ")
    word_list.append(word)
    i = i + 1
unique_list = remove_duplicate(word_list)
print(unique_list)