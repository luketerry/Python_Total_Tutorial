

X = 1
def a():
    X = 2
    print(X)
    def b():
        nonlocal X
        X = 22
        print(X)
        return X
    b()
    print(X)
    return b
if __name__=='__main__':
    a()()