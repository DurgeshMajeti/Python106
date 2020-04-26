# generating random numbers
import random
for i in range(10):
    print(int(random.random()*1000//1+5000))
print()
print(random.randint(10,20))
print()
t= [1,2,3,4,5,6]
print(random.choice(t))
t=['a','b','c','d','e','f']
print(random.choice(t))