x = 50

def func():
    global x

    print('x equal', x)
    x = 2
    print('Replace global value of x to', x)

func()
print('The value x is', x)