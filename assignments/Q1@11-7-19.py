import numpy as np

matr = np.genfromtxt("data.csv",delimiter=",")
vet = matr[:,3]
matr = matr[:,:3]
matr = np.matrix(matr)
vet = np.matrix(vet)
try:
    sol = np.matmul(matr.I,vet.T)
except:
    print("Sorry, This system of linear equations is either inconsistent or having multiple solutions")
    print("Please change the input")
    exit()
print(sol)