class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
parrot1=parrot("Blu",10)
parrot2=parrot("Woo",15)
print("Parrot 1 name:",parrot1.name)
print("Parrot 1 name:",parrot1.age)
print("Parrot 2 name:",parrot2.name)
print("Parrot 2 name:",parrot2.age)
print("parrot 1 is a",parrot1.species)
print("parrot 2 is also a {}".format(parrot2.species))