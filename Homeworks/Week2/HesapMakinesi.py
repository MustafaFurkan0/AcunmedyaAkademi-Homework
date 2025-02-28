def hesapMakinesi(number1,number2,operation):
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '*':
        return number1 * number2
    elif operation == '/':
        if number2 == 0:
            return "Bölme işlemi için ikinci sayı 0 olamaz!"
        return number1 / number2
    else:
        return "Geçersiz operatör işlemi girdiniz. Lütfen +, -, * veya / kullanın.!!!"
    
number1 = float(input("Birinci sayıyı giriniz: "))
number2 = float(input("ikinci sayıyı giriniz : "))
operation = input("Yapmak istegiğiniz işlemin sembolünü giriniz (+, -, *, /): ")

print(f"{number1} {operation} {number2} = {hesapMakinesi(number1, number2, operation)}")
