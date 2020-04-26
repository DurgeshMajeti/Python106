values = [1,3,58,63,98,22,85,4,42,74,34,-11,-9,-90,77,12]
min = values[0]
max = values[0]
for i in values:
    if min > i:
        min = i
    if max < i:
        max = i
print(max, "  " ,min)