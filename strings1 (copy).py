word = input("Enter a string : ")
#Prints a string letter by letter
i = 0
while i < len(word):
    print(word[i], "---------", word[len(word)-(i+1)])
    i = i+1