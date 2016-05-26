from __future__  import print_function
def a():
    d={"x":1}
    print(d["x"])
    def b():
        d["x"]+=1
        return d["x"]
    b()
    print(d["x"])
    return b
a()