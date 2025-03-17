# Kullanıcıdan 5 adet sayı alarak bir listeye ekleyen ve bu listenin 
# toplamını, ortalamasını, en büyük ve en küçük elemanını bulan program

list = []
i = 0
sum = 0
while i < 5:
    number = int(input("Enter number: "))
    list.append(number)
    i = i +1

for l1 in list:
    sum = sum + l1

average = sum / len(list)
max_number = max(list)
min_number = min(list) 
print("Toplam       :", sum)
print("Ortalama     :", average)
print("En büyük sayı:", max_number)
print("En küçük sayı:", min_number)