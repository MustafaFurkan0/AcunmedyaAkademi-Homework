# Girilen iki sayının toplamını, farkını, çarpımını ve bölümünü bulan hesap makinesi fonksiyonu
def calculator(number1, number2):
    print("Total         :", (number1 + number2))
    print("Difference    :", (number1 - number2))
    print("Multiplication:", (number1 * number2))
    if number2 != 0 :
        print("Division      :", (number1 / number2))
    else:
        print("Tanımsız..(Bölme için number2 sıfır olamaz)")
  
number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))  

calculator(number1, number2)