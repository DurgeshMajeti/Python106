import numpy as np
def Car_to_Polar():
    x = float(input("Enter x coordinate : "))
    y = float(input("Enter y coordinate : "))
    r = np.sqrt(x*x + y*y)
    theta = (np.arctan(y/x))*180/np.pi
    print("Theta = ",theta)
    print("Radius = ",r)

def Polar_to_Car():
    theta = float(input("Enter theta : "))
    theta = theta/180*np.pi
    r = float(input("Enter radius : "))
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    print("x = ",x)
    print("y = ",y)

while True:
    print("1.Cartesian to Polar")
    print("2.Polar to Cartesian")
    choice = input("Enter your choice : ")
    if(choice == '1'):
        Car_to_Polar()
    elif(choice == '2'):
        Polar_to_Car()
    else:
        break
    print("\n\n")