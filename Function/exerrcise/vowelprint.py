name = input("Enter a string : ")
def rmVowel(name) :
    vowels ="AEIOUaeiou"
    result = " ".join([char for char in name if char not in vowels])
    return result
           
print("String after removing vowel : ",rmVowel(name))
