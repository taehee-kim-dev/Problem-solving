
def func2():
    global test
    test -= 1
    print(test)


def func1():
    global test
    test = 10

func1()
func2()