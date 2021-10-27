# we can also impoert iur own header file to import useful functions

def helloUser(name):
    print("Hello", name) #This function returns Hello and value of variable name
def add(a, b): # adds a & b
    sum = a + b
    return sum

if __name__ == "__main__": #to check
    print(add(2,3))
