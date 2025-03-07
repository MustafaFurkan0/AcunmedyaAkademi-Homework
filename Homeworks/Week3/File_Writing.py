def writing_file(fileName, data):
    with open(fileName, "a", encoding='utf-8') as file:
        file.write(data + "\n")

def read_file(fileName):
    with open(fileName, "r", encoding='utf-8') as file:    
        return file.readlines()

fileName = "Test_file.txt"
# open(fileName,"w",) 
print("Enter your message...")
for i in range(5): 
    data = input()
    writing_file(fileName, data)

print("\n*********************************")
print("Dosyadaki veriler:")
lines = read_file(fileName)
for line in lines:
    print(line.strip())
