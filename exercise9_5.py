filename = input("Enter file name : ")
try:
    fsearch = open(filename,'r')
except:
    print("File ",filename," cannot be opened")
    exit()
dictionary = dict()
for line in fsearch:
    if(line.find("From: ")!=-1):
        start = line.find("@")
        end = line.find(" ",start)
        line = line[start+1:end]
        if(line in dictionary):
            dictionary[line] = dictionary[line]+1
        else:
            dictionary[line] = 1
print(dictionary)
