# Kullanıcının yaşına göre hangi yaş grubunda olduğunu bulan program 

def determine_age_group(age):

    if 0 <= age <= 12:
        return 'Çocuk'
    elif 13 <= age <= 19:
        return 'Genç'
    elif 20 <= age <= 59:
        return 'Yetişkin'
    elif 60 <= age <= 100:
        return 'Yaşlı'
    else:
        return "Geçersiz yaş"
 
age = int(input("Enter your age: "))
print(f"Yaşınıza göre grubunuz: {determine_age_group(age)}" )