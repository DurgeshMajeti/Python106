import matplotlib.pyplot as pl
import numpy as np

def unif():
    data = np.random.random(100000)
    return data
def norm():
    data = np.random.normal(size=100000,loc=100,scale=5.0)
    return data
def pois():
    data = np.random.poisson(size=100000)
    return data
def show(data,bin=100):
    pl.hist(data,bins=bin)
    pl.show()
while True:
    print("1.Uniform Distrobution")
    print("2.Normal Distribution")
    print("3.Poission Distribution")
    choice = input("Enter your choice : ")
    if(choice == "1"):
        show(unif(),250)
    elif(choice == "2"):
        show(norm(),250)
    elif(choice == "3"):
        show(pois())
    else:
        break