name = input("Enter a string : ")
char = input("' Enter character : ")
def index(name , char) :
    for index in range(len(name)) :
        if name[index] == char:
            return index
        
    return -1
           
result = index(name, char)
print("index of char : ", result  )