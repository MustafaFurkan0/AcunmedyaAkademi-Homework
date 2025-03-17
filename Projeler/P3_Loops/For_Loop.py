# 1’den 100’e kadar olan sayıları ekrana yazdırın.
def print_numbers():
    for i in range(1, 101):
        print(i, end=" ")

# 1’den 100’e kadar sadece çift sayıları ekrana yazdıran bir program yazın.
def print_even_numbers():
    for i in range(1,101):
        if i % 2 == 0:
            print(i ,end = " ")
         
print_numbers()
print("\n-----------------------------------------------------")
print_even_numbers()