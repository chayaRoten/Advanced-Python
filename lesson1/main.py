import datetime

#1
def time1(func):
    def culc():
        time11 = datetime.datetime.now()
        func()
        time22 = datetime.datetime.now()
        print(time22 - time11)
    return culc


@time1
def print1():
    x = 0
    for i in range(1000000):
        x += 1



#2
myDict={}
def cache(func):
    def enterToDict():
        if func in myDict:
            return myDict[func]
        x=func()
        if x==None:
            x='void'
        myDict[func]=x
    return  enterToDict

@time1
@cache
def fibunachi():
    n = 40
    num1 = 0
    num2 = 1
    next_number = num2
    count = 1
    while count <= n:
        print(next_number, end=" ")
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
    print()


@cache
def try1():
    v=40
    print(v)
    return 40

if __name__ == '__main__':
    print1()
    fibunachi()
    try1()
    try1()
    print(myDict)

