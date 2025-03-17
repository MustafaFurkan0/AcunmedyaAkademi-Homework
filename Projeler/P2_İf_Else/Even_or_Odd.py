# Kullanıcının girdiği bir sayının tek mi çift mi olduğunu bulan program
def even_num(number):
    if number % 2 == 0:
        return f"{number}: Çift sayıdır !!!"
    return f"{number}: Tek sayıdır !!!"

number = int(input("Enter number: "))
print(even_num(number))