import random
def random_to_file(numbr):
    fhand = open("random_numbers",'w')
    for j in range(0,numbr):
        i = random.random()*100
        fhand.write(str(int(i)) + "\n")
    print("Finished writing into file")
