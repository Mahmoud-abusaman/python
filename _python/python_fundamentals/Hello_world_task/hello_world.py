print("hello world")

name="noella"
print("hello",name)
print("hello"+name)

name=42
print("hello",name)
print("hello "+str(name))

fav_food1="pizza"
fav_food2="sushi"
print(f"I love to eat {fav_food1} and {fav_food2}")
print("I love to eat {} and {}".format(fav_food1,fav_food2))




def a():
    print(1)
    x=b()
    print(x)
    return 10
def b():
    print(3)
    return 5

y=a()
print(y)