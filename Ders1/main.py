print("Hello word")

####### değişkenler

name = "Mustafa" #string, str 
print(name)
# python=> type-safe olmayan dildir.
age = 22 # integer, int
print(age)
print(type(age))
age = "abc"
print(age)
print(type(age))
#

####### operatörler

### matematiksel (aritmatik) operatörler
print(1+1)
print(5-2)
print(5*5)
print(25/5)  # bölme işlemi
print(29//5) # tam bölme işlemi
print(38%5)  # mod alma işlemi
print(5**3)  # üs alma işelmi
#

### atama operatörleri
a = "abc"
number= 5
print(number)

number +=5 # number = number + 5
number -=2
print(number)
number /= 4 #float
number *= 10
print(number)
#

### karşılaştırma operatörleri
is_valid = True #bool, boolean
print(1 == 1)
print(1 != 1)
print(10 > 5)
print(10 >= 10)
#

### mantıksal operatörler, => and,or,not

# and => iki tarafında true olması dışındaki tüm durumları false yapar
print(1 == 1 and 1 == 2) # true & false  => false
print(1 == 1 and 10 > 5) # true & true   => true
print( 1 != 1 and 5 > 10)# false & false => false

# or -> iki tarafında false olması dışındaki tüm durumları true yapar
print(1 == 1 or 5 > 10) # true  | false -> true
print(1 != 1 or 5 > 10) # false | false -> false

print( (1 == 1 and 2 > 5) or 6 > 6 and (10 > 5 or 5 ==5 ) )

print(not 1 == 1) # not => tersini almaya yarar
#

students = ["Salih", "Bayram", "Mustafa", "Eminem", 9, True, 55.5]
print(students)
students.append("Çetin") # listenin sonuna ekler
print(students)
students.pop() # listenin son elemanını siler
print(students)

### indexing 
print(students[0])
#
 