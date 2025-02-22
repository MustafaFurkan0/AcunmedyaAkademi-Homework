# reference type vs  value type (immutable - mutable)
a = 1
b = a
b += 10
print(a)
print(b)

list1= ["Furkan", "Emine", "Mustafa"]
list2= list1

list2.append("Emirhan")

print(list1)
print(list2)


# döngüler - iterasyos (iteration)

for i in range(5): # indentation, indent (boşluklarla )
    print(i)
    print("Merhaba")
print("For bitti")

for i in range(5,10):
    print(i)

for i in range(5,56,10):
    print(i)

print("*********")

for i in range(0,100):
    if i == 50:
        break #bu iterasyonda bu satırdan aşağısını çalıştırmadan döngüyü bitir.
    print(i)
    
for i in range(0,100):
    if i == 50:
        continue #bu iterasyonda bu satırdan aşağısını çalıştırmadan sonraki iterasyona geç.
    print(i)

for student in list1:
    if student == "Mustafa":
        continue
    print(student)

# while
# koşullarla çalışır
# sonsuz döngü tehlikesi
i = 5
while i < 10:
    i += 1
    if i == 7:
        continue
    print(i)

# şart - koşul blokları
age = 18
# kural1 => tek çıktı !!
# kural2 => yukarıdan aşağıya ilk doğru koşul
if age > 18:
    print("Giriş yapabilirsiniz")
elif age == 18:
    print("Ay kontrolü yapılıyor...")
else:
    print("Giriş yapamazsınız..")
# 