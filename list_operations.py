li = []
inp = "1"
while True:
    inp = input("Enter a number : ")
    if(inp == "done"):
        break
    try:
        inp = int(inp)
    except:
        print("Bad input")
        continue
    li.append(inp)
#####################################
#                                   #
#####################################
minimum = "0"
maximum = "0"
total = 0
for i in li:
    if(minimum == "0" or minimum > i):
        minimum = i
    if(maximum == "0" or maximum < i):
        maximum = i
    total += i
print("Minimum : ",minimum)
print("Maximum : ",maximum)
print("Total : ",total)
try:
    print("Average : ", total/len(li))
except:
    print("Average : 0")