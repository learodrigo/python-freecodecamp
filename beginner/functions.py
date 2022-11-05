def greeting(name, age):
    print("Hey " + name + ". How's it going? Are you " + str(age) + " ?")


greeting("Leandro", 30)
name = "Carlos"
greeting(name, 50)

print()


def custom_sum(a, b):
    return a + b


def cube(num):
    return pow(num, 3)


print(cube(2))
print(custom_sum(2, 5))


def raise_to_power(base, power):
    res = 1
    for i in range(power):
        res *= base
    return res


print(raise_to_power(4, 3))
