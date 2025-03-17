# •Kullanıcıdan iki sayı alarak bu sayıların toplamını, farkını, çarpımını ve bölümünü ekrana yazdırma

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

toplam = number1 + number2
fark   = number1 - number2
carpim = number1 * number2
bolum  = number1 / number2

print(f"Toplam: {toplam}")
print(f"Fark: {fark}")
print(f"Çarpım: {carpim}")
print(f"Bölüm: {bolum}")