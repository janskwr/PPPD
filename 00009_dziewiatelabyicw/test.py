def a():
    print('chuj')
    x = 10
    def b():
        global x
        print(x)
        x = 20
    b()


a()