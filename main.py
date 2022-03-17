def count(list):
    even = 0
    add = 0
    for i in list:
        if i % 2 == 0:
            even = even + 1
        else:
            add = add + 1
    return even, add


list = [12, 32, 1, 21, 54, 43, 67, 43]

even, add = count(list)
print("even :{} and add :{}".format(even, add))


def feb(n):
    a = 0
    b = 1
    print(a)
    print(b)
    if n == 1:
        print(b)

    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)


feb(10)


def fac(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


result = fac(5)
print(result)


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


result = fact(5)
print(result)

result = fact(5)
print(result)

f = lambda a, b: a + b
result = f(5, 6)
print(result)
