total = 0
count = 0
average = 0
while True:
    i = input("Enter a number : ")
    if(i=="done"):
        break
    try:
        i = float(i)
    except:
        print("bad data")
        continue
    total = total + i
    count = count + 1
average = total / count
print("Total : ",total)
print("Count : ",count)
print("Average : ",average)