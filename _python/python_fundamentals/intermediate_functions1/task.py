import random

def randInt(**args):
    mini =args["min"] if "min" in args else 0
    maxi =args["max"] if "max" in args else 100
    num = random.random() * (maxi - mini) + mini
    return round(num)

print(randInt()) 
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))