from src.hashvsequal.Animals import Animals

cat = Animals("dog", 4)
dog = Animals("dog", 4)

print(id(cat)==id(dog)) #False
print(cat==dog) #True
print(cat.__eq__(dog)) #True


setAnimals = {cat, dog}
print(len(setAnimals)) #1
