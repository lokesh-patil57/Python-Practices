l = ["lokesh", "Bhavesh", "Mohit" , "Darshan", "sh"]
def stripp(l,word):
    n=[]
    for item in l:
        if(word == item):
            l.remove(item)
            print(l)
        n.append(item.strip(word))
    return n

print(stripp(l,"sh"))