#Goal of this tryout is to create a function from scratch and invoke it for the given problem

def celsius_to_fahernit(temp):
    return ((9/5)*temp+32)

def fahernit_to_celisus(temp):
    return ((temp-32)*(5/9))

print(celsius_to_fahernit(0))
print(fahernit_to_celisus(32))