# Kullanıcının girdiği bir kelimenin palindrom olup olmadığını kontrol eden fonksiyon
def is_palindrom(word):
    word = word.lower()
    is_palidrom = True
    liste = []
    for i in word:
        liste.append(i)
               
    temp = len(liste)-1
    print(liste)
    for j in liste:
        if j != liste[temp] :
            is_palidrom = False
        temp = temp - 1
    
    return is_palidrom

i = 0
while i < 5:
    word= input("Kelime giriniz: ")
    
    if is_palindrom(word):
        print(f"{word} -> Polindrom")
    else:
        print(f"{word} -> Polindrom Değil !!")
    i += 1