filename = input("Enter file name : ")
fsearch = open(filename,'r')
total_confidence = 0
count = 0
for line in fsearch:
    if line.find("X-DSPAM-Confidence:") != -1:
        ipos = line.find(" ")
        confidence = float(line[ipos:])
        count = count + 1
        total_confidence += confidence
average = total_confidence / count
print("Average spam confidence : ", average)
fsearch.close()