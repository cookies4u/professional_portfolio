age = 30
name = "juan"

print(f'hello {name} there yall, i\'m {age} years old')

def hello(name, age=0):
    if age > 18:
        print('hello {} there yall, i\'m {} years old'.format(name,age))
    else:
        print("older than 18")

hello('jay', 12)
hello('jay')

dognames = ['dog1', 'dog2', 'dog3']
dognames[1] = 'janes'
print(dognames)


age = 0

# ctl + c -- to stop infinite loop
while age < 18:
    print(age)
    age += 1

for dog in dognames:
    print(dog)

for x in range(1,10):
    print(x)

dogs = {'fido': 8, 'sally': 17,'sean': 20}
dogs['sarah'] = 6
print(dogs)
print(dogs['sally'])
del(dogs['sean'])
print(dogs)

class Dog:
    dogInfo = 'dogs are cool'

    def bark(self, str):
        print('BARK' + str)

mydog = Dog()
mydog.bark('blass')
mydog.name = 'fido'
mydog.age = 16
print(mydog.name)
print(mydog.age)

class Dogv2:
    def __init__(self, name, age, fur):
        self.name = name
        self.age = age
        self.fur = fur

    def bark(self, str):
        print('BARK' + str)

mydog = Dogv2('fido',12,'brown')

print(mydog.age)
