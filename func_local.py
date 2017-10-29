x = 50

def func(x):
    print('x equal', x)
    x = 2
    print('replacement local x to', x)

func(x)
print('x still', x)