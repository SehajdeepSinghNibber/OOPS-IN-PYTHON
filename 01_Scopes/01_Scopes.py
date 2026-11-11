# GLOBAL
username= "Sehajdeep"

def test():
    # LOCAL
    username = "chai"
    print(username)

print(username)
test()

x = 99

# def func(y):
#     z = x+y
#     return z

# result = func(1)

# print(result)

def func2():
    global x
    x = 88

print(x)
func2()
print(x)

def f1():
    x = 12
    def f2():
        print(x)
    f2()

f1()