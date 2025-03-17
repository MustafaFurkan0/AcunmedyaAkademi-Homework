# Kullanıcıdan aldığı kelimeleri bir listeye ekleyerek ters sıralayan program 

list = []
reverse_list = []
i = 0
while i < 5:
    word = input("Enter the word: ")
    list.append(word)
    i = i + 1

for i in range(5,0,-1):
    temp = list[i-1]
    reverse_list.append(temp)
    i -= 1

# reverse_list = list[::-1]
print(reverse_list)