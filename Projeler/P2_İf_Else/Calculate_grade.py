# Kullanıcının notunu alarak harf notunu hesaplayın

def calculate_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    elif 0 <= score <= 59:
        return 'F'
    else:
        return "Geçersiz not"

score = float(input("Notunuzu girin: "))
print("Harf Notunuz: " + calculate_grade(score))