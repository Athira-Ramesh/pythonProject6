class person:
    def __init__(object,name,age):
        object.name=name
        object.age=age
    def myfunc(abc):
        print("hello my name is"+abc.name)
p1=person("athira","21")
p1.myfunc()
p1.age="21"