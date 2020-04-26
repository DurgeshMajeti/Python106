class PartyAnimal:
    x = 0
    name = ''
    def populate():
        self.x += 1
        print("Current population of "+self.name+" is ",self.x)
    def __init__(self, name):
        self.name = name
        self.x = 1
        print(self.name," is born")
    def __del__(self):
        print(self.x," "+self.name+'s'," dead")
    def __str__(self):
        return self.name

animals = []
while True:
    print("Add new member : add <name>")
    print("Populate animal : populate <name>")
    print("Kill an animal : kill <name>")
    print("Extint a family : extint <name>")
    print("Apocalypse : apocalypse")
    command = input("Command : ")
    print("\n\n\n\n\n\n")
    code = command[:command.find(' ')]
    name = command[command.find(' '):]
    if code == 'add':
        a = PartyAnimal(name)
        animals.append(a)
    elif code == 'populate':
        pass