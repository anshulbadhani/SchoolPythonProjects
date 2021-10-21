# we can also impoert iur own header file to import useful functions

def helloUser(name):
    print("Hello", name)
def add(a, b):
    sum = a + b
    return sum

if __name__ == "__main__":
    print(add(2,3))