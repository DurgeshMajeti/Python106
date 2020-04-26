import math
import creating_file
numbr = int(input("Total observations to be generated : "))
creating_file.random_to_file(numbr)
fhand = open("random_numbers")
total = 0
count = 0
var_sum = 0
for abc in fhand:
    total = total + int(abc.strip())
    count = count + 1
print("Frequency : ",count)
print("Mean : ",total/count)
mean = total/count
fhand.close()
fhand = open("random_numbers")
for line in fhand:
    var_sum = var_sum + (int(line.strip()) - mean) ** 2
sd = math.sqrt(var_sum / count)
print("Standard Deviation : ", sd)
fhand.close()