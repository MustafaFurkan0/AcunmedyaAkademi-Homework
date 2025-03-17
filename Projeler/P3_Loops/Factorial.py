# Kullanıcıdan bir sayı alıp, bu sayının faktöriyelini hesaplayan program 
def factorial(number):
    factorial_num = 1
    if number < 0:
        return "Negatif sayıların faktöriyeli hesaplanamaz !!!"
    else:
        while number >= 0:
            if number == 0:
                factorial_num = factorial_num * 1
            elif number == 1:
                factorial_num = factorial_num * 1
            else:
                factorial_num = factorial_num * number
            number = number - 1
        return factorial_num
        
number = int(input("Enter number: "))
print(f"{number}! = {factorial(number)}")