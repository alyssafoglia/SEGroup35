#function1
def removeVowels(strWithVowels):
    
    if (type(strWithVowels) != str):
        raise TypeError("Invalid type")
    
    vowels = "aeiouAEIOU"
    
    for char in vowels:
        strWithVowels = strWithVowels.replace(char,"")
    
    return strWithVowels

#function2
def multiply(n1,n2):
    return n1*n2