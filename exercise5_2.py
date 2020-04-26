min = None
max = None
indata = None
while indata != 'done':
    indata = input("Enter a number : ")
    try:
        indata = float(indata)
    except:
        print("bad data")
        continue
    if(min == None or max == None):
        min = indata
        max = indata        
    if indata < min:
        min = indata
    if indata > max:
        indata = max
print("Minimum in the list : ",min)
print("Maximum in the list : ",max)