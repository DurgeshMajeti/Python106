name = input("Enter a string : ")
dictionary = dict()
for i in name:
    if i in dictionary:
        dictionary[i] = dictionary[i]+1
    else:
        dictionary[i] = 1
#print(dictionary)
for i in dictionary:
    print(i,"  ",dictionary[i])
lst = list(dictionary.values())
lst.sort(None,True)
print(lst)